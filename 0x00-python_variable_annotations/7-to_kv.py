#!/usr/bin/env python3
from typing import Union
"""type-annotated function to_kv that takes a string k"""


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """type-annotated function to_kv that takes a string k"""
    return (k, float(v) **2)
