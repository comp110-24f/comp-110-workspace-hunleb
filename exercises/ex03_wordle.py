"""EX03 - Structured Wordle"""

__author__: str = "730747201"


def input_guess(user_word_len: int) -> str:
    """Function that returns the user's word if it is the correct length"""

    word_guess: str = input(
        f"Enter a {user_word_len} character word: "
    )  # Prompts the user to enter enter a word which will be stored as word_guess

    while (
        len(word_guess) != user_word_len
    ):  # Creates a while loop that will continue until the user inputs a word with the correct length, making the while statement false

        word_guess = input(
            f"That wasn't {user_word_len} chars! Try again: "
        )  # Prompts the user to input a word with the correct length, stores value as word_guess

    return word_guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Returns True/False if char_guess is/n't found in secret_word"""
    assert len(char_guess) == 1

    index: int = 0

    while len(secret_word) > index:

        if secret_word[index] == char_guess:

            return (
                True  # Returns True if char_guess if found in an index of secret_word
            )

        index += 1  # Allows for each letter to be checked in secret_word

    return False  # Returns False if char_guess is not found in an index of secret_word


def emojified(word_guess: str, secret_word: str) -> str:
    """Function that uses emojis to indicate where a character is located in the secret word"""

    assert len(word_guess) == len(
        secret_word
    )  # States the guessed word and secret word are the same length

    WHITE_BOX: str = "\U00002B1C"  # White box emoji
    GREEN_BOX: str = "\U0001F7E9"  # Green box emoji
    YELLOW_BOX: str = "\U0001F7E8"  # Yellow box emoji

    index: int = 0

    boxes: str = ""  # Empty string that will be used to add the colored boxes

    while len(word_guess) > index:

        if (
            word_guess[index] == secret_word[index]
        ):  # Adds a green box if the same letter exists at the same index
            boxes += GREEN_BOX
        elif contains_char(
            secret_word, word_guess[index]
        ):  # Adds a yellow box if the letter is found elsewhere in the word
            boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX  # Adds a white box if the letter is not found anywhere in the word

        index += 1

    return boxes  # Returns the string with boxes in it


def main(secret: str) -> None:
    """The entrypoint of the program and the main game loop."""

    turn: int = 1  # Counts the amount of turns the user is on

    guess: str = input_guess(len(secret))
    # Defines the guess variable, representing the word that the user guesses, asks user for a word based on # of letters in secret
    while turn <= 6:
        print(
            f"=== Turn {turn}/6 ==="
        )  # Prints what turn the user is on, starting at 1

        print(
            emojified(guess, secret)
        )  # Prints the box emojies based on the guessed word

        if guess == secret:

            print(
                f"You won in {turn}/6 turns!"
            )  # If the user guesses the secret word, this will print
            quit()
        else:

            guess = input_guess(user_word_len=len(secret))

        turn += 1  # Increases amount of turns user has taken

    if turn > 6:
        print(
            "X/6 - Sorry, try again tomorrow!"
        )  # If the user uses all 6 turns before guessing secret, this will print


if __name__ == "__main__":
    main(secret="codes")
