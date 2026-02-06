"""
Validation utilities for FL Studio MCP server.

Provides input validation functions for all parameters.
"""

from typing import Tuple, Union

from fl_studio_mcp.core.exceptions import InvalidParameterError


def validate_tempo(bpm: float) -> float:
    """
    Validate and clamp tempo value.

    Args:
        bpm: Tempo in beats per minute

    Returns:
        Validated tempo value

    Raises:
        InvalidParameterError: If tempo is out of valid range
    """
    MIN_TEMPO = 20.0
    MAX_TEMPO = 999.0

    try:
        bpm = float(bpm)
    except (TypeError, ValueError) as e:
        raise InvalidParameterError(
            f"Tempo must be a number, got {bpm}",
            parameter_name="tempo",
            parameter_value=bpm
        ) from e

    if not (MIN_TEMPO <= bpm <= MAX_TEMPO):
        raise InvalidParameterError(
            f"Tempo must be between {MIN_TEMPO} and {MAX_TEMPO} BPM, got {bpm}",
            parameter_name="tempo",
            parameter_value=bpm
        )

    return bpm


def validate_midi_key(key: int) -> int:
    """
    Validate MIDI key number.

    Args:
        key: MIDI note number (0-127)

    Returns:
        Validated key number

    Raises:
        InvalidParameterError: If key is out of range
    """
    try:
        key = int(key)
    except (TypeError, ValueError) as e:
        raise InvalidParameterError(
            f"MIDI key must be an integer, got {key}",
            parameter_name="key",
            parameter_value=key
        ) from e

    if not (0 <= key <= 127):
        raise InvalidParameterError(
            f"MIDI key must be between 0 and 127, got {key}",
            parameter_name="key",
            parameter_value=key
        )

    return key


def validate_velocity(velocity: int) -> int:
    """
    Validate and clamp velocity value.

    Args:
        velocity: MIDI velocity (0-127)

    Returns:
        Validated velocity value

    Raises:
        InvalidParameterError: If velocity is invalid
    """
    try:
        velocity = int(velocity)
    except (TypeError, ValueError) as e:
        raise InvalidParameterError(
            f"Velocity must be an integer, got {velocity}",
            parameter_name="velocity",
            parameter_value=velocity
        ) from e

    if not (0 <= velocity <= 127):
        raise InvalidParameterError(
            f"Velocity must be between 0 and 127, got {velocity}",
            parameter_name="velocity",
            parameter_value=velocity
        )

    return velocity


def validate_channel_id(channel_id: int, max_channels: int = 999) -> int:
    """
    Validate channel ID.

    Args:
        channel_id: Channel index
        max_channels: Maximum number of channels allowed

    Returns:
        Validated channel ID

    Raises:
        InvalidParameterError: If channel ID is invalid
    """
    try:
        channel_id = int(channel_id)
    except (TypeError, ValueError) as e:
        raise InvalidParameterError(
            f"Channel ID must be an integer, got {channel_id}",
            parameter_name="channel_id",
            parameter_value=channel_id
        ) from e

    if not (0 <= channel_id <= max_channels):
        raise InvalidParameterError(
            f"Channel ID must be between 0 and {max_channels}, got {channel_id}",
            parameter_name="channel_id",
            parameter_value=channel_id
        )

    return channel_id


def validate_pattern_id(pattern_id: int, max_patterns: int = 999) -> int:
    """
    Validate pattern ID.

    Args:
        pattern_id: Pattern index
        max_patterns: Maximum number of patterns allowed

    Returns:
        Validated pattern ID

    Raises:
        InvalidParameterError: If pattern ID is invalid
    """
    try:
        pattern_id = int(pattern_id)
    except (TypeError, ValueError) as e:
        raise InvalidParameterError(
            f"Pattern ID must be an integer, got {pattern_id}",
            parameter_name="pattern_id",
            parameter_value=pattern_id
        ) from e

    if not (0 <= pattern_id <= max_patterns):
        raise InvalidParameterError(
            f"Pattern ID must be between 0 and {max_patterns}, got {pattern_id}",
            parameter_name="pattern_id",
            parameter_value=pattern_id
        )

    return pattern_id


def validate_mixer_track_id(track_id: int, max_tracks: int = 999) -> int:
    """
    Validate mixer track ID.

    Args:
        track_id: Mixer track index
        max_tracks: Maximum number of mixer tracks

    Returns:
        Validated mixer track ID

    Raises:
        InvalidParameterError: If track ID is invalid
    """
    try:
        track_id = int(track_id)
    except (TypeError, ValueError) as e:
        raise InvalidParameterError(
            f"Mixer track ID must be an integer, got {track_id}",
            parameter_name="track_id",
            parameter_value=track_id
        ) from e

    if not (0 <= track_id <= max_tracks):
        raise InvalidParameterError(
            f"Mixer track ID must be between 0 and {max_tracks}, got {track_id}",
            parameter_name="track_id",
            parameter_value=track_id
        )

    return track_id


