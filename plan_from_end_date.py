from itertools import cycle, islice

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

START_DATE = "3/1/2025"
END_DATE = "2/2/2025"
TRAIN_EVERY_X_DAYS = 2

from datetime import datetime, timedelta


def training_dates():
    start_date = datetime.strptime(START_DATE, "%d/%m/%Y")
    end_date = datetime.strptime(END_DATE, "%d/%m/%Y")
    training_dates = []

    while start_date <= end_date:
        training_dates.append(start_date.strftime("%d/%m/%Y"))
        start_date += timedelta(days=TRAIN_EVERY_X_DAYS)

    return training_dates


dates = training_dates()
days = len(dates)

plans = list(islice(cycle(["medium", "speed", "easy", "long"]), days))

for i in range(days):
    plan = plans[i]
    training = ""

    if plan == "easy":
        training = f"Easy - {num_between(min_easy_run_distance, max_easy_run_distance, i, days)}k"
    elif plan == "medium":
        training = f"{random_item(MEDIUM_RUN_SESSIONS)} - {num_between(min_medium_run_distance, max_medium_run_distance, i, days)}k"
    elif plan == "speed":
        training = f"{random_item(SPEED_RUN_SESSIONS)} - {num_between(min_speed_run_distance, max_speed_run_distance, i, days)}k"
    elif plan == "long":
        training = f"{random_item(LONG_RUN_SESSIONS)} - {num_between(min_long_run_distance, max_long_run_distance, i, days)}k"

    print(f"{dates[i]}: {training}")
