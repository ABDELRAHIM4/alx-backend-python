#!/usr/bin/env python3
import asyncio
from typing import List
import heapq
wait_random = __import__('0-basic_async_syntax').wait_random
"""an async routine called wait_n that takes in 2 int arguments """


async def wait_n(n: int, max_delay: int) -> List[float]:
    """an async routine called wait_n that takes in 2 int arguments """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay = []
    for task in asyncio.as_completed(tasks):
        heapq.heappush(delay, await task)
    return (delay)
