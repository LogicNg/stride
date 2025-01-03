from src.constants import RACE_DISTANCE

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
