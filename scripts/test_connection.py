"""
Test script for FL Studio MCP connection.

This script tests the connection to FL Studio and verifies basic functionality.
"""

import sys
import logging

# Add parent directory to path for imports
sys.path.insert(0, ".")

from fl_studio_mcp.core.bridge import get_bridge, FLStudioBridge
from fl_studio_mcp.core.connection import ConnectionManager
from fl_studio_mcp.api.transport import TransportAPI
from fl_studio_mcp.api.channels import ChannelAPI
from fl_studio_mcp.api.mixer import MixerAPI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def test_connection():
    """Test connection to FL Studio."""
    print("=" * 60)
    print("FL Studio MCP Connection Test")
    print("=" * 60)
    print()

    # Initialize bridge and APIs
    bridge = get_bridge()
    connection_manager = ConnectionManager(bridge)
    transport_api = TransportAPI(bridge)
    channel_api = ChannelAPI(bridge)
    mixer_api = MixerAPI(bridge)

    # Test 1: Check Flapi availability
    print("Test 1: Checking Flapi availability...")
    try:
        bridge._ensure_flapi()
        print("✓ Flapi is available")
    except Exception as e:
        print(f"✗ Flapi not available: {e}")
        print()
        print("Please install Flapi: pip install flapi")
        return False
    print()

    # Test 2: Connect to FL Studio
    print("Test 2: Connecting to FL Studio...")
    print("Make sure FL Studio is running and Flapi script is loaded.")
    try:
        success = connection_manager.connect()
        if success:
            print("✓ Connected to FL Studio successfully")
        else:
            print("✗ Failed to connect to FL Studio")
            return False
    except Exception as e:
        print(f"✗ Connection error: {e}")
        print()
        print("Troubleshooting:")
        print("1. Make sure FL Studio is running")
        print("2. Run 'flapi install' to install the Flapi script")
        print("3. Configure MIDI ports in FL Studio")
        return False
    print()

    # Test 3: Get connection status
    print("Test 3: Getting connection status...")
    try:
        status = connection_manager.get_connection_status()
        print(f"✓ Connection status: {status}")
    except Exception as e:
        print(f"✗ Error getting status: {e}")
    print()

    # Test 4: Get project info
    print("Test 4: Getting project information...")
    try:
        tempo = transport_api.get_tempo()
        channel_count = channel_api.get_count()
        mixer_count = mixer_api.get_track_count()

        print(f"✓ Tempo: {tempo} BPM")
        print(f"✓ Channels: {channel_count}")
        print(f"✓ Mixer tracks: {mixer_count}")
    except Exception as e:
        print(f"✗ Error getting project info: {e}")
    print()

    # Test 5: Get channels
    print("Test 5: Getting channel information...")
    try:
        channels = channel_api.get_all()
        print(f"✓ Found {len(channels)} channels:")
        for channel in channels[:5]:  # Show first 5
            print(f"  - {channel['name']} (ID: {channel['id']})")
        if len(channels) > 5:
            print(f"  ... and {len(channels) - 5} more")
    except Exception as e:
        print(f"✗ Error getting channels: {e}")
    print()

    # Test 6: Get transport status
    print("Test 6: Getting transport status...")
    try:
        status = transport_api.get_status()
        print(f"✓ Playing: {status['playing']}")
        print(f"✓ Recording: {status['recording']}")
        print(f"✓ Position: {status['position_beats']} beats")
    except Exception as e:
        print(f"✗ Error getting transport status: {e}")
    print()

    # Test 7: Get mixer levels
    print("Test 7: Getting mixer levels...")
    try:
        levels = mixer_api.get_all_levels()
        print(f"✓ Found {len(levels)} mixer tracks:")
        for track in levels[:3]:  # Show first 3
            print(f"  - {track['name']}: Vol={track['volume']:.2f}, Pan={track['pan']:.2f}")
        if len(levels) > 3:
            print(f"  ... and {len(levels) - 3} more")
    except Exception as e:
        print(f"✗ Error getting mixer levels: {e}")
    print()

    # Test 8: Health check
    print("Test 8: Health check...")
    try:
        healthy = connection_manager.health_check()
        if healthy:
            print("✓ Connection is healthy")
        else:
            print("✗ Connection health check failed")
    except Exception as e:
        print(f"✗ Health check error: {e}")
    print()

    # Disconnect
    print("Disconnecting...")
    connection_manager.disconnect()
    print("✓ Disconnected")
    print()

    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)
    return True


if __name__ == "__main__":
    try:
        success = test_connection()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)
