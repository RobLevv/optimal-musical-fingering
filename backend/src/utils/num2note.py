"""
This module provides a function to convert a number to its corresponding musical note.
The notes are represented in MIDI note number format, where C0 = 0 and G10 = 127.
"""
__author__ = "Eliot Christon"
__email__  = "eliot.christon@gmail.com"
__github__ = "eliot-christon"

def num2note(num:int) -> str:
    """Convert a number to its corresponding note. (midi note number, C0 = 0, G10 = 127)"""
    if num < 0 or num > 127:
        raise ValueError(f"The number {num} is not in the range of a midi note number (0-127)")
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note = notes[num % 12]
    octave = num // 12
    return note + str(octave)
