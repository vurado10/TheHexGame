from typing import List


def execute_all_funcs(funcs: List, *args, **kwargs):
    for func in funcs:
        func(*args, **kwargs)


def get_min_max(elements, key=None):
    min_e, max_e = (min(elements, key=key),
                    max(elements, key=key))

    return min_e, max_e

