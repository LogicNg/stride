import random


def random_item(array):
    return random.choice(array)


def num_between(min_val, max_val, i, number_of_weeks_to_train):
    difference = max_val - min_val
    increment = difference / number_of_weeks_to_train
    return round(min_val + increment * i)
