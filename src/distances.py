from src.constants import RACE_DISTANCE

if RACE_DISTANCE == "5k":
    min_easy_run_distance = 5
    max_easy_run_distance = 8
    min_medium_run_distance = 4
    max_medium_run_distance = 5
    min_speed_run_distance = 3
    max_speed_run_distance = 4
    min_long_run_distance = 8
    max_long_run_distance = 12
elif RACE_DISTANCE == "10k":
    min_easy_run_distance = 6
    max_easy_run_distance = 9
    min_medium_run_distance = 5
    max_medium_run_distance = 8
    min_speed_run_distance = 4
    max_speed_run_distance = 7
    min_long_run_distance = 8
    max_long_run_distance = 14
elif RACE_DISTANCE == "half-marathon":
    min_easy_run_distance = 7
    max_easy_run_distance = 12
    min_medium_run_distance = 6
    max_medium_run_distance = 10
    min_speed_run_distance = 5
    max_speed_run_distance = 10
    min_long_run_distance = 10
    max_long_run_distance = 18
elif RACE_DISTANCE == "marathon":
    min_easy_run_distance = 8
    max_easy_run_distance = 16
    min_medium_run_distance = 7
    max_medium_run_distance = 13
    min_speed_run_distance = 7
    max_speed_run_distance = 10
    min_long_run_distance = 12
    max_long_run_distance = 35
