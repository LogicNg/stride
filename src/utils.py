import random


def random_item(array):
    return random.choice(array)


def num_between(min_val, max_val, i, splits):
    difference = max_val - min_val
    increment = difference / splits
    return round(min_val + increment * i)
