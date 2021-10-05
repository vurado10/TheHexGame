from typing import List


def execute_all_funcs(funcs: List, *args, **kwargs):
    for func in funcs:
        func(*args, **kwargs)