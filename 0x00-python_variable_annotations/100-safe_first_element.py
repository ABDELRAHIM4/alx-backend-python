#!/usr/bin/env python3
from typing import Sequence, Union, Any
"""Augment the following code with the correct duck-typed annotation"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, type(None)]:
    """Augment the following code with the correct duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
