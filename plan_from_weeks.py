import random

from src.constants import (
    LONG_RUN_SESSIONS,
    MEDIUM_RUN_SESSIONS,
    RACE_DISTANCE,
    SPEED_RUN_SESSIONS,
    WEEKS_TO_TRAIN,
)
from src.distances import (
    max_easy_run_distance,
    max_long_run_distance,
    max_medium_run_distance,
    max_speed_run_distance,
    min_easy_run_distance,
    min_long_run_distance,
    min_medium_run_distance,
    min_speed_run_distance,
)
from src.utils import num_between, random_item

weeks_to_train = WEEKS_TO_TRAIN


def handle_number_of_weeks_to_train():
    global weeks_to_train
    weeks_to_train -= 1  # Reserve one week for race week
    if RACE_DISTANCE == "half-marathon":
        weeks_to_train -= 2  # Two weeks for tapering
    if RACE_DISTANCE == "marathon":
        weeks_to_train -= 3  # Three weeks for tapering


def handle_taper_weeks(week, week_number):
    print(f"Week {week_number}:")
    print("Day 1: Rest or Crosstrain")
    print(f"Day 2: {random_item(MEDIUM_RUN_SESSIONS)} - {week['medium_run_distance']}k")
    print(f"Day 3: Easy - {week['easy_run_distance']}k")
    print(f"Day 4: {random_item(SPEED_RUN_SESSIONS)} - {week['speed_run_distance']}k")
    print("Day 5: Rest or Crosstrain")
    print(f"Day 6: Easy - {week['easy_run_distance']}k")
    print(f"Day 7: {random_item(LONG_RUN_SESSIONS)} - {week['long_run_distance']}k")


for i in range(1, weeks_to_train + 1):
    print(f"Week {i}:")
    print("Day 1: Rest or Crosstrain")
    print(
        f"Day 2: {random_item(MEDIUM_RUN_SESSIONS)} - {num_between(min_medium_run_distance, max_medium_run_distance, i, weeks_to_train)}k"
    )
    print(
        f"Day 3: Easy - {num_between(min_easy_run_distance, max_easy_run_distance, i, weeks_to_train)}k"
    )
    print(
        f"Day 4: {random_item(SPEED_RUN_SESSIONS)} - {num_between(min_speed_run_distance, max_speed_run_distance, i, weeks_to_train)}k"
    )
    print("Day 5: Rest or Crosstrain")
    print(
        f"Day 6: Easy - {num_between(min_easy_run_distance, max_easy_run_distance, i, weeks_to_train)}k"
    )
    print(
        f"Day 7: {random_item(LONG_RUN_SESSIONS)} - {num_between(min_long_run_distance, max_long_run_distance, i, weeks_to_train)}k"
    )

if RACE_DISTANCE == "half-marathon":
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
        handle_taper_weeks(week, weeks_to_train + index + 1)

if RACE_DISTANCE == "marathon":
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
        handle_taper_weeks(week, weeks_to_train + index + 1)

print(f"Week {weeks_to_train + 1}:")
print("Day 1: Rest or Crosstrain")
print("Day 2: Easy - 5k")
print("Day 3: Rest or Crosstrain")
print("Day 4: Rest")
print("Day 5: Easy - 3k")
print("Day 6: Rest")
print("Day 7: Race Day!")
