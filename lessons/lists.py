"""Introduction to Lists"""

names: list[str] = list()

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

print(my_numbers)


# Add items to list
my_numbers.append(1.5)
my_numbers.append(2.3)

print(my_numbers)

# Create and already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription notation/indexing
print(game_points[2])

game_points[1] = 72
print(game_points)

# Length of list
print(len(game_points))

# Removes value from list
game_points.pop(1)
print(game_points)


def display(user_list: list[int]) -> None:

    index: int = 0

    while len(user_list) > index:

        print(user_list[index])

        index = +1
