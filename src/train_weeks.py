from src.constants import LONG_RUN_SESSIONS, MEDIUM_RUN_SESSIONS, SPEED_RUN_SESSIONS
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


def print_train_weeks(weeks_to_train):
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
        print()
