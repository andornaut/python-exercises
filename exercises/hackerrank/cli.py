from typing import Annotated

import typer

from exercises.hackerrank import search, sorting, string_manipulation

app = typer.Typer(add_completion=False, no_args_is_help=True)


@app.command()
def fraudulent_activity_notifications(expenditure: list[int], days: int):
    result = sorting.fraudulent_activity_notifications(expenditure, days)
    print(result)


@app.command()
def sherlock_and_the_valid_string(sample: str):
    result = string_manipulation.sherlock_and_the_valid_string(sample)
    print(result)


@app.command()
def triple_sum(
    a: Annotated[list[int], typer.Option()],
    b: Annotated[list[int], typer.Option()],
    c: Annotated[list[int], typer.Option()],
):
    result = search.triple_sum(a, b, c)
    print(result)
