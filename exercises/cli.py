from typing import Optional

import typer

from exercises import (
    __app_name__,
    __version__,
    gift_exchange as gift_exchange_module,
)
from exercises.hackerrank.cli import app as hackerrank_app


app = typer.Typer(add_completion=False, no_args_is_help=True)
app.add_typer(hackerrank_app, name="hackerrank")


@app.command()
def gift_exchange(filepath: str = "gift_exchange.csv"):
    # `filepath` may be relative to the cliapp module or an absolute path
    # eg.
    #   exercises gift-exchange gift_exchange.csv
    #   or
    #   exercises gift-exchange ${PWD}/cliapp/data/gift_exchange.csv
    gift_exchange_module.gift_exchange(filepath)


@app.callback(invoke_without_command=True)
def default(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        is_eager=True,
    )
) -> None:
    """
    Coding exercises in Python
    """
    if version:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()
