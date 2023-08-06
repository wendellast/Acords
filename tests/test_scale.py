from pytest import mark, raises

from acords.scales import NOTES, SCALES, scales


def test_scale_should_work_with_lowercase_notes():
    tonic = 'c'
    tonality = 'maior'
    result = scales(tonic, tonality)
    assert result


def test_note_not_found_return_as_erro():
    tonic = 'x'
    tonality = 'maior'

    message_of_erro = f'Note not found, try one of thesee {NOTES}'

    with raises(ValueError) as erro:
        result = scales(tonic, tonality)

    assert message_of_erro == erro.value.args[0]


def test_should_return_an_erro_saying_that_the_scale_does_not_exist():
    tonic = 'C'
    tonality = 'tonality'
    message_of_erro = (
        'These scales do not exist or have not been implemented, '
        f'try one of these: {list(SCALES.keys())}'
    )

    with raises(KeyError) as erro:
        result = scales(tonic, tonality)

    assert message_of_erro == erro.value.args[0]


@mark.parametrize(
    'tonic,expected',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_should_return_the_correct_notes(tonic, expected):
    result = scales(tonic, 'maior')

    assert result['notes'] == expected


def test_should_return_seven_degrees():
    tonic = 'C'
    tonality = 'maior'
    expected = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    result = scales(tonic, tonality)['degrees']
    assert result == expected
