"""
FL Studio Channels API wrapper.

Provides control over channel rack, instruments, and channels.
"""

from typing import Dict, List, Any

from fl_studio_mcp.core.bridge import FLStudioBridge


class ChannelAPI:
    """
    Wrapper for FL Studio channels functions.

    Controls channel rack operations, including instruments,
    channel selection, and channel properties.
    """

    def __init__(self, bridge: FLStudioBridge):
        """
        Initialize channel API.

        Args:
            bridge: FLStudioBridge instance
        """
        self.bridge = bridge

    def get_count(self) -> int:
        """
        Get the number of channels in the project.

        Returns:
            Number of channels
        """
        result = self.bridge.safe_execute(
            "channels.channelCount()"
        )
        if result.get("success"):
            return int(result.get("data", 0))
        return 0

    def get_name(self, channel_id: int) -> str:
        """
        Get the name of a channel.

        Args:
            channel_id: Channel index

        Returns:
            Channel name
        """
        result = self.bridge.safe_execute(
            f'channels.getChannelName({channel_id})'
        )
        if result.get("success"):
            return str(result.get("data", f"Channel {channel_id}"))
        return f"Channel {channel_id}"

    def set_name(self, channel_id: int, name: str) -> bool:
        """
        Set the name of a channel.

        Args:
            channel_id: Channel index
            name: New channel name

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            f'channels.setChannelName({channel_id}, "{name}")'
        )
        return result.get("success", False)

    def get_color(self, channel_id: int) -> str:
        """
        Get the color of a channel.

        Args:
            channel_id: Channel index

        Returns:
            Color as hex string (e.g., "#FF5733")
        """
        result = self.bridge.safe_execute(
            f"channels.getChannelColor({channel_id})"
        )
        if result.get("success"):
            color_int = result.get("data", 0)
            # Convert integer color to hex
            return f"#{color_int:06X}"
        return "#000000"

    def set_color(self, channel_id: int, color_hex: str) -> bool:
        """
        Set the color of a channel.

        Args:
            channel_id: Channel index
            color_hex: Color as hex string (e.g., "#FF5733")

        Returns:
            True if successful
        """
        # Remove # if present and convert to int
        color_int = int(color_hex.lstrip("#"), 16)

        result = self.bridge.safe_execute(
            f"channels.setChannelColor({channel_id}, {color_int})"
        )
        return result.get("success", False)

    def select(self, channel_id: int) -> bool:
        """
        Select a channel.

        Args:
            channel_id: Channel index

        Returns:
            True if successful
        """
        result = self.bridge.safe_execute(
            f"channels.selectChannel({channel_id})"
        )
        return result.get("success", False)

    def get_selected(self) -> int:
        """
        Get the currently selected channel index.

        Returns:
            Selected channel index, or -1 if none selected
        """
        result = self.bridge.safe_execute(
            "channels.selectedChannel()"
        )
        if result.get("success"):
            return int(result.get("data", -1))
        return -1

    def get_all(self) -> List[Dict[str, Any]]:
        """
        Get information about all channels.

        Returns:
            List of channel information dictionaries
        """
        count = self.get_count()
        channels = []

        for i in range(count):
            channel_info = {
                "id": i,
                "name": self.get_name(i),
                "color": self.get_color(i),
                "selected": (i == self.get_selected()),
            }
            channels.append(channel_info)

        return channels

    def create_channel(self, name: str, color: str = None) -> Dict[str, Any]:
        """
        Create a new channel (if API supports it).

        Note: This may require alternative approaches as FL Studio's
        Python API has limited support for creating channels programmatically.

        Args:
            name: Channel name
            color: Optional color hex string

        Returns:
            Channel information dictionary
        """
        # This is a placeholder - actual implementation depends on FL API capabilities
        # In practice, you might need to duplicate an existing channel or use other methods
        raise NotImplementedError(
            "Creating channels programmatically is not directly supported. "
            "Consider duplicating existing channels or creating templates."
        )

    def set_piano_roll_note(
        self,
        channel_id: int,
        position: float,
        key: int,
        duration: float,
        velocity: int = 100
    ) -> bool:
        """
        Add a note to the piano roll.

        Args:
            channel_id: Channel index
            position: Position in beats
            key: MIDI key (0-127)
            duration: Duration in beats
            velocity: Note velocity (0-127)

        Returns:
            True if successful
        """
        # FL Studio API for adding notes
        result = self.bridge.safe_execute(
            f"channels.addNote({channel_id}, {position}, {key}, {duration}, {velocity})"
        )
        return result.get("success", False)

    def get_midi_channel(self, channel_id: int) -> int:
        """
        Get the MIDI channel number for a channel.

        Args:
            channel_id: Channel index

        Returns:
            MIDI channel number (0-15)
        """
        result = self.bridge.safe_execute(
            f"channels.getTargetFxTrack({channel_id})"
        )
        if result.get("success"):
            return int(result.get("data", 0))
        return 0
