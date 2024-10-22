"""Ex05 - Testing more list utility functions"""

from exercises.ex05.utils import only_evens, sub, add_at_index

import pytest

__author__: str = "730747201"


def test_only_evens() -> None:
    """Test only_evens with even and odd values."""
    list1: list[int] = [1, 2, 23, 27, 30]

    result = only_evens(list1)

    assert result == [2, 30]


def test_only_evens_only_evens() -> None:
    """Test only_evens when all values are even."""
    list1: list[int] = [2, 4, 6, 8, 10]

    result = only_evens(list1)

    assert result == [2, 4, 6, 8, 10]


def test_only_evens_empty_list() -> None:
    """Test that only_evens handles empty lists."""
    list1: list[int] = []

    result = only_evens(list1)

    assert result == []


def test_sub_normal() -> None:
    """Test that sub returns desired list when given a start and end idex"""
    list1: list[int] = [10, 20, 30, 40, 50]

    result = sub(list1, 1, 4)

    assert result == [20, 30, 40]


def test_sub_negative_start() -> None:
    """Test that sub starts at first index when negative."""
    list1: list[int] = [10, 20, 30, 40, 50]

    result = sub(list1, -5, 3)

    assert result == [10, 20, 30]


def test_sub_ofb() -> None:
    """Test that sub can handle end indexes larger than the list."""
    list1: list[int] = [10, 20, 30, 40, 50]

    result = sub(list1, 1, 20)

    assert result == [20, 30, 40, 50]


def test_add_at_index_normal() -> None:
    """Test that add_at_index inputs element at the correct index."""
    list1: list[int] = [1, 2, 3, 4, 5]

    add_at_index(list1, 10, 2)

    assert list1 == [1, 2, 10, 3, 4, 5]


def test_add_at_index_empty_list():
    """Test that add_at_index adds an element to an empty list."""

    lst = []

    add_at_index(lst, 10, 0)

    assert lst == [10]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""

    list_object = [1, 2, 3]

    index_to_insert_num = 10

    value_to_add = 5

    with pytest.raises(IndexError):
        add_at_index(list_object, index_to_insert_num, value_to_add)
