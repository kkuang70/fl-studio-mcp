# FL Studio MCP - Prompting Guide

This guide shows you how to control FL Studio using natural language prompts with Claude and the FL Studio MCP server.

---

## 🚀 Getting Started

### Prerequisites
- ✅ FL Studio running
- ✅ loopMIDI running with ports created
- ✅ MCP server configured in Claude Desktop
- ✅ Flapi script installed in FL Studio

### First Connection

Start by connecting to FL Studio:

```
"Connect to FL Studio"
```

You should see a success message confirming the connection.

---

## 🎵 Basic Commands

### Project Information

**Get current project info:**
```
"Get project information"
"What's the current tempo?"
"How many channels do I have?"
"Show me all mixer levels"
```

**Tempo control:**
```
"Set the tempo to 140 BPM"
"Change tempo to 85 for a lo-fi beat"
"Speed it up to 174 BPM (drum and bass)"
```

### Transport Control

**Playback:**
```
"Start playback"
"Stop the music"
"Pause playback"
```

**Status:**
```
"Is FL Studio playing?"
"What's the current position?"
"Show me transport status"
```

---

## 🎹 Creating Music

### Creating Melodies

**Simple melodies:**
```
"Create a C major scale melody"
"Add a melody in A minor with 8 notes"
"Create a simple arpeggio pattern"
```

**Specific melodies:**
```
"Create a melody: C, E, G, C (one octave up), G, E, C"
"Add a bassline following the root notes"
"Create a jazzy melody with some chromatic notes"
```

**Note parameters:**
```
"Create a C4 note at beat 0, duration 1 beat"
"Add a sharp staccato note at position 2.5"
"Create a long held note (4 beats) starting at beat 4"
```

### Working with Channels

**Channel management:**
```
"Create a new channel for piano"
"Add a synth channel"
"Show me all channels"
"Select channel 3"
```

**Instruments:**
```
"Create a drum channel"
"Add a bass guitar channel"
"Create a strings channel"
```

### Creating Patterns

**Basic patterns:**
```
"Create a new 4-bar pattern"
"Make a 16-beat drum pattern"
"Create an 8-bar melody pattern"
```

**Named patterns:**
```
"Create a pattern called 'Verse'"
"Add a chorus pattern"
"Make a bridge pattern"
```

---

## 🥁 Drums & Rhythm

### Drum Patterns

**Basic beats:**
```
"Create a basic rock drum beat"
"Add a hip-hop drum pattern"
"Make a house music beat"
"Create a trap beat"
```

**Specific elements:**
```
"Add a kick drum on beats 1 and 3"
"Put a snare on beats 2 and 4"
"Add hi-hats on every offbeat"
"Create a syncopated drum pattern"
```

**Advanced rhythms:**
```
"Add a drum fill in bar 4"
"Create a broken beat pattern"
"Make a polyrhythmic percussion pattern"
```

---

## 🎼 Chords & Harmony

### Chord Progressions

**Basic progressions:**
```
"Create a I-IV-V-I chord progression in C major"
"Add a ii-V-I progression in jazz style"
"Make a four-chord progression: C, G, Am, F"
```

**Advanced harmony:**
```
"Add a 7th chord progression"
"Create a jazz ii-V-I with extensions"
"Add a suspended chord resolution"
```

**Inversions:**
```
"Use first inversion for these chords"
"Add a chord progression with smooth voice leading"
```

### Scales & Modes

**Scale-based melodies:**
```
"Create a melody using the C major scale"
"Make a solo using A minor pentatonic"
"Add a Dorian mode melody"
"Create a blues scale solo"
```

**Musical modes:**
```
"Use Phrygian mode for this melody"
"Create a Lydian melody"
"Add a Mixolydian scale run"
```

---

## 🎚️ Mixing & Effects

### Mixer Control

**Level adjustments:**
```
"Set mixer track 1 to 0.8"
"Turn up the bass channel"
"Lower the volume of track 3"
"Set all levels to a good starting point"
```

