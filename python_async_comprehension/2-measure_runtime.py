#!/usr/bin/env python3
"""
Import async_comprehension from the previous file
and write a measure_runtime coroutine
that will execute async_comprehension
four times in parallel using asyncio.gather.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime measure the total runtime and return it.
    """
    start = time.perf_counter()
    # tasks = [async_comprehension() for _ in range(4)]
    # result = await asyncio.gather(*tasks)
    # above are easier way to read
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    total_time = time.perf_counter() - start
    return total_time
