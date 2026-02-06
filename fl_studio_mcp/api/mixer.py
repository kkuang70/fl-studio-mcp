"""
FL Studio Mixer API wrapper.

Provides control over mixer tracks, levels, and routing.
"""

from typing import Dict, List, Any

from fl_studio_mcp.core.bridge import FLStudioBridge


class MixerAPI:
    """
    Wrapper for FL Studio mixer functions.

    Controls mixer track operations, including levels,
    pans, sends, and routing.
    """

    def __init__(self, bridge: FLStudioBridge):
        """
        Initialize mixer API.

        Args:
            bridge: FLStudioBridge instance
        """
        self.bridge = bridge

    def get_track_count(self) -> int:
        """
        Get the number of mixer tracks.

        Returns:
            Number of mixer tracks
        """
        result = self.bridge.safe_execute(
            "mixer.trackCount()"
        )
        if result.get("success"):
            return int(result.get("data", 0))
        return 0

    def get_track_name(self, track_id: int) -> str:
        """
        Get the name of a mixer track.

        Args:
            track_id: Mixer track index (0 = Master)

        Returns:
            Track name
        """
        result = self.bridge.safe_execute(
            f'mixer.getTrackName({track_id})'
        )
        if result.get("success"):
            return str(result.get("data", f"Track {track_id}"))
        return f"Track {track_id}"

    def set_track_name(self, track_id: int, name: str) -> bool:
        """
        Set the name of a mixer track.

        Args:
            track_id: Mixer track index
            name: New track name

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            f'mixer.setTrackName({track_id}, "{name}")'
        )
        return result.get("success", False)

    def get_volume(self, track_id: int) -> float:
        """
        Get the volume of a mixer track.

        Args:
            track_id: Mixer track index

        Returns:
            Volume level (0.0 - 1.0)
        """
        result = self.bridge.safe_execute(
            f"mixer.getTrackVolume({track_id})"
        )
        if result.get("success"):
            return float(result.get("data", 0.8))
        return 0.8

    def set_volume(self, track_id: int, volume: float) -> bool:
        """
        Set the volume of a mixer track.

        Args:
            track_id: Mixer track index
            volume: Volume level (0.0 - 1.0)

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            f"mixer.setTrackVolume({track_id}, {volume})"
        )
        return result.get("success", False)

    def get_pan(self, track_id: int) -> float:
        """
        Get the pan of a mixer track.

        Args:
            track_id: Mixer track index

        Returns:
            Pan value (-1.0 = left, 0.0 = center, 1.0 = right)
        """
        result = self.bridge.safe_execute(
            f"mixer.getTrackPan({track_id})"
        )
        if result.get("success"):
            return float(result.get("data", 0.0))
        return 0.0

    def set_pan(self, track_id: int, pan: float) -> bool:
        """
        Set the pan of a mixer track.

        Args:
            track_id: Mixer track index
            pan: Pan value (-1.0 = left, 0.0 = center, 1.0 = right)

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            f"mixer.setTrackPan({track_id}, {pan})"
        )
        return result.get("success", False)

    def get_all_levels(self) -> List[Dict[str, Any]]:
        """
        Get volume and pan levels for all mixer tracks.

        Returns:
            List of mixer track information
        """
        track_count = self.get_track_count()
        tracks = []

        for i in range(track_count):
            track_info = {
                "track_id": i,
                "name": self.get_track_name(i),
                "volume": self.get_volume(i),
                "pan": self.get_pan(i),
            }
            tracks.append(track_info)

        return tracks

    def route_channel(self, channel_id: int, mixer_track_id: int) -> bool:
        """
        Route a channel to a mixer track.

        Args:
            channel_id: Channel index
            mixer_track_id: Mixer track index

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            f"channels.routeToMixerTrack({channel_id}, {mixer_track_id})"
        )
        return result.get("success", False)

    def get_meter_level(self, track_id: int) -> float:
        """
        Get the current meter level for a track.

        Args:
            track_id: Mixer track index

        Returns:
            Current level (0.0 - 1.0)
        """
        result = self.bridge.safe_execute(
            f"mixer.getTrackMeterLevel({track_id})"
        )
        if result.get("success"):
            return float(result.get("data", 0.0))
        return 0.0

    def solo_track(self, track_id: int, solo: bool = True) -> bool:
        """
        Solo or unsolo a mixer track.

        Args:
            track_id: Mixer track index
            solo: True to solo, False to unsolo

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            f"mixer soloTrack {track_id}"
        )
        return result.get("success", False)

    def mute_track(self, track_id: int, mute: bool = True) -> bool:
        """
        Mute or unmute a mixer track.

        Args:
            track_id: Mixer track index
            mute: True to mute, False to unmute

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            f"mixer muteTrack {track_id}"
        )
        return result.get("success", False)
