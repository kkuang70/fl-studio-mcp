"""
MIDI utility functions for FL Studio MCP server.

Provides helper functions for MIDI note conversions, frequencies, etc.
"""

from typing import Dict, List, Tuple, Union


# MIDI note names to note number mapping
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def note_to_number(note: str, octave: int) -> int:
    """
    Convert note name and octave to MIDI note number.

    Args:
        note: Note name (e.g., "C", "C#", "Db")
        octave: Octave number (e.g., 4 for middle C)

    Returns:
        MIDI note number (0-127)

    Raises:
        ValueError: If note name is invalid

    Examples:
        >>> note_to_number("C", 4)
        60
        >>> note_to_number("A", 4)
        69
    """
    # Handle flat notes (convert to sharp)
    note = note.replace("Db", "C#")
    note = note.replace("Eb", "D#")
    note = note.replace("Gb", "F#")
    note = note.replace("Ab", "G#")
    note = note.replace("Bb", "A#")

    try:
        note_index = NOTE_NAMES.index(note)
    except ValueError:
        raise ValueError(
            f"Invalid note name: '{note}'. Must be one of {NOTE_NAMES}"
        )

    midi_number = note_index + (octave + 1) * 12

    if not (0 <= midi_number <= 127):
        raise ValueError(
            f"MIDI note number {midi_number} out of range (0-127). "
            f"Note: {note}{octave}"
        )

    return midi_number


