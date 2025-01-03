from src.constants import RACE_DISTANCE
from src.last_week import print_last_week
from src.taper_weeks import print_taper_weeks
from src.train_weeks import print_train_weeks

WEEKS_TO_TRAIN = 16

weeks_to_train = WEEKS_TO_TRAIN - 1

if RACE_DISTANCE == "half-marathon":
    weeks_to_train -= 2  # Two weeks for tapering

if RACE_DISTANCE == "marathon":
    weeks_to_train -= 3  # Three weeks for tapering

print_train_weeks(weeks_to_train)
print_taper_weeks(weeks_to_train)
print_last_week()
