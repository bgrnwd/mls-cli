from typer import Argument, echo, Typer, Option, Exit
from rich.console import Console
from rich.table import Table
from pandas import read_html, DataFrame
from typing import Optional
from datetime import datetime

app = Typer()
console = Console()
dt = datetime.today()


def _filter_and_create_rich_table(df: DataFrame, title: str) -> Table:
    """
    Takes a DataFrame and drops any columns where all values are null.
    Converts the DataFrame to a rich table and prints the output to the
    console.

    :param df: DataFrame containing the scrapped HTML table
    :param title: string for the title of the console table
    :returns: None
    """
    df.dropna(axis=1, how="all", inplace=True)
    table = Table(title=title)

    for col in df.columns:
        table.add_column(col)

    for val in df.values:
        table.add_row(*[str(v) for v in val])

    console.print(table)

    return table


# @app.command("g")
# @app.command("game")
# def game(date: Optional[str] = Argument(None)) -> None:
#     """
#     Gets the current status of a game

#     :param date: date
#     :returns: None
#     """
#     # TODO


@app.command("s")
@app.command("standings")
def standings(conf: Optional[str] = Argument(None)) -> None:
    """
    Queries the MLS website and prints the current standings in the
    user's terminal.

    :param conf: string to limit the query to the eastern or western
                 conference
    :returns: None
    """
    if conf is None:
        response = read_html(
            "https://www.mlssoccer.com/standings/supporters-shield", header=1
        )
        df = response[0]
        heading = "MLS Standings"
    else:
        response = read_html("https://www.mlssoccer.com/standings", header=1)
        if conf in ["E", "e", "east", "East", "Eastern", "eastern"]:
            df = response[0]
            heading = "Eastern Conference Standings"
        elif conf in ["W", "w", "west", "Western", "western"]:
            df = response[1]
            heading = "Western Conference Standings"
        else:
            echo("Conference not recognized")
            Exit(1)

    _filter_and_create_rich_table(df, heading)


@app.command("p")
@app.command("player")
def player(
    name: str,
    playoffs: bool = Option(False),
    regular: bool = Option(False),
) -> None:
    """
    Queries the MLS website and prints the player's statistics in the
    user's terminal.

    :param name: name of the player
    :param playoffs: flag used to get playoff statistics
    :param regular: flag used to get regular season statistics
    :returns: None
    """
    PLAYER_URL = f"https://www.mlssoccer.com/players/{name.replace(' ','-').lower()}"
    player_data = read_html(PLAYER_URL)
    df = DataFrame()
    heading = ""
    if regular:
        df = player_data[0]
        heading = f"{name} - Career Statistics (Regular Season)"
    elif playoffs:
        df = player_data[1]
        heading = f"{name} - Career Statistics (Playoffs)"
    else:
        echo("Option not recognized")
        Exit(1)

    _filter_and_create_rich_table(df, heading)


@app.command("t")
@app.command("transactions")
def transactions(
    year: str = dt.year, team: str = Option("", help="Full team name")
) -> None:
    """
    Queries the MLS website and prints the transactions for a given year
    and/or team

    :param team: team name
    :param year: year e.g. 2020
    :returns: None
    """
    TRANSACTION_URL = f"https://www.mlssoccer.com/transactions/{year}"
    teams = read_html(TRANSACTION_URL, header=0)
    if team:
        for t in teams:
            if team in t.keys()[0]:
                df = t
            else:
                continue
        # TODO clean up the way this table is printed
        if not df.empty:
            _filter_and_create_rich_table(
                df, f"{year} {team.capitalize()} Transactions"
            )
        else:
            echo("Team not found")
            Exit(1)

    else:
        for t in teams:
            _filter_and_create_rich_table(t, "Transactions")


def main():
    app()


if __name__ == "__main__":
    main()
