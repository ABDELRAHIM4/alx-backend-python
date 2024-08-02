#!/usr/bin/env python3
from typing import Callable
""" type-annotated function make_multiplier that takes a float"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function make_multiplier that takes a float"""
    def multiply(x: float) -> float:
        return (x * multiplier)
    return (multiply)
