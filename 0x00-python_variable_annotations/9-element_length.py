#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
"""Annotate the below function’s parameters"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the below function’s parameters"""
    return [(i, len(i)) for i in lst]
