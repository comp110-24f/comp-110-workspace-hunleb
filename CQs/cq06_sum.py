"""Summing the elements of a list using different loops"""

__author__ = "730747201"


def w_sum(vals: list[float]) -> float:

    idx = 0

    sum = 0.0

    while idx < len(vals):

        sum += vals[idx]

        idx += 1

    return sum


def f_sum(vals: list[float]) -> float:

    sum = 0.0

    for idx in vals:

        sum += idx

    return sum


def f_range_sum(vals: list[float]) -> float:

    sum = 0.0

    for idx in range(0, len(vals)):

        sum += vals[idx]

    return sum
