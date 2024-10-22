from CQs.cq07.find_max import find_and_remove_max

__author__ = "730747201"


def test_get_first() -> None:

    numbers: list[int] = [
        1,
        2,
        3,
    ]

    assert find_and_remove_max(numbers) == 3


def test_mutate() -> None:

    test_list: list[int] = [2, 4, 4, 3, 1]

    expected_list: list[int] = [2, 3, 1]

    find_and_remove_max(test_list)

    assert test_list == expected_list


def test_unconventional() -> None:

    empty: list[int] = []

    assert find_and_remove_max(empty) == -1
