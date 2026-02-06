"""
FL Studio MCP Server - Main entry point.

This is the main MCP server that exposes tools for controlling FL Studio.
"""

import asyncio
import logging
from typing import Any

from fastmcp import FastMCP
from pydantic import BaseModel, Field

from fl_studio_mcp.core.bridge import get_bridge
from fl_studio_mcp.core.connection import ConnectionManager
from fl_studio_mcp.api.transport import TransportAPI
from fl_studio_mcp.api.channels import ChannelAPI
from fl_studio_mcp.api.mixer import MixerAPI
from fl_studio_mcp.utils.validation import (
    validate_tempo,
    validate_channel_id,
    validate_mixer_track_id,
    validate_volume,
    validate_midi_key,
    validate_velocity,
    validate_position,
    validate_duration,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create MCP server
mcp = FastMCP("fl-studio-server")

# Initialize bridge and APIs
bridge = get_bridge()
connection_manager = ConnectionManager(bridge)
transport_api = TransportAPI(bridge)
channel_api = ChannelAPI(bridge)
mixer_api = MixerAPI(bridge)


# ============================================================================
# CONNECTION TOOLS
# ============================================================================

@mcp.tool()
async def connect_to_fl_studio() -> dict[str, Any]:
    """
    Connect to FL Studio.

    Establishes a connection to FL Studio via Flapi.
    FL Studio must be running and the Flapi script must be loaded.

    Returns:
        Connection status and information
    """
    try:
        success = connection_manager.connect()
        if success:
            status = connection_manager.get_connection_status()
            return {
                "success": True,
                "message": "Successfully connected to FL Studio",
                "connection_info": status,
            }
        else:
            return {
                "success": False,
                "message": "Failed to connect to FL Studio",
            }
    except Exception as e:
        logger.error(f"Error connecting to FL Studio: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


@mcp.tool()
async def get_connection_status() -> dict[str, Any]:
    """
    Get current connection status.

    Returns information about the current connection to FL Studio.

    Returns:
        Connection status information
    """
    try:
        status = connection_manager.get_connection_status()
        return {
            "success": True,
            "status": status,
        }
    except Exception as e:
        logger.error(f"Error getting connection status: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


# ============================================================================
# TRANSPORT TOOLS
# ============================================================================

@mcp.tool()
async def transport_start() -> dict[str, Any]:
    """
    Start FL Studio playback.

    Begins playback from the current position.

    Returns:
        Success status and message
    """
    try:
        connection_manager.ensure_connected()
        success = transport_api.start()

        return {
            "success": success,
            "message": "Playback started" if success else "Failed to start playback",
        }
    except Exception as e:
        logger.error(f"Error starting playback: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


@mcp.tool()
async def transport_stop() -> dict[str, Any]:
    """
    Stop FL Studio playback.

    Stops playback and returns to the beginning.

    Returns:
        Success status and message
    """
    try:
        connection_manager.ensure_connected()
        success = transport_api.stop()

        return {
            "success": success,
            "message": "Playback stopped" if success else "Failed to stop playback",
        }
    except Exception as e:
        logger.error(f"Error stopping playback: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


@mcp.tool()
async def get_transport_status() -> dict[str, Any]:
    """
    Get current transport status.

    Returns information about playback state, recording state, and position.

    Returns:
        Transport status information including playing, recording, and position
    """
    try:
        connection_manager.ensure_connected()
        status = transport_api.get_status()

        return {
            "success": True,
            "status": status,
        }
    except Exception as e:
        logger.error(f"Error getting transport status: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


# ============================================================================
# PROJECT TOOLS
# ============================================================================

@mcp.tool()
async def get_project_info() -> dict[str, Any]:
    """
    Get information about the current FL Studio project.

    Returns detailed information about the project including tempo,
    channel count, mixer track count, and transport status.

    Returns:
        Project information dictionary
    """
    try:
        connection_manager.ensure_connected()

        # Get tempo
        tempo = transport_api.get_tempo()

        # Get channel count
        channel_count = channel_api.get_count()

        # Get mixer track count
        mixer_track_count = mixer_api.get_track_count()

        # Get transport status
        transport_status = transport_api.get_status()

        project_info = {
            "tempo_bpm": tempo,
            "channel_count": channel_count,
            "mixer_track_count": mixer_track_count,
            "transport": transport_status,
        }

        return {
            "success": True,
            "project_info": project_info,
        }
    except Exception as e:
        logger.error(f"Error getting project info: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


@mcp.tool()
async def set_tempo(bpm: float) -> dict[str, Any]:
    """
    Set the project tempo.

    Args:
        bpm: Tempo in beats per minute (20-999)

    Returns:
        Success status and new tempo
    """
    try:
        connection_manager.ensure_connected()

        # Validate tempo
        validated_bpm = validate_tempo(bpm)

        # Set tempo
        success = transport_api.set_tempo(validated_bpm)

        return {
            "success": success,
            "tempo_bpm": validated_bpm,
            "message": f"Tempo set to {validated_bpm} BPM" if success else "Failed to set tempo",
        }
    except Exception as e:
        logger.error(f"Error setting tempo: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


# ============================================================================
# CHANNEL TOOLS
# ============================================================================

@mcp.tool()
async def get_channels() -> dict[str, Any]:
    """
    Get all channels in the project.

    Returns a list of all channels with their names, colors, and selection status.

    Returns:
        List of channel information
    """
    try:
        connection_manager.ensure_connected()

        channels = channel_api.get_all()

        return {
            "success": True,
            "channels": channels,
            "count": len(channels),
        }
    except Exception as e:
        logger.error(f"Error getting channels: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


@mcp.tool()
async def select_channel(channel_id: int) -> dict[str, Any]:
    """
    Select a channel by ID.

    Args:
        channel_id: Channel index to select

    Returns:
        Success status and message
    """
    try:
        connection_manager.ensure_connected()

        # Validate channel ID
        max_channels = channel_api.get_count()
        validated_id = validate_channel_id(channel_id, max_channels)

        # Select channel
        success = channel_api.select(validated_id)

        channel_name = channel_api.get_name(validated_id)

        return {
            "success": success,
            "channel_id": validated_id,
            "channel_name": channel_name,
            "message": f"Selected channel: {channel_name}" if success else "Failed to select channel",
        }
    except Exception as e:
        logger.error(f"Error selecting channel: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


# ============================================================================
# MIXER TOOLS
# ============================================================================

@mcp.tool()
async def get_mixer_levels() -> dict[str, Any]:
    """
    Get volume and pan levels for all mixer tracks.

    Returns current levels for all mixer tracks in the project.

    Returns:
        List of mixer track information with levels
    """
    try:
        connection_manager.ensure_connected()

        levels = mixer_api.get_all_levels()

        return {
            "success": True,
            "tracks": levels,
            "count": len(levels),
        }
    except Exception as e:
        logger.error(f"Error getting mixer levels: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


@mcp.tool()
async def set_mixer_fader(track_id: int, volume: float) -> dict[str, Any]:
    """
    Set the volume fader for a mixer track.

    Args:
        track_id: Mixer track index (0 = Master)
        volume: Volume level (0.0 - 1.0)

    Returns:
        Success status and new volume
    """
    try:
        connection_manager.ensure_connected()

        # Validate inputs
        max_tracks = mixer_api.get_track_count()
        validated_track_id = validate_mixer_track_id(track_id, max_tracks)
        validated_volume = validate_volume(volume)

        # Set volume
        success = mixer_api.set_volume(validated_track_id, validated_volume)

        track_name = mixer_api.get_track_name(validated_track_id)

        return {
            "success": success,
            "track_id": validated_track_id,
            "track_name": track_name,
            "volume": validated_volume,
            "message": f"Set {track_name} volume to {validated_volume:.2f}" if success else "Failed to set volume",
        }
    except Exception as e:
        logger.error(f"Error setting mixer fader: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


# ============================================================================
# NOTE TOOLS (Basic Implementation)
# ============================================================================

@mcp.tool()
async def create_note(
    channel_id: int,
    position: float,
    key: int,
    duration: float,
    velocity: int = 100
) -> dict[str, Any]:
    """
    Create a MIDI note in a channel.

    Adds a note to the piano roll for the specified channel.

    Args:
        channel_id: Channel index
        position: Position in beats (e.g., 0.0 for start)
        key: MIDI key number (0-127, where 60 = C4)
        duration: Note duration in beats
        velocity: Note velocity (0-127, default 100)

    Returns:
        Success status and note information
    """
    try:
        connection_manager.ensure_connected()

        # Validate inputs
        max_channels = channel_api.get_count()
        validated_channel_id = validate_channel_id(channel_id, max_channels)
        validated_position = validate_position(position)
        validated_key = validate_midi_key(key)
        validated_duration = validate_duration(duration)
        validated_velocity = validate_velocity(velocity)

        # Add note
        success = channel_api.set_piano_roll_note(
            validated_channel_id,
            validated_position,
            validated_key,
            validated_duration,
            validated_velocity,
        )

        return {
            "success": success,
            "note": {
                "channel_id": validated_channel_id,
                "position": validated_position,
                "key": validated_key,
                "duration": validated_duration,
                "velocity": validated_velocity,
            },
            "message": "Note created successfully" if success else "Failed to create note",
        }
    except Exception as e:
        logger.error(f"Error creating note: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
        }


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Main entry point for the MCP server."""
    logger.info("Starting FL Studio MCP Server...")

    # Run the MCP server
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
