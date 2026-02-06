"""
FL Studio Transport API wrapper.

Provides control over playback, recording, and transport functions.
"""

from typing import Dict, Any

from fl_studio_mcp.core.bridge import FLStudioBridge
from fl_studio_mcp.core.exceptions import FLStudioMCPError


class TransportAPI:
    """
    Wrapper for FL Studio transport functions.

    Controls playback, recording, and other transport-related operations.
    """

    def __init__(self, bridge: FLStudioBridge):
        """
        Initialize transport API.

        Args:
            bridge: FLStudioBridge instance
        """
        self.bridge = bridge

    def start(self) -> bool:
        """
        Start playback.

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            "transport.start()"
        )
        return result.get("success", False)

    def stop(self) -> bool:
        """
        Stop playback.

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            "transport.stop()"
        )
        return result.get("success", False)

    def pause(self) -> bool:
        """
        Pause playback.

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            "transport.start() if transport.isPlaying() else transport.stop()"
        )
        return result.get("success", False)

    def record(self) -> bool:
        """
        Start recording.

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            "transport.record()"
        )
        return result.get("success", False)

    def is_playing(self) -> bool:
        """
        Check if currently playing.

        Returns:
            True if playing
        """
        result = self.bridge.safe_execute(
            "transport.isPlaying()"
        )
        if result.get("success"):
            return bool(result.get("data", False))
        return False

    def is_recording(self) -> bool:
        """
        Check if currently recording.

        Returns:
            True if recording
        """
        result = self.bridge.safe_execute(
            "transport.isRecording()"
        )
        if result.get("success"):
            return bool(result.get("data", False))
        return False

    def get_status(self) -> Dict[str, Any]:
        """
        Get current transport status.

        Returns:
            Dictionary with transport status information
        """
        is_playing = self.is_playing()
        is_recording = self.is_recording()

        # Get current position in beats
        position_result = self.bridge.safe_execute(
            "transport.getSongPos()"
        )

        position = 0.0
        if position_result.get("success"):
            position = position_result.get("data", 0)

        return {
            "playing": is_playing,
            "recording": is_recording,
            "position_beats": position,
        }

    def jump_to(self, position: float) -> bool:
        """
        Jump to position in song.

        Args:
            position: Position in beats

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            f"transport.setSongPos({position})"
        )
        return result.get("success", False)

    def set_loop_mode(self, enabled: bool) -> bool:
        """
        Enable or disable loop mode.

        Args:
            enabled: True to enable loop mode

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            f"transport.setLoopMode({1 if enabled else 0})"
        )
        return result.get("success", False)

    def get_loop_mode(self) -> bool:
        """
        Get current loop mode state.

        Returns:
            True if loop mode is enabled
        """
        result = self.bridge.safe_execute(
            "transport.getLoopMode()"
        )
        if result.get("success"):
            return result.get("data", 0) > 0
        return False

    def set_tempo(self, bpm: float) -> bool:
        """
        Set project tempo.

        Args:
            bpm: Tempo in beats per minute

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            f"transport.setTempo({bpm})"
        )
        return result.get("success", False)

    def get_tempo(self) -> float:
        """
        Get current tempo.

        Returns:
            Tempo in BPM
        """
        result = self.bridge.safe_execute(
            "transport.getTempo()"
        )
        if result.get("success"):
            return float(result.get("data", 120.0))
        return 120.0
