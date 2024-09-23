"""While Loops Challenge Question"""

__author__ = "730747201"


def num_instances(phrase: str, search_char: str) -> int:
    """Defines num_instances which will take the user's input and return how many instances there are."""
    count: int = 0

    index: int = 0

    """Declares the variable count which will keep track of how many instances there are of a letter"""
    """Declares the variable index which will allow the loop to compare search_char to each letter of phrase"""

    while index < len(phrase):
        """Runs if there is an instance of search_char in phrase"""
        if phrase[index] == search_char:
            """Adds 1 to count for every instance of the given search_char"""
            count = count + 1
        """Adds one to index in order to loop the funciton until phrase has been completed"""
        index = index + 1
    """Returns the value of count"""
    return count
