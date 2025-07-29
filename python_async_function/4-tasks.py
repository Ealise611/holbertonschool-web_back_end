#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n
except task_wait_random is being called.
"""

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    function to run n times of wait_random
    and return a sorted list of float"""
    delays = []
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
