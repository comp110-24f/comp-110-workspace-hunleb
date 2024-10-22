__author__ = "730747201"


def find_and_remove_max(list1: list[int]) -> int:

    if len(list1) == 0:

        return -1

    max_number = list1[0]

    for i in range(1, len(list1)):

        if list1[i] >= max_number:

            max_number = list1[i]

    index: int = 0

    while index < len(list1):

        if list1[index] == max_number:

            list1.pop(index)

        else:

            index += 1

    return max_number
