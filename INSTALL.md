# Quick Installation Checklist

## 🚀 Get Started in 10 Minutes

### 1. Install Dependencies (2 minutes)
```bash
pip install fastmcp pydantic python-dotenv flapi
```

### 2. Install loopMIDI (Windows only, 2 minutes)
- Download: https://www.tobias-erichsen.de/software/loopmidi.html
- Create two ports: "Flapi Request" and "Flapi Response"

### 3. Install Flapi (1 minute)
```bash
flapi install
```

### 4. Configure FL Studio (3 minutes)
- Open FL Studio
- Options → MIDI Settings
- Link "Flapi Request" to input
- Link "Flapi Response" to output

### 5. Test Connection (1 minute)
```bash
python scripts/test_connection.py
```

### 6. Start Server (instant)
```bash
python -m fl_studio_mcp.fl_studio_server
```

## ✅ You're Ready!

Now you can control FL Studio with AI!

## Documentation
- [Quick Start](docs/QUICK_START.md) - General quick start
- [Windows Setup](docs/WINDOWS_SETUP.md) - Detailed Windows guide
- [Project Summary](PROJECT_SUMMARY.md) - What we built
- [README](README.md) - Main documentation

## Example Commands
```
"Connect to FL Studio"
"Get project info"
"Set tempo to 140 BPM"
"Create a C4 note"
"Start playback"
```

---

**Made with 🎵**
