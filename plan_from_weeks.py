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
from src.last_week import print_last_week
from src.taper_weeks import print_taper_weeks
from src.train_weeks import print_train_weeks
from src.utils import num_between, random_item

weeks_to_train = WEEKS_TO_TRAIN - 1

if RACE_DISTANCE == "half-marathon":
    weeks_to_train -= 2  # Two weeks for tapering

if RACE_DISTANCE == "marathon":
    weeks_to_train -= 3  # Three weeks for tapering

print_train_weeks(weeks_to_train)
print_taper_weeks(weeks_to_train)
print_last_week()
