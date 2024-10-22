"""Mutating functions."""

__author__ = "730747201"


def manual_append(list: list[int], int: int) -> None:

    list.append(int)

    return


def double(list: list[int]) -> None:

    idx = 0

    while idx < len(list):

        list[idx] = list[idx] * 2

        idx += 1

    return


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
