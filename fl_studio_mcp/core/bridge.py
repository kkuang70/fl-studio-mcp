"""
Flapi bridge wrapper for communicating with FL Studio.

This module provides a bridge between the MCP server and FL Studio via Flapi.
"""

import logging
from typing import Any, Optional

from fl_studio_mcp.core.exceptions import (
    FlapiNotFoundError,
    FLStudioConnectionError,
    FLStudioNotConnectedError,
    FLStudioAPIError,
    MIDIPortNotFoundError,
)

logger = logging.getLogger(__name__)


class FLStudioBridge:
    """
    Bridge to FL Studio using Flapi.

    This class manages the connection to FL Studio and executes
    Python code remotely within FL Studio via the Flapi library.
    """

    def __init__(self):
        self._connected = False
        self._flapi = None
        self._attempted_import = False

    def _ensure_flapi(self) -> None:
        """Ensure Flapi is imported and available."""
        if self._attempted_import:
            return

        try:
            import flapi

            self._flapi = flapi
            self._attempted_import = True
            logger.info("Flapi imported successfully")
        except ImportError as e:
            raise FlapiNotFoundError(
                "Flapi is not installed. Install it with: pip install flapi"
            ) from e

    def connect(self, request_port: str = "Flapi Request", response_port: str = "Flapi Response") -> bool:
        """
        Connect to FL Studio via Flapi.

        Args:
            request_port: Name of the MIDI request port
            response_port: Name of the MIDI response port

        Returns:
            True if connection successful

        Raises:
            FlapiNotFoundError: If Flapi is not installed
            FLStudioConnectionError: If connection fails
        """
        if self._connected:
            logger.warning("Already connected to FL Studio")
            return True

        self._ensure_flapi()

        try:
            # Enable Flapi connection
            self._flapi.enable()
            self._connected = True
            logger.info(f"Connected to FL Studio (request={request_port}, response={response_port})")
            return True
        except Exception as e:
            raise FLStudioConnectionError(
                f"Failed to connect to FL Studio: {str(e)}\n"
                f"Make sure FL Studio is running and Flapi script is loaded."
            ) from e

    def disconnect(self) -> None:
        """Disconnect from FL Studio."""
        if self._connected:
            try:
                if self._flapi:
                    self._flapi.disable()
            except Exception as e:
                logger.warning(f"Error during disconnect: {e}")
            finally:
                self._connected = False
                logger.info("Disconnected from FL Studio")

    @property
    def is_connected(self) -> bool:
        """Check if currently connected to FL Studio."""
        return self._connected

    def execute(self, code: str) -> Any:
        """
        Execute Python code in FL Studio.

        Args:
            code: Python code to execute

        Returns:
            Result of the code execution

        Raises:
            FLStudioNotConnectedError: If not connected
            FLStudioAPIError: If execution fails
        """
        if not self._connected:
            raise FLStudioNotConnectedError(
                "Not connected to FL Studio. Call connect() first."
            )

        try:
            # Execute the code via Flapi
            result = eval(code)
            logger.debug(f"Executed code: {code[:50]}...")
            return result
        except Exception as e:
            logger.error(f"Error executing code: {e}")
            raise FLStudioAPIError(
                f"Failed to execute code in FL Studio: {str(e)}",
                api_component="executor"
            ) from e

    def safe_execute(self, code: str) -> dict:
        """
        Execute code with error handling.

        Args:
            code: Python code to execute

        Returns:
            Dictionary with success status and data/error
        """
        try:
            result = self.execute(code)
            return {"success": True, "data": result}
        except FLStudioMCPError as e:
            return {"success": False, "error": str(e), "type": e.__class__.__name__}
        except Exception as e:
            return {"success": False, "error": str(e), "type": "unexpected_error"}

    def get_connection_info(self) -> dict:
        """
        Get information about the current connection.

        Returns:
            Dictionary with connection status and info
        """
        return {
            "connected": self._connected,
            "flapi_available": self._attempted_import,
            "flapi_version": self._get_flapi_version() if self._flapi else None,
        }

    def _get_flapi_version(self) -> Optional[str]:
        """Get Flapi version if available."""
        try:
            import flapi
            return getattr(flapi, "__version__", "unknown")
        except:
            return None


# Global bridge instance
_bridge_instance: Optional[FLStudioBridge] = None


def get_bridge() -> FLStudioBridge:
    """Get the global bridge instance."""
    global _bridge_instance
    if _bridge_instance is None:
        _bridge_instance = FLStudioBridge()
    return _bridge_instance
