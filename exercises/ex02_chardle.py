"""EX02 - Chardle - A cute step toawrd Wordle."""

__author__ = "730747201"


def input_word() -> str:
    """Defines input_word as a function and returns a str value of user's input"""

    user_word: str = input(
        "Enter a 5-character word: "
    )  # Prompts the user to input a word when input_word is called.

    if (
        len(user_word) != 5
    ):  # Conditional logic that checks if the user's word of choice is exactly 5 characters.

        print(
            "Error: Word must contain 5 characters."
        )  # Prints this message informing the user that their word is not 5 characters long.
        exit()  # Exits the program to prevent any more code from running.

    return user_word  # Returns the user's input as their given word.


def input_letter() -> str:
    """Defines input_character as a function and returns a str value of user's input"""

    user_character: str = input(
        "Enter a single character: "
    )  # Prompts the user to input a character when input_character is called.

    if (
        len(user_character) != 1
    ):  # Conditional logic that checks if the user's character of choice is exactly 1 character long.

        print(
            "Error: Character must be a single character."
        )  # Prints this message informing the user that their character is longer than 1 character.
        exit()  # Exits the program to prevent any more code from running.

    return user_character  # Returns the user's input as their given character.


def contains_char(word: str, letter: str) -> None:
    """Defines contains_char as a funtion that checks for any instances of letter in word"""

    print(
        "Searching for " + letter + " in " + word
    )  # Informs the user that the inputted character is being searched for in the word.

    count = 0

    if word[0] == letter:

        print(
            letter + " found at index 0"
        )  # Uses conditional logic to search for the letter in index 0 and prints if found.
        count = (
            count + 1
        )  # Adds one to count which will be used to inform the user of how many instances of the letter are found.

    if word[1] == letter:

        print(
            letter + " found at index 1"
        )  # Uses conditional logic to search for the letter in index 1 and prints if found.
        count = (
            count + 1
        )  # Adds one to count which will be used to inform the user of how many instances of the letter are found.

    if word[2] == letter:

        print(
            letter + " found at index 2"
        )  # Uses conditional logic to search for the letter in index 2 and prints if found.
        count = (
            count + 1
        )  # Adds one to count which will be used to inform the user of how many instances of the letter are found.

    if word[3] == letter:

        print(
            letter + " found at index 3"
        )  # Uses conditional logic to search for the letter in index 3 and prints if found.
        count = (
            count + 1
        )  # Adds one to count which will be used to inform the user of how many instances of the letter are found.

    if word[4] == letter:

        print(
            letter + " found at index 4"
        )  # Uses conditional logic to search for the letter in index 4 and prints if found.
        count = (
            count + 1
        )  # Adds one to count which will be used to inform the user of how many instances of the letter are found.

    if count == 0:
        print(
            "No instances of " + letter + " found in " + word
        )  # Informs the user that there are no instances of their given letter found in the word.

    elif count == 1:
        print(
            "1 instance of " + letter + " found in " + word
        )  # Informs the user that there is one instance of their given letter found in the word.

    else:
        print(
            str(count) + " instances of " + letter + " found in " + word
        )  # Informs the user that there are 2-5 instances of their given letter found in the word.

    return None


def main() -> None:

    contains_char(
        word=input_word(), letter=input_letter()
    )  # Combines all of the functions previously written.

    return None


if __name__ == "__main__":
    main()
