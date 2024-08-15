#!/usr/bin/env python3
"""Complex types - list of floats"""


def sum_list(input_list: list[float]) -> float:
    """Returns their sum as a float"""

    sum: float = 0
    for i in input_list:
        sum += i
    return sum
