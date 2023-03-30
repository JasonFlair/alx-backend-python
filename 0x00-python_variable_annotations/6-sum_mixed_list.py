#!/usr/bin/env python3
"""returns sum of floats and ints as a float"""
import typing

from typing import List


def sum_mixed_list(mxd_list: List[typing.Union[float, int]]) -> float:
    sumofmixedlist: float = 0
    for num in mxd_list:
        sumofmixedlist += num
    return sumofmixedlist