**Stereo panning:**
```
"Pan the guitars to the left"
"Center the bass"
"Create a stereo spread for the pads"
```

**Balance:**
```
"Balance the mix properly"
"Make the kick drum punch through"
"Create space for the vocals"
```

### Effects & Automation (Future)

**Note:** These features will be available in Phase 4

```
"Add reverb to the snare"
"Put a delay on the lead synth"
"Automate the filter cutoff"
"Create a sidechain compression effect"
```

---

## 🎛️ Workflow Automation

### Project Setup

**Quick setup:**
```
"Set up a project for a 120 BPM house track"
"Create a lo-fi beat template at 85 BPM"
"Set up for a 174 BPM drum and bass track"
```

**Channel organization:**
```
"Create channels for: kick, snare, hi-hat, bass, lead"
"Set up a full rock band arrangement"
"Make channels for a string section"
```

### Arrangement

**Basic structure:**
```
"Create a verse-chorus arrangement"
"Set up a 32-bar song structure"
"Add an intro and outro"
```

**Advanced:**
```
"Arrange the patterns for a full song"
"Create a dynamic build-up"
"Add a breakdown section"
```

---

## 🎨 Style & Genre

### Electronic Music

**House:**
```
"Create a house music beat at 124 BPM"
"Add a classic house chord stab"
"Make a filter sweep build-up"
```

**Techno:**
```
"Create a techno loop at 130 BPM"
"Add industrial percussion"
"Make a repetitive synth motif"
```

**EDM/Dubstep:**
```
"Create a dubstep wobble bass riff"
"Make a massive drop section"
"Add risers and falls"
```

### Hip-Hop & R&B

**Beats:**
```
"Create a boom-bap drum beat"
"Add a trap beat with rolling hi-hats"
"Make a chilled lo-fi hip-hop beat"
```

**Melodies:**
```
"Add a soulful chord progression"
"Create a melodic trap lead"
"Make a smooth R&B pad"
```

### Rock & Pop

**Instruments:**
```
"Create a power chord progression"
"Add a bass guitar line"
"Make a lead guitar melody"
```

**Arrangement:**
```
"Set up verse-chorus-verse-chorus-bridge-chorus"
"Add a guitar solo section"
"Create a dynamic arrangement"
```

### Jazz & Classical

**Jazz:**
```
"Create a ii-V-I progression in F major"
"Add a walking bass line"
"Make a bebop-style melody"
```

**Classical:**
```
"Create a counterpoint melody"
"Add a classical chord progression"
"Make a fugue-like pattern"
```

---

## 📝 Advanced Prompting Tips

### Be Specific

**Good:**
```
"Create a C major melody with 8 notes starting at C4, using quarter notes, each note lasting 1 beat"
```

**Less effective:**
```
"Make a melody"
```

### Use Musical Terminology

**Instead of:**
```
"Make it sound higher"
```

**Try:**
```
"Transpose the melody up an octave"
"Add notes in the higher register"
```

### Break Down Complex Tasks

**Complex:**
```
"Create a full song"
```

**Better:**
```
"Step 1: Create a 4-chord progression (C-G-Am-F)
Step 2: Add a bassline following root notes
Step 3: Create a drum beat with kick on 1 and 3, snare on 2 and 4
Step 4: Add a simple melody using the pentatonic scale"
```

### Reference Specific Parameters

**Examples:**
```
"Create a note at channel 1, position 0.0, key 60 (C4), duration 1.0, velocity 100"
"Set mixer track 1 volume to 0.75"
"Create a pattern with length 16 beats"
```

---

## 🎯 Common Workflows

### Workflow 1: Quick Beat Creation

```
1. "Connect to FL Studio"
2. "Set tempo to 140 BPM"
3. "Create a drum channel"
4. "Create a kick drum on beats 1, 2, 3, 4"
5. "Add a snare on beats 2 and 4"
6. "Add hi-hats on offbeats"
7. "Start playback to test"
```

### Workflow 2: Melody Creation

