from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from acords.scales import scales

console = Console()
app = Typer()


@app.command()
def scale(
    tonic=Argument('c', help='tonic note of the scale'),
    tonality=Argument('maior', help='tonality of the scale'),
):
    table = Table()
    notes, degrees = scales(tonic, tonality).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*notes)
    console.print(table)
