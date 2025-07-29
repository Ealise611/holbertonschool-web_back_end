#!/usr/bin/env python3
"""
annotate below function
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function to return items in list
    """
    return [(i, len(i)) for i in lst]
