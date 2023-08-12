from pytest import mark
from typer.testing import CliRunner

from acords.cli import app

runner = CliRunner()


def test_cli_scale_shound_return_0_or_stdout():
    result = runner.invoke(app)
    assert result.exit_code == 0


@mark.parametrize('note', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_cli_scale_shound_contain_of_the_notes_in_the_answer(note):
    result = runner.invoke(app)
    assert note in result.stdout


@mark.parametrize('note', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_cli_scale_shound_contain_of_the_notes_in_the_answer_fa(note):
    result = runner.invoke(app, ['F'])
    assert note in result.stdout


@mark.parametrize('degrees', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_cli_scale_shound_contain_of_the_notes_in_the_answer(degrees):
    result = runner.invoke(app)
    assert degrees in result.stdout
