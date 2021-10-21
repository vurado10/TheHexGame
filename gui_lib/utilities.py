import math
from typing import List


def execute_all_funcs(funcs: List, *args, **kwargs):
    for func in funcs:
        func(*args, **kwargs)


def get_min_max(elements, key=None):
    min_e, max_e = (min(elements, key=key),
                    max(elements, key=key))

    return min_e, max_e


def format_time(title, seconds: float) -> str:
    time_str = str(math.inf)
    if seconds != math.inf:
        seconds_int = round(seconds)
        minutes = seconds_int // 60
        seconds_mod = seconds_int % 60

        minutes_str = str(minutes) if minutes > 9 else "0" + str(minutes)

        seconds_mod_str = str(seconds_mod) \
            if seconds_mod > 9 \
            else "0" + str(seconds_mod)

        time_str = f"{minutes_str}:{seconds_mod_str}"

    return f"{title}  {time_str}"

