#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
"""an async routine called wait_n that takes in 2 int arguments """


async def wait_n(n, max_delay) -> float:
    """an async routine called wait_n that takes in 2 int arguments """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*tasks)
    return (sorted(delay))
