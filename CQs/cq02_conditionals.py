"""Practice with Conditionals, Local Variables, and User Input"""

__author__ = "730747201"


def guess_a_number() -> None:
    """Establishes the secret number as 7"""

    secret: int = 7

    """Asks the user to input a number"""

    guessed_number = int(input("Guess a number:"))

    """Prints the number inputted by the user"""

    print("Your guess was " + str(guessed_number))

    """Compares the input number to the secret number and returns the correct statement"""

    if guessed_number == secret:

        print("You got it!")

    elif guessed_number < secret:

        print("Your guess was too low! The secret number is " + str(secret))

    else:

        print("Your guess was too high! The secret number is " + str(secret))

    return None


if __name__ == "__main__":
    guess_a_number()