```
1. "Connect to FL Studio"
2. "Get project info"
3. "Create a synth channel"
4. "Create a melody using C major scale: C, D, E, F, G, A, B, C"
5. "Vary the note durations for interest"
6. "Start playback and adjust as needed"
```

### Workflow 3: Full Track Setup

```
1. "Connect to FL Studio"
2. "Set tempo to 124 BPM"
3. "Create channels: kick, snare, hi-hat, bass, lead, pad"
4. "Create a 4-chord progression"
5. "Add drums in a house pattern"
6. "Create a bassline following root notes"
7. "Add a lead melody"
8. "Create a verse-chorus arrangement"
```

---

## 🔧 Troubleshooting Prompts

### Connection Issues

```
"Are you connected to FL Studio?"
"Get connection status"
"Check the health of the connection"
```

### Understanding Current State

```
"What's in my project right now?"
"Show me all channels"
"Get current project info"
"What's the tempo and key?"
```

### Debugging

```
"List all created notes"
"Show me mixer levels"
"What's on the playlist?"
```

---

## 💡 Pro Tips

1. **Start Simple** - Begin with basic commands before attempting complex arrangements
2. **Iterate** - Build up music piece by piece, adjusting as you go
3. **Listen First** - Use transport commands to playback and hear what you're creating
4. **Experiment** - Try different scales, chords, and rhythms
5. **Save Often** - Remember to save your project (when feature is available)

---

## 🎓 Learning Examples

### Example 1: First Melody

```
"Let's create a simple melody:
1. Create a new channel called 'Melody'
2. Set tempo to 120 BPM
3. Add these notes in C major:
   - C4 at beat 0, duration 1
   - D4 at beat 1, duration 1
   - E4 at beat 2, duration 1
   - F4 at beat 3, duration 1
   - G4 at beat 4, duration 2
4. Start playback so I can hear it"
```

### Example 2: Drum Beat

```
"Create a basic drum beat:
1. Create a drum channel
2. Add kick on beats 1, 2, 3, 4
3. Add snare on beats 2 and 4
4. Add hi-hat on every 0.5 beat
5. Set tempo to 100 BPM
6. Start playback"
```

### Example 3: Chord Progression

```
"Create a chord progression:
1. Create 4 channels for the chords
2. Add these chords (C major):
   - Channel 1: C-E-G (C major)
   - Channel 2: G-B-D (G major)
   - Channel 3: A-C-E (A minor)
   - Channel 4: F-A-C (F major)
3. Make each chord last 4 beats
4. Create a 16-bar progression"
```

---

## 🚧 Coming Soon (Future Phases)

These features will be available in future updates:

- **Note reading**: "Show me all notes in channel 1"
- **Note editing**: "Change the note at position 2 to D4"
- **Pattern management**: "Duplicate this pattern"
- **Playlist arrangement**: "Add pattern 1 to the playlist"
- **Audio export**: "Export to WAV file"
- **Plugin control**: "Change the filter cutoff"
- **Automation**: "Automate the volume"
- **FX chains**: "Add reverb to this channel"

---

## 🎮 Quick Reference

### Essential Commands

| Task | Prompt |
|------|--------|
| Connect | "Connect to FL Studio" |
| Start | "Start playback" |
| Stop | "Stop playback" |
| Tempo | "Set tempo to X BPM" |
| Info | "Get project info" |
| Channels | "Show all channels" |
| Mixer | "Get mixer levels" |

### Note Creation Formula

```
"Create a note:
- Channel: [number]
- Position: [beat number]
- Key: [0-127, where 60 = C4]
- Duration: [beats]
- Velocity: [0-127, default 100]"
```

---

## 🎵 Happy Music Making!

Experiment with these prompts and discover what's possible. The more you use the FL Studio MCP server, the more you'll discover creative ways to make music with AI!

**Need more examples?** Check out the [EXAMPLES.md](EXAMPLES.md) file for complete walkthroughs.

**Questions?** Open an issue on GitHub or check the documentation.

---

**Made with 🎵 for AI-powered music production**
