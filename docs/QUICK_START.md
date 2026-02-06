# FL Studio MCP Server - Quick Start Guide

## Installation

### 1. Install Python Dependencies

```bash
# Install basic dependencies
pip install fastmcp pydantic python-dotenv

# Install with Flapi support (recommended)
pip install flapi

# Or install everything
pip install -e ".[flapi,dev]"
```

### 2. Install and Configure Flapi

Flapi is the bridge between Python and FL Studio.

```bash
# Install Flapi
pip install flapi

# Run the Flapi installer
flapi install
```

This will copy the Flapi server script to your FL Studio directory.

### 3. Set Up MIDI Ports (Windows Only)

**Windows users:**

1. Download and install [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html)
2. Open loopMIDI and create two ports:
   - `Flapi Request`
   - `Flapi Response`

**macOS users:**

MIDI ports are created automatically - no manual setup needed!

### 4. Configure FL Studio

1. Open FL Studio
2. Go to **Options → MIDI Settings**
3. Find the MIDI controller section
4. Link `Flapi Request` to the Flapi script
5. Link `Flapi Response` to the Flapi script
6. Assign unique port numbers to each

For detailed instructions, see [FLAPI_SETUP.md](FLAPI_SETUP.md).

### 5. Configure Environment Variables

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your settings
# Notably, update the FL Studio path if needed
```

## Testing the Connection

Run the test script to verify everything works:

```bash
python scripts/test_connection.py
```

You should see output like:

```
============================================================
FL Studio MCP Connection Test
============================================================

Test 1: Checking Flapi availability...
✓ Flapi is available

Test 2: Connecting to FL Studio...
✓ Connected to FL Studio successfully

Test 3: Getting connection status...
✓ Connection status: {...}

Test 4: Getting project information...
✓ Tempo: 120.0 BPM
✓ Channels: 10
✓ Mixer tracks: 20

...
```

## Starting the MCP Server

Once everything is configured, start the server:

```bash
python -m fl_studio_mcp.fl_studio_server
```

The server will start and listen for MCP commands via stdio.

## Configuring with Claude

To use this server with Claude (or another MCP client), add it to your MCP configuration:

**For Claude Desktop:**

1. Open Claude Desktop settings
2. Go to "MCP Servers"
3. Add a new server:

```json
{
  "mcpServers": {
    "fl-studio": {
      "command": "python",
      "args": ["-m", "fl_studio_mcp.fl_studio_server"],
      "cwd": "C:\\Users\\YourName\\Projects\\fl-studio-mcp"
    }
  }
}
```

**For command-line MCP clients:**

```bash
python -m fl_studio_mcp.fl_studio_server
```

## Example Usage

Once connected, you can use natural language to control FL Studio:

**Basic Commands:**

- "Connect to FL Studio"
- "Get project info"
- "Set tempo to 140 BPM"
- "Start playback"
- "Stop playback"
- "Get all channels"

**Creating Music:**

- "Create a C major melody"
- "Add a drum pattern"
- "Create a chord progression"
- "Add a bassline"

**Mixing:**

- "Set mixer track 1 volume to 0.7"
- "Get all mixer levels"
- "Pan track 2 to the left"

## Troubleshooting

### "Flapi not available"

**Solution:** Install Flapi:
```bash
pip install flapi
```

### "Failed to connect to FL Studio"

**Solutions:**
1. Make sure FL Studio is running
2. Run `flapi install` to install the Flapi script
3. Verify MIDI ports are configured correctly
4. Check that the Flapi script is loaded in FL Studio

### MIDI Port Issues (Windows)

**Solutions:**
1. Open loopMIDI and verify the ports exist
2. Restart FL Studio after creating ports
3. Make sure ports are linked in FL Studio MIDI settings

### Import Errors

**Solution:** Make sure you've installed the package in development mode:
```bash
pip install -e .
```

## Next Steps

- Read the [API Reference](API_REFERENCE.md) for all available tools
- Check out [Examples](EXAMPLES.md) for usage examples
- Review the [Installation Guide](INSTALLATION.md) for detailed setup

## Getting Help

- Open an issue on GitHub
- Check the documentation in the `docs/` folder
- Review the test script for usage examples

## System Requirements

- **Python:** 3.10 or higher
- **FL Studio:** 20.7+ (21.0+ recommended)
- **Operating System:** Windows 10+ or macOS 10.14+
- **MIDI:** loopMIDI (Windows only, macOS automatic)

---

**Ready to make music with AI?** Let's go! 🎵
