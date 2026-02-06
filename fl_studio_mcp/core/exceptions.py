"""Custom exceptions for FL Studio MCP server."""


class FLStudioMCPError(Exception):
    """Base exception for FL Studio MCP errors."""

    pass


class FLStudioConnectionError(FLStudioMCPError):
    """Raised when connection to FL Studio fails."""

    pass


class FLStudioNotConnectedError(FLStudioMCPError):
    """Raised when attempting an operation while not connected to FL Studio."""

    pass


class FLStudioAPIError(FLStudioMCPError):
    """Raised when FL Studio API returns an error."""

    def __init__(self, message: str, api_component: str = None):
        super().__init__(message)
        self.api_component = api_component


class InvalidParameterError(FLStudioMCPError):
    """Raised when an invalid parameter is provided."""

    def __init__(self, message: str, parameter_name: str = None, parameter_value: any = None):
        super().__init__(message)
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value


class FlapiNotFoundError(FLStudioMCPError):
    """Raised when Flapi is not installed or not available."""

    pass


class MIDIPortNotFoundError(FLStudioMCPError):
    """Raised when required MIDI ports are not found."""

    def __init__(self, message: str, port_name: str = None):
        super().__init__(message)
        self.port_name = port_name
