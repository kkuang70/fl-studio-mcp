# Windows Setup Guide for FL Studio MCP

## Step-by-Step Windows Installation

This guide will walk you through setting up the FL Studio MCP server on Windows.

---

## Prerequisites

- **Windows 10 or 11**
- **FL Studio 20.7+** (21.0+ recommended)
- **Python 3.10 or higher**
- **Administrator privileges** (for MIDI port setup)

---

## Step 1: Install Python Dependencies

Open **Command Prompt** or **PowerShell**:

```bash
# Navigate to your project directory
cd C:\Users\YourName\Projects\fl-studio-mcp

# Install dependencies
pip install fastmcp pydantic python-dotenv flapi

# Verify installation
pip list | grep -E "fastmcp|flapi|pydantic"
```

---

## Step 2: Install loopMIDI

### Download and Install

1. Download loopMIDI: https://www.tobias-erichsen.de/software/loopmidi.html
2. Run the installer
3. During installation, you can choose to start loopMIDI automatically

### Create Virtual MIDI Ports

1. Open **loopMIDI** (search in Start menu)
2. Click the "+" button to create a new port
3. Name it: `Flapi Request`
4. Click "+" again
5. Name it: `Flapi Response`

You should now see two ports in the loopMIDI window:

```
loopMIDI
├── Flapi Request
└── Flapi Response
```

**Tip:** Leave loopMIDI running in the background while using FL Studio.

---

## Step 3: Install Flapi Script in FL Studio

### Run the Flapi Installer

```bash
# In your project directory
flapi install
```

This will:
- Locate your FL Studio installation
- Copy the Flapi server script to the correct location
- Register the script with FL Studio

If successful, you should see:
```
Flapi has been installed successfully!
```

---

## Step 4: Configure FL Studio MIDI Settings

### Open MIDI Settings

1. Open **FL Studio**
2. Go to **Options → MIDI Settings** (or press `F10`)
3. You'll see the MIDI settings window

### Link Flapi Request Port

1. Find the "Input" section on the left
2. Look for **Flapi Request**
3. Click on it to select
4. In the "Controller type" dropdown, select **Flapi - Request** (or similar)
5. Note the **Port number** shown (e.g., "Port 1")

### Link Flapi Response Port

1. Find the "Output" section on the left
2. Look for **Flapi Response**
3. Click on it to select
4. In the "Port" number, select a different port (e.g., "Port 2")

### Verify MIDI Link

In the MIDI settings window, you should see:
- **Flapi Request** linked to an input port
- **Flapi Response** linked to an output port
- Both ports show as active/enabled

**Close the MIDI settings window.**

---

## Step 5: Configure Environment Variables

### Create .env File

```bash
# In your project directory
copy .env.example .env
```

### Edit .env File

Open `.env` in a text editor and update:

```bash
# FL Studio Configuration
FL_STUDIO_USER_DATA_PATH="C:\\Users\\YourName\\Documents\\Image-Line\\FL Studio"

# Flapi Configuration (should match loopMIDI port names)
FLAPI_REQUEST_PORT="Flapi Request"
FLAPI_RESPONSE_PORT="Flapi Response"

# MCP Configuration
MCP_LOG_LEVEL="INFO"
FL_AUTO_CONNECT="false"
```

**Important:** Use double backslashes `\\` for Windows paths!

---

## Step 6: Test the Connection

### Run the Test Script

```bash
python scripts\test_connection.py
```

### Expected Output

```
============================================================
FL Studio MCP Connection Test
============================================================

Test 1: Checking Flapi availability...
✓ Flapi is available

Test 2: Connecting to FL Studio...
✓ Connected to FL Studio successfully

Test 3: Getting connection status...
✓ Connection status: {'connected': True, ...}

Test 4: Getting project information...
✓ Tempo: 120.0 BPM
✓ Channels: 10
✓ Mixer tracks: 125

Test 5: Getting channel information...
✓ Found 10 channels:
  - Channel 1 (ID: 0)
  - Channel 2 (ID: 1)
  ...

Test 6: Getting transport status...
✓ Playing: False
✓ Recording: False
✓ Position: 0.0 beats

Test 7: Getting mixer levels...
✓ Found 125 mixer tracks:
  - Master: Vol=0.80, Pan=0.00
  ...

Test 8: Health check...
✓ Connection is healthy

Disconnecting...
✓ Disconnected

============================================================
All tests completed!
============================================================
```

