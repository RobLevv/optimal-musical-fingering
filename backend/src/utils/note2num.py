"""
This module provides a function to convert musical notes to their corresponding MIDI note numbers.
"""
__author__ = "Eliot Christon"
__email__  = "eliot.christon@gmail.com"
__github__ = "eliot-christon"

def note2num(note:str) -> int:
    """Convert a note to its corresponding number. (midi note number, C0 = 0, G10 = 127)"""
    notes = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}

    # the note has, at least, 1 letter and 1 number. It could also have an alteration (# or b)
    letter = note[0]
    if note[1] in ["#", "b"]:
        alt = note[1]
        octave = int(note[2:])
    else:
        alt = ""
        octave = int(note[1:])

    num = notes[letter] + 12 * octave
    num += 1 * (alt == "#") - 1 * (alt == "b")

    if num < 0 or num > 127:
        raise ValueError(\
            f"The note {note} is not in the range of a midi note number (0-127), number is {num}")

    return num