def number_to_note(midi_number: int) -> str:
    """
    Convert MIDI note number to note name with octave.

    Args:
        midi_number: MIDI note number (0-127)

    Returns:
        Note name with octave (e.g., "C4", "A#5")

    Raises:
        ValueError: If MIDI number is out of range

    Examples:
        >>> number_to_note(60)
        'C4'
        >>> number_to_note(69)
        'A4'
    """
    if not (0 <= midi_number <= 127):
        raise ValueError(f"MIDI number must be 0-127, got {midi_number}")

    note_index = midi_number % 12
    octave = (midi_number // 12) - 1

    return f"{NOTE_NAMES[note_index]}{octave}"


def parse_note_string(note_str: str) -> int:
    """
    Parse note string to MIDI note number.

    Supports formats like "C4", "A#5", "Db3", etc.

    Args:
        note_str: Note string (e.g., "C4", "A#5", "Db3")

    Returns:
        MIDI note number

    Raises:
        ValueError: If note string is invalid

    Examples:
        >>> parse_note_string("C4")
        60
        >>> parse_note_string("A#5")
        82
    """
    note_str = note_str.strip()

    # Find where the octave number starts
    i = 0
    while i < len(note_str) and not note_str[i].isdigit():
        i += 1

    if i == 0 or i == len(note_str):
        raise ValueError(
            f"Invalid note format: '{note_str}'. Expected format like 'C4' or 'A#5'"
        )

    note_name = note_str[:i]
    octave = int(note_str[i:])

    return note_to_number(note_name, octave)


def midi_to_frequency(midi_number: int) -> float:
    """
    Convert MIDI note number to frequency in Hz.

    Uses the formula: f = 440 * 2^((n-69)/12)
    where n is the MIDI note number and 69 is A4.

    Args:
        midi_number: MIDI note number (0-127)

    Returns:
        Frequency in Hz

    Examples:
        >>> midi_to_frequency(69)  # A4
        440.0
        >>> midi_to_frequency(60)  # C4 (middle C)
        261.6255653005986
    """
    if not (0 <= midi_number <= 127):
        raise ValueError(f"MIDI number must be 0-127, got {midi_number}")

    return 440.0 * (2.0 ** ((midi_number - 69) / 12.0))


def frequency_to_midi(frequency: float) -> int:
    """
    Convert frequency in Hz to nearest MIDI note number.

    Uses the formula: n = 12 * log2(f/440) + 69

    Args:
        frequency: Frequency in Hz

    Returns:
        Nearest MIDI note number

    Examples:
        >>> frequency_to_midi(440.0)
        69
        >>> frequency_to_midi(261.63)
        60
    """
    import math

    if frequency <= 0:
        raise ValueError(f"Frequency must be positive, got {frequency}")

    midi_number = round(12 * math.log2(frequency / 440.0) + 69)

    # Clamp to valid range
    return max(0, min(127, midi_number))


def get_scale_notes(root: str, scale_type: str = "major") -> List[int]:
    """
    Get MIDI note numbers for a scale.

    Args:
        root: Root note (e.g., "C4", "A#3")
        scale_type: Type of scale ("major", "minor", "pentatonic_major", etc.)

    Returns:
        List of MIDI note numbers in the scale

    Examples:
        >>> get_scale_notes("C4", "major")
        [60, 62, 64, 65, 67, 69, 71]  # C major scale
    """
    # Scale intervals (semitones from root)
    SCALES = {
        "major": [0, 2, 4, 5, 7, 9, 11],
        "minor": [0, 2, 3, 5, 7, 8, 10],
        "pentatonic_major": [0, 2, 4, 7, 9],
        "pentatonic_minor": [0, 3, 5, 7, 10],
        "blues": [0, 3, 5, 6, 7, 10],
        "chromatic": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    }

    scale_type = scale_type.lower().replace(" ", "_")

    if scale_type not in SCALES:
        raise ValueError(
            f"Unknown scale type: '{scale_type}'. "
            f"Available: {list(SCALES.keys())}"
        )

    intervals = SCALES[scale_type]
    root_midi = parse_note_string(root)

    return [root_midi + interval for interval in intervals]


def get_chord_notes(root: str, chord_type: str = "major") -> List[int]:
    """
    Get MIDI note numbers for a chord.

    Args:
        root: Root note (e.g., "C4", "A#3")
        chord_type: Type of chord ("major", "minor", "diminished", etc.)

    Returns:
        List of MIDI note numbers in the chord

    Examples:
        >>> get_chord_notes("C4", "major")
        [60, 64, 67]  # C major chord (C-E-G)
        >>> get_chord_notes("C4", "minor")
        [60, 63, 67]  # C minor chord (C-Eb-G)
    """
    # Chord intervals (semitones from root)
    CHORDS = {
        "major": [0, 4, 7],
        "minor": [0, 3, 7],
        "diminished": [0, 3, 6],
        "augmented": [0, 4, 8],
        "major_7th": [0, 4, 7, 11],
        "minor_7th": [0, 3, 7, 10],
        "dominant_7th": [0, 4, 7, 10],
        "sus2": [0, 2, 7],
        "sus4": [0, 5, 7],
    }

    chord_type = chord_type.lower().replace(" ", "_")

    if chord_type not in CHORDS:
        raise ValueError(
            f"Unknown chord type: '{chord_type}'. "
            f"Available: {list(CHORDS.keys())}"
        )

    intervals = CHORDS[chord_type]
    root_midi = parse_note_string(root)

    return [root_midi + interval for interval in intervals]


def velocity_to_string(velocity: int) -> str:
    """
    Convert MIDI velocity to dynamic marking.

    Args:
        velocity: MIDI velocity (0-127)

    Returns:
        Dynamic marking string

    Examples:
        >>> velocity_to_string(20)
        'pp'
        >>> velocity_to_string(100)
        'mf'
    """
    if velocity < 20:
        return "pp"
    elif velocity < 40:
        return "p"
    elif velocity < 60:
        return "mp"
    elif velocity < 80:
        return "mf"
    elif velocity < 100:
        return "f"
    else:
        return "ff"


def validate_velocity(velocity: int) -> int:
    """
    Validate and clamp MIDI velocity.

    Args:
        velocity: Velocity value

    Returns:
        Clamped velocity (0-127)

    Raises:
        ValueError: If velocity is not an integer
    """
    if not isinstance(velocity, int):
        raise ValueError(f"Velocity must be an integer, got {type(velocity)}")

    return max(0, min(127, velocity))