### Troubleshooting Common Issues

#### "Flapi not available"
```bash
pip install flapi
```

#### "Failed to connect to FL Studio"
- Make sure FL Studio is running
- Make sure loopMIDI is running
- Check MIDI port names in .env match loopMIDI exactly
- Verify Flapi script is loaded in FL Studio

#### "MIDI port not found"
- Verify loopMIDI ports are created
- Restart FL Studio after creating ports
- Check port names match exactly (case-sensitive)

---

## Step 7: Start the MCP Server

### Manual Start

```bash
python -m fl_studio_mcp.fl_studio_server
```

The server will start and wait for MCP commands via stdio.

### Verify Server is Running

You should see:
```
INFO - Starting FL Studio MCP Server...
```

The server is now ready to accept commands!

---

## Step 8: Configure with Claude (Optional)

If using Claude Desktop:

1. Open Claude Desktop
2. Click **Settings** (gear icon)
3. Go to **MCP Servers**
4. Add a new server:

```json
{
  "mcpServers": {
    "fl-studio": {
      "command": "python",
      "args": ["-m", "fl_studio_mcp.fl_studio_server"],
      "cwd": "C:\\Users\\YourName\\Projects\\fl-studio-mcp",
      "env": {
        "FLAPI_REQUEST_PORT": "Flapi Request",
        "FLAPI_RESPONSE_PORT": "Flapi Response"
      }
    }
  }
}
```

5. Restart Claude Desktop

---

## Quick Verification

Once the server is running, test it with Claude:

```
You: Connect to FL Studio
Claude: [Calls connect_to_fl_studio()]
✓ Successfully connected!

You: Get project info
Claude: [Calls get_project_info()]
✓ Tempo: 120 BPM, Channels: 10, etc.
```

---

## Windows-Specific Tips

### Run loopMIDI at Startup

1. Press `Win + R`
2. Type `shell:startup`
3. Create a shortcut to loopMIDI
4. Now it will start automatically with Windows

### Firewall Warning

If Windows Firewall shows a warning:
- Click "Allow access"
- This is needed for MIDI communication

### FL Studio Path

Your FL Studio data path is typically:
```
C:\Users\YourName\Documents\Image-Line\FL Studio
```

If you installed it elsewhere, update the `.env` file.

---

## Common Windows Issues

### Issue: "Python command not found"

**Solution:**
1. Reinstall Python
2. Check "Add Python to PATH" during installation
3. Restart Command Prompt

### Issue: "pip not recognized"

**Solution:**
```bash
python -m pip install fastmcp pydantic python-dotenv flapi
```

### Issue: MIDI ports disappear

**Solution:**
1. Close FL Studio
2. Restart loopMIDI
3. Recreate the ports if needed
4. Restart FL Studio

### Issue: Flapi script not showing in FL Studio

**Solution:**
```bash
# Reinstall Flapi
flapi install --force

# Or manually copy the script to:
# C:\Users\YourName\Documents\Image-Line\FL Studio\Actions\Scripting\
```

---

## Success Checklist

- [ ] Python 3.10+ installed
- [ ] Dependencies installed (`fastmcp`, `flapi`, etc.)
- [ ] loopMIDI installed and running
- [ ] Virtual MIDI ports created ("Flapi Request", "Flapi Response")
- [ ] Flapi script installed (`flapi install`)
- [ ] FL Studio MIDI settings configured
- [ ] .env file created and configured
- [ ] Test script runs successfully
- [ ] MCP server starts without errors

---

## Next Steps

Once everything is working:

1. **Test basic commands** - Connect, get info, set tempo
2. **Create music** - Add notes, create patterns
3. **Explore the API** - Check out all available tools
4. **Build automation** - Create workflows with AI

For more information, see:
- [QUICK_START.md](QUICK_START.md)
- [API_REFERENCE.md](API_REFERENCE.md) (coming soon)
- [EXAMPLES.md](EXAMPLES.md) (coming soon)

---

## Getting Help

If you're stuck:

1. Check the test script output for errors
2. Review the troubleshooting sections above
3. Open an issue on GitHub with:
   - Windows version
   - FL Studio version
   - Error messages
   - Test script output

---

**Happy music making with AI!** 🎵🤖
