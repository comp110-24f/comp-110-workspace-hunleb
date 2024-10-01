"""A Program to Plan a Tea Party"""

__author__: str = "730747201"


def main_planner(guests: int) -> None:
    """Prints the statements below after being provided the number of guests"""

    print("A Cozy Tea Party for " + str(guests) + " people!")

    print("Tea Bags: " + str(tea_bags(guests)))

    print("Treats: " + str(treats(guests)))

    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))

    return None


def tea_bags(people: int) -> int:
    """Returns 2 tea bags for every person."""

    return people * 2


def treats(people: int) -> int:
    """Returns 1.5 treats for every person."""

    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of tea and treats then combines the cost."""

    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
