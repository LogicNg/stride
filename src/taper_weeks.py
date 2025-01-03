from src.constants import (
    LONG_RUN_SESSIONS,
    MEDIUM_RUN_SESSIONS,
    RACE_DISTANCE,
    SPEED_RUN_SESSIONS,
)
from src.utils import random_item

taper_weeks = []


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


def print_taper_weeks(starting_weak):
    for index, week in enumerate(taper_weeks):
        print(f"Week {starting_weak + index}:")
        print("Day 1: Rest or Crosstrain")
        print(
            f"Day 2: {random_item(MEDIUM_RUN_SESSIONS)} - {week['medium_run_distance']}k"
        )
        print(f"Day 3: Easy - {week['easy_run_distance']}k")
        print(
            f"Day 4: {random_item(SPEED_RUN_SESSIONS)} - {week['speed_run_distance']}k"
        )
        print("Day 5: Rest or Crosstrain")
        print(f"Day 6: Easy - {week['easy_run_distance']}k")
        print(f"Day 7: {random_item(LONG_RUN_SESSIONS)} - {week['long_run_distance']}k")
        print()
