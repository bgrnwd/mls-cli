from typer import Argument, echo, Typer, Option, Exit
from rich.console import Console
from rich.table import Table
from pandas import read_html
from typing import Optional

app = Typer()
console = Console()


@app.command("g")
def game(date: Optional[str] = Argument(None)):
    echo("Game on!")


@app.command("s")
def standings(conf: Optional[str] = Argument(None)):
    if conf is None:
        response = read_html(
            "https://www.mlssoccer.com/standings/supporters-shield", header=1
        )
        df = response[0]
    else:
        response = read_html("https://www.mlssoccer.com/standings", header=1)
        if conf in ["E", "e", "east", "East", "Eastern", "eastern"]:
            df = response[0]
        elif conf in ["W", "w", "west", "Western", "western"]:
            df = response[1]
        else:
            echo("Conference not recognized")
            Exit(1)

    df.dropna(axis=1, how="all", inplace=True)
    table = Table(title="MLS Standings")
    for col in df.columns:
        table.add_column(col)

    for val in df.values:
        table.add_row(*[str(v) for v in val])

    console.print(table)


@app.command("p")
def player(
    name: str,
    playoffs: bool = Option(False),
    regular: bool = Option(False),
):
    PLAYER_URL = f"https://www.mlssoccer.com/players/{name.replace(' ','-').lower()}"
    player_data = read_html(PLAYER_URL)
    if regular:
        df = player_data[0]
        table = Table(title="Career Statistics (Regular Season)")
    elif playoffs:
        df = player_data[1]
        table = Table(title="Career Statistics (Playoffs)")
    else:
        echo("Option not recognized")
        Exit(1)

    df.dropna(axis=1, how="all", inplace=True)
    for col in df.columns:
        table.add_column(col)

    for val in df.values:
        table.add_row(*[str(v) for v in val])

    console.print(table)


if __name__ == "__main__":
    app()
