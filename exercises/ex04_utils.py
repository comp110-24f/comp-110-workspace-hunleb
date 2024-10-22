"""EX04 - List Utility Functions"""

__author__: str = "730747201"


def all(list: list[int], int: int) -> bool:
    """Checks if int is equal to every value in list"""

    if len(list) == 0:

        return False  # safeguard incase the list is empty

    for x in list:  # loops through every value of list

        if x != int:  # if a value in list is not equal int..

            return False  # it will return False

    return True  # if all are equal, return True


def max(input: list[int]) -> int:
    """Returns the largest value in a given list"""
    if len(input) == 0:

        raise ValueError(
            "max() arg is an empty List"
        )  # safeguard that returns error message

    max_number = input[
        0
    ]  # declares max_number as a variable, starting at the first list value

    for i in range(1, len(input)):  # for every value after the first..

        if input[i] > max_number:  # if that value is greater than max_number..

            max_number = input[i]  # max_number is updated to the largest value in input

    return max_number  # returns the largest number found


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Function that determines if two lists are equal"""

    if len(list1) != len(list2):  # if both lists are not equal length..

        return False  # returns False

    for i in range(len(list1)):  # for every value in the length of list1..

        if (
            list1[i] != list2[i]
        ):  # if the values in both lists at the same position does not equal..

            return False  # returns False

    return True  # if the above conditions are not met, returns True


def extend(list1: list[int], list2: list[int]) -> None:
    """Function that takes in two lists, then adds second to first"""

    i: int = 0  # incrementor

    while i < len(list2):  # iterates through every value in list2

        list1.append(list2[i])  # appends each value in list2 to list 1

        i += 1  # incrementor

    return  # returns nothing
