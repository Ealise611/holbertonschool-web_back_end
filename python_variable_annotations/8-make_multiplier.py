#!/usr/bin/env python3
"""
Write a type-annotated function make_multiplier that
takes a float multiplier as argument and
returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function take float and return a function
    """
    def mul(a: float) -> float:
        """
        function to do a * multiplier
        """
        return a * multiplier
    return mul