def validate_volume(volume: float) -> float:
    """
    Validate and clamp volume value.

    Args:
        volume: Volume level (0.0 - 1.0)

    Returns:
        Validated volume value

    Raises:
        InvalidParameterError: If volume is invalid
    """
    try:
        volume = float(volume)
    except (TypeError, ValueError) as e:
        raise InvalidParameterError(
            f"Volume must be a number, got {volume}",
            parameter_name="volume",
            parameter_value=volume
        ) from e

    if not (0.0 <= volume <= 1.0):
        raise InvalidParameterError(
            f"Volume must be between 0.0 and 1.0, got {volume}",
            parameter_name="volume",
            parameter_value=volume
        )

    return volume


def validate_pan(pan: float) -> float:
    """
    Validate and clamp pan value.

    Args:
        pan: Pan value (-1.0 to 1.0, where -1 is left, 0 is center, 1 is right)

    Returns:
        Validated pan value

    Raises:
        InvalidParameterError: If pan is invalid
    """
    try:
        pan = float(pan)
    except (TypeError, ValueError) as e:
        raise InvalidParameterError(
            f"Pan must be a number, got {pan}",
            parameter_name="pan",
            parameter_value=pan
        ) from e

    if not (-1.0 <= pan <= 1.0):
        raise InvalidParameterError(
            f"Pan must be between -1.0 and 1.0, got {pan}",
            parameter_name="pan",
            parameter_value=pan
        )

    return pan


def validate_position(position: float) -> float:
    """
    Validate position value.

    Args:
        position: Position in beats (must be >= 0)

    Returns:
        Validated position value

    Raises:
        InvalidParameterError: If position is invalid
    """
    try:
        position = float(position)
    except (TypeError, ValueError) as e:
        raise InvalidParameterError(
            f"Position must be a number, got {position}",
            parameter_name="position",
            parameter_value=position
        ) from e

    if position < 0:
        raise InvalidParameterError(
            f"Position must be >= 0, got {position}",
            parameter_name="position",
            parameter_value=position
        )

    return position


def validate_duration(duration: float) -> float:
    """
    Validate duration value.

    Args:
        duration: Duration in beats (must be > 0)

    Returns:
        Validated duration value

    Raises:
        InvalidParameterError: If duration is invalid
    """
    try:
        duration = float(duration)
    except (TypeError, ValueError) as e:
        raise InvalidParameterError(
            f"Duration must be a number, got {duration}",
            parameter_name="duration",
            parameter_value=duration
        ) from e

    if duration <= 0:
        raise InvalidParameterError(
            f"Duration must be > 0, got {duration}",
            parameter_name="duration",
            parameter_value=duration
        )

    return duration


def validate_color(color: str) -> str:
    """
    Validate color hex string.

    Args:
        color: Color in hex format (e.g., "#FF5733" or "FF5733")

    Returns:
        Validated color string with # prefix

    Raises:
        InvalidParameterError: If color is invalid
    """
    if not isinstance(color, str):
        raise InvalidParameterError(
            f"Color must be a string, got {type(color)}",
            parameter_name="color",
            parameter_value=color
        )

    # Remove # if present
    color = color.lstrip("#")

    # Validate hex format
    if len(color) != 6:
        raise InvalidParameterError(
            f"Color must be 6-character hex string (e.g., 'FF5733'), got '{color}'",
            parameter_name="color",
            parameter_value=color
        )

    try:
        int(color, 16)
    except ValueError as e:
        raise InvalidParameterError(
            f"Color must be a valid hex string, got '{color}'",
            parameter_name="color",
            parameter_value=color
        ) from e

    return f"#{color}"


def validate_file_path(file_path: str, must_exist: bool = False) -> str:
    """
    Validate file path.

    Args:
        file_path: File path to validate
        must_exist: If True, file must exist

    Returns:
        Validated file path

    Raises:
        InvalidParameterError: If file path is invalid
    """
    import os

    if not isinstance(file_path, str):
        raise InvalidParameterError(
            f"File path must be a string, got {type(file_path)}",
            parameter_name="file_path",
            parameter_value=file_path
        )

    file_path = os.path.expanduser(file_path)

    if must_exist and not os.path.exists(file_path):
        raise InvalidParameterError(
            f"File does not exist: {file_path}",
            parameter_name="file_path",
            parameter_value=file_path
        )

    return file_path
