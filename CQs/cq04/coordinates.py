"""Importing + Scope Challenge Question 4: Coordinates"""

__author__ = "730747201"


def get_coords(xs: str, ys: str) -> None:

    index: int = 0

    count: int = 0

    while index < len(xs):

        count = 0

        while count < len(ys):

            print("(" + xs[index] + "," + ys[count] + ")")

            count += 1

        index += 1

    return
