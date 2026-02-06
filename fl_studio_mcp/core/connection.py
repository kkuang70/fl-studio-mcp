"""
Connection management for FL Studio MCP server.

This module handles connection lifecycle and configuration.
"""

import logging
import os
from typing import Optional

from dotenv import load_dotenv

from fl_studio_mcp.core.bridge import FLStudioBridge

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


class ConnectionManager:
    """
    Manages FL Studio connection lifecycle.

    Handles connection initialization, configuration from environment,
    and connection health monitoring.
    """

    def __init__(self, bridge: Optional[FLStudioBridge] = None):
        """
        Initialize connection manager.

        Args:
            bridge: FLStudioBridge instance (uses global instance if None)
        """
        self.bridge = bridge or FLStudioBridge()
        self._auto_connect = os.getenv("FL_AUTO_CONNECT", "false").lower() == "true"

    def get_midi_port_names(self) -> tuple[str, str]:
        """
        Get MIDI port names from environment or defaults.

        Returns:
            Tuple of (request_port, response_port)
        """
        request_port = os.getenv("FLAPI_REQUEST_PORT", "Flapi Request")
        response_port = os.getenv("FLAPI_RESPONSE_PORT", "Flapi Response")
        return request_port, response_port

    def connect(self) -> bool:
        """
        Establish connection to FL Studio.

        Returns:
            True if connection successful

        Raises:
            FLStudioConnectionError: If connection fails
        """
        if self.bridge.is_connected:
            logger.info("Already connected to FL Studio")
            return True

        request_port, response_port = self.get_midi_port_names()

        logger.info(f"Connecting to FL Studio (ports: {request_port}, {response_port})")
        return self.bridge.connect(request_port, response_port)

    def disconnect(self) -> None:
        """Close connection to FL Studio."""
        self.bridge.disconnect()

    def ensure_connected(self) -> None:
        """
        Ensure connection is active, connect if needed.

        Raises:
            FLStudioConnectionError: If connection fails
        """
        if not self.bridge.is_connected:
            if self._auto_connect:
                logger.info("Auto-connecting to FL Studio")
                self.connect()
            else:
                raise FLStudioConnectionError(
                    "Not connected to FL Studio. Connect manually first."
                )

    def get_connection_status(self) -> dict:
        """
        Get current connection status.

        Returns:
            Dictionary with connection status information
        """
        status = self.bridge.get_connection_info()
        request_port, response_port = self.get_midi_port_names()

        status.update({
            "midi_ports": {
                "request": request_port,
                "response": response_port,
            },
            "auto_connect": self._auto_connect,
        })

        return status

    def health_check(self) -> bool:
        """
        Check if connection is healthy.

        Returns:
            True if connection is healthy
        """
        if not self.bridge.is_connected:
            return False

        try:
            # Try to execute a simple command
            result = self.bridge.safe_execute("1 + 1")
            return result.get("success", False)
        except Exception as e:
            logger.warning(f"Health check failed: {e}")
            return False
