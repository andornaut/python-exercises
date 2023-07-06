from collections import namedtuple
import csv
import os
from random import shuffle
from typing import Generator

Person = namedtuple("Person", "name email")


def _absolute_path(filepath: str) -> str:
    return os.path.normpath(os.path.join(os.path.dirname(__file__), filepath))


def _line_to_person(line: list[str]) -> Person:
    name, email = line
    return Person(name, email)


def _read_csv(filepath: str) -> list[Person]:
    lines = _yield_lines(_absolute_path(filepath))
    return [_line_to_person(line) for line in lines]


def _shuffle_people(people: list[Person]) -> list[Person]:
    people = people.copy()
    shuffle(people)
    return people


def _yield_lines(filepath: str) -> Generator[list[str], None, None]:
    with open(filepath) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            yield row


def _assign_exchangers(
    givers: list[Person], receivers: list[Person]
) -> list[tuple[Person, Person]]:
    exchangers = []
    have_received = set()
    for giver in givers:
        for receiver in receivers:
            if giver == receiver:
                continue
            if receiver in have_received:
                continue
            exchangers.append((giver, receiver))
            have_received.add(receiver)
            break
    return exchangers


def gift_exchange(filepath: str):
    people = _read_csv(filepath)
    givers = _shuffle_people(people)
    receivers = _shuffle_people(people)
    exchangers = _assign_exchangers(givers, receivers)

    # There can only be 0 or 1 unassigned person, and they're both giver and receiver
    unassigned_person_or_empty = set(givers) - {giver for (giver, _) in exchangers}
    if unassigned_person_or_empty:
        unassigned_person = unassigned_person_or_empty.pop()
        (giver, receiver) = exchangers.pop()
        exchangers.append((giver, unassigned_person))
        exchangers.append((unassigned_person, receiver))

    for giver, receiver in exchangers:
        print(f"{giver.email} -> {receiver.email}")


if __name__ == "__main__":
    """
    Run with either:
    `python gift_exchange.py` or
    `exercises gift-exchange`
    """
    gift_exchange("gift_exchange.csv")
