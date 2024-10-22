"""Ex05 - More list utility functions"""

__author__: str = "730747201"


def only_evens(list1: list[int]) -> list[int]:
    """Returns only the even values of a given list."""
    newlist: list[int] = []

    for x in range(0, len(list1)):

        if list1[x] % 2 == 0:

            newlist.append(list1[x])

    return newlist


def sub(list1: list[int], start: int, end: int) -> list[int]:
    """Returns a list that contains the values of a list between a start and end point."""
    if len(list1) == 0 or start >= len(list1) or end <= 0:

        return []

    if start < 0:

        start = 0

    if end > len(list1):

        end = len(list1)

    newlist: list[int] = []

    for x in range(start, end):

        newlist.append(list1[x])

    return newlist


def add_at_index(list1: list[int], element: int, index: int) -> None:
    """Adds a value to a list at a given index."""
    if index < 0 or index > len(list1):

        raise IndexError("Index is out of bounds for the input list")

    list1.append(0)

    for i in range(len(list1) - 1, index, -1):

        list1[i] = list1[i - 1]

    list1[index] = element

    print(element)

    return None
