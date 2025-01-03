import random

from src.constants import (
    distance_value,
    long_run_sessions,
    medium_run_sessions,
    number_of_weeks_to_train,
    speed_run_sessions,
)

minimum_easy_run_distance = None
maximum_easy_run_distance = None
minimum_medium_run_distance = None
maximum_medium_run_distance = None
minimum_speed_run_distance = None
maximum_speed_run_distance = None
minimum_long_run_distance = None
maximum_long_run_distance = None


def handle_number_of_weeks_to_train():
    global number_of_weeks_to_train
    number_of_weeks_to_train -= 1  # Reserve one week for race week
    if distance_value == "half-marathon":
        number_of_weeks_to_train -= 2  # Two weeks for tapering
    if distance_value == "marathon":
        number_of_weeks_to_train -= 3  # Three weeks for tapering


def handle_distance_change():
    global minimum_easy_run_distance, maximum_easy_run_distance
    global minimum_medium_run_distance, maximum_medium_run_distance
    global minimum_speed_run_distance, maximum_speed_run_distance
    global minimum_long_run_distance, maximum_long_run_distance

    if distance_value == "5k":
        minimum_easy_run_distance = 5
        maximum_easy_run_distance = 8
        minimum_medium_run_distance = 4
        maximum_medium_run_distance = 5
        minimum_speed_run_distance = 3
        maximum_speed_run_distance = 4
        minimum_long_run_distance = 8
        maximum_long_run_distance = 12
    elif distance_value == "10k":
        minimum_easy_run_distance = 6
        maximum_easy_run_distance = 9
        minimum_medium_run_distance = 5
        maximum_medium_run_distance = 8
        minimum_speed_run_distance = 4
        maximum_speed_run_distance = 7
        minimum_long_run_distance = 8
        maximum_long_run_distance = 14
    elif distance_value == "half-marathon":
        minimum_easy_run_distance = 7
        maximum_easy_run_distance = 12
        minimum_medium_run_distance = 6
        maximum_medium_run_distance = 10
        minimum_speed_run_distance = 5
        maximum_speed_run_distance = 10
        minimum_long_run_distance = 10
        maximum_long_run_distance = 18
    elif distance_value == "marathon":
        minimum_easy_run_distance = 8
        maximum_easy_run_distance = 16
        minimum_medium_run_distance = 7
        maximum_medium_run_distance = 13
        minimum_speed_run_distance = 7
        maximum_speed_run_distance = 10
        minimum_long_run_distance = 12
        maximum_long_run_distance = 35


def get_random_session(array):
    return random.choice(array)


def get_increasing_number_between(min_val, max_val, i, number_of_weeks_to_train):
    difference = max_val - min_val
    increment = difference / number_of_weeks_to_train
    return round(min_val + increment * i)


def handle_taper_weeks(week, week_number):
    print(f"Week {week_number}:")
    print("Day 1: Rest or Crosstrain")
    print(
        f"Day 2: {get_random_session(medium_run_sessions)} - {week['medium_run_distance']}k"
    )
    print(f"Day 3: Easy - {week['easy_run_distance']}k")
    print(
        f"Day 4: {get_random_session(speed_run_sessions)} - {week['speed_run_distance']}k"
    )
    print("Day 5: Rest or Crosstrain")
    print(f"Day 6: Easy - {week['easy_run_distance']}k")
    print(
        f"Day 7: {get_random_session(long_run_sessions)} - {week['long_run_distance']}k"
    )


def create_plan():
    print("\033c", end="")  # Clear the console for a fresh plan

    handle_distance_change()
    handle_number_of_weeks_to_train()

    for i in range(1, number_of_weeks_to_train + 1):
        print(f"Week {i}:")
        print("Day 1: Rest or Crosstrain")
        print(
            f"Day 2: {get_random_session(medium_run_sessions)} - {get_increasing_number_between(minimum_medium_run_distance, maximum_medium_run_distance, i, number_of_weeks_to_train)}k"
        )
        print(
            f"Day 3: Easy - {get_increasing_number_between(minimum_easy_run_distance, maximum_easy_run_distance, i, number_of_weeks_to_train)}k"
        )
        print(
            f"Day 4: {get_random_session(speed_run_sessions)} - {get_increasing_number_between(minimum_speed_run_distance, maximum_speed_run_distance, i, number_of_weeks_to_train)}k"
        )
        print("Day 5: Rest or Crosstrain")
        print(
            f"Day 6: Easy - {get_increasing_number_between(minimum_easy_run_distance, maximum_easy_run_distance, i, number_of_weeks_to_train)}k"
        )
        print(
            f"Day 7: {get_random_session(long_run_sessions)} - {get_increasing_number_between(minimum_long_run_distance, maximum_long_run_distance, i, number_of_weeks_to_train)}k"
        )

    if distance_value == "half-marathon":
        taper_weeks = [
            {
                "long_run_distance": 15,
                "medium_run_distance": 7,
                "speed_run_distance": 7,
                "easy_run_distance": 10,
            },
            {
                "long_run_distance": 12,
                "medium_run_distance": 6,
                "speed_run_distance": 5,
                "easy_run_distance": 10,
            },
        ]
        for index, week in enumerate(taper_weeks):
            handle_taper_weeks(week, number_of_weeks_to_train + index + 1)

    if distance_value == "marathon":
        taper_weeks = [
            {
                "long_run_distance": 26,
                "medium_run_distance": 10,
                "speed_run_distance": 8,
                "easy_run_distance": 12,
            },
            {
                "long_run_distance": 20,
                "medium_run_distance": 8,
                "speed_run_distance": 6,
                "easy_run_distance": 10,
            },
            {
                "long_run_distance": 16,
                "medium_run_distance": 7,
                "speed_run_distance": 4,
                "easy_run_distance": 10,
            },
        ]
        for index, week in enumerate(taper_weeks):
            handle_taper_weeks(week, number_of_weeks_to_train + index + 1)

    print(f"Week {number_of_weeks_to_train + 1}:")
    print("Day 1: Rest or Crosstrain")
    print("Day 2: Easy - 5k")
    print("Day 3: Rest or Crosstrain")
    print("Day 4: Rest")
    print("Day 5: Easy - 3k")
    print("Day 6: Rest")
    print("Day 7: Race Day!")


create_plan()
