NOTES = 'C C# D D# E F F# G G# A A# B'.split()
SCALES = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def scales(tonic: str, tonality: str) -> dict[str, list[str]]:
    """
    Generates a scale apart from a tonic and a tonality

    Parameters:
        tonic: Note that will be tonic of the scale
        tonality: Scale tonality

    Returns:
        Returns a dictionary with the notes of the scales and the degrees

    Examples:
        >>> scales('C', 'maior')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scales('A', 'maior')
        {'notes': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """

    intervals = SCALES[tonality]
    tonic_pos = NOTES.index(tonic)

    temp = []

    for interval in intervals:
        note = (tonic_pos + interval) % 12
        temp.append(NOTES[note])

    return {
        'notes': temp,
        'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
