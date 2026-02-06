# FL Studio MCP Server

An **MCP (Model Context Protocol) server** for FL Studio that enables AI (like Claude) to directly control FL Studio for music generation, instrument manipulation, and project automation.

## Features

- 🎵 **Music Generation**: Create melodies, chords, and beats with AI
- 🎛️ **Transport Control**: Play, stop, record, and navigate projects
- 🎚️ **Mixer Control**: Adjust levels, pans, and routing
- 🎼 **Pattern & Playlist**: Arrange and organize your music
- 🔌 **Plugin Automation**: Control any plugin parameter
- 📤 **Export**: Render projects to audio files

## How It Works

```
AI (Claude) → MCP Server → Flapi Bridge → MIDI → FL Studio
```

The server uses:
- **FastMCP** for MCP protocol implementation
- **Flapi** for remote communication with FL Studio
- **FL Studio MIDI Scripting API** for DAW control

## Installation

### Prerequisites

1. **FL Studio 20.7+** (or FL Studio 2025 recommended)
2. **Python 3.10+**
3. **loopMIDI** (Windows only) - [Download here](https://www.tobias-erichsen.de/software/loopmidi.html)

### Step 1: Install this package

We recommend using [uv](https://github.com/astral-sh/uv) for fast package management:

```bash
# Clone the repository
git clone https://github.com/yourusername/fl-studio-mcp.git
cd fl-studio-mcp

# Install with uv (recommended - 10-100x faster than pip!)
uv sync

# Or install with Flapi support
uv sync --extra flapi

# Or install with all optional dependencies
uv sync --all-extras
```

**If you prefer pip:**

```bash
# Install with basic dependencies
pip install -e .

# Or install with Flapi support (recommended)
pip install -e ".[flapi]"

# Or install with all optional dependencies
pip install -e ".[flapi,pyflp,dev]"
```

### Step 2: Install and Configure Flapi

```bash
# Install Flapi (with uv)
uv pip install flapi

# Or with pip
pip install flapi

# Run the Flapi installer
flapi install

# This will copy the Flapi server script to your FL Studio directory
```

### Step 3: Set Up MIDI Ports (Windows)

1. Open **loopMIDI** and create two ports:
   - `Flapi Request`
   - `Flapi Response`

2. In FL Studio, go to **Options → MIDI Settings**
3. Link the MIDI ports to the Flapi script (see detailed docs)

**macOS**: MIDI ports are created automatically - no manual setup needed!

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```bash
# FL Studio Configuration
FL_STUDIO_USER_DATA_PATH="C:\Users\YourName\Documents\Image-Line\FL Studio"

# Flapi Configuration
FLAPI_REQUEST_PORT="Flapi Request"
FLAPI_RESPONSE_PORT="Flapi Response"

# MCP Configuration
MCP_LOG_LEVEL="INFO"
```

## Usage

### Starting the Server

```bash
# With uv (recommended)
uv run python -m fl_studio_mcp.fl_studio_server

# Or directly with python
python -m fl_studio_mcp.fl_studio_server
```

### Configuring with Claude

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "fl-studio": {
      "command": "python",
      "args": ["-m", "fl_studio_mcp.fl_studio_server"]
    }
  }
}
```

### Example Prompts

Once connected, you can use natural language to control FL Studio:

- "Create a C major melody with 8 notes"
- "Set the tempo to 120 BPM"
- "Add a drum channel with a kick pattern"
- "Export the project to WAV"
- "Create a lo-fi beat at 85 BPM"

## Available Tools

### Transport Control
- `transport_start()` - Start playback
- `transport_stop()` - Stop playback
- `get_transport_status()` - Get current state

### Project Management
- `get_project_info()` - Get project details (tempo, key, etc.)
- `set_tempo(bpm)` - Change project tempo
- `save_project(path)` - Save project

### Music Generation
- `create_channel(name, color)` - Create new instrument track
- `create_note(channel_id, position, key, duration, velocity)` - Add MIDI note
- `create_pattern(name, length)` - Create new pattern
- `get_channels()` - List all channels

### Mixer
- `set_mixer_fader(track_id, volume)` - Adjust volume
- `get_mixer_levels()` - Get all mixer levels
- `link_channel_to_mixer(channel_id, mixer_track_id)` - Route audio

### Export
- `export_audio(format, path, quality)` - Render to audio file

## Project Structure

```
fl-studio-mcp/
├── fl_studio_mcp/
│   ├── fl_studio_server.py    # Main MCP server
│   ├── core/                   # Bridge & connection
│   ├── tools/                  # MCP tool implementations
│   ├── api/                    # FL Studio API wrappers
│   └── utils/                  # Utilities
├── scripts/                    # Helper scripts
├── docs/                       # Documentation
└── tests/                      # Tests
```

## Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [Flapi Setup](docs/FLAPI_SETUP.md)
- [API Reference](docs/API_REFERENCE.md)
- [Examples](docs/EXAMPLES.md)

## Development

### Running Tests

```bash
# With uv (recommended)
uv run pytest

# Or directly
pytest
```

### Code Formatting

```bash
# With uv
uv run black fl_studio_mcp/
uv run ruff check fl_studio_mcp/

# Or directly
black fl_studio_mcp/
ruff check fl_studio_mcp/
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- [FastMCP](https://gofastmcp.com/) - MCP server framework
- [Flapi](https://github.com/MaddyGuthridge/Flapi) - FL Studio remote control
- [FL Studio](https://www.image-line.com/) - The DAW
- [IL-Group/FL-Studio-API-Stubs](https://github.com/IL-Group/FL-Studio-API-Stubs) - API documentation

## Status

🚧 **This project is under active development**

Currently implementing Phase 1 (MVP Foundation). See [todo.md](todo.md) for progress.

---

**Made with 🎵 for AI-powered music production**
