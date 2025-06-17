import random

levels = {
    "easy": [1, 10],
    "medium": [1, 50],
    "hard": [1, 150],
}
mode = "easy"
number_range = levels[mode]
number = random.randint(number_range[0], number_range[1])