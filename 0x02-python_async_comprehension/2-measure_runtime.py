#!/usr/bin/env python3
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension
"""write a measure_runtime coroutine that will execute async"""


async def measure_runtime():
    """write a measure_runtime coroutine that will execute aync"""
    start_time = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = time.perf_counter()
    run_time = end_time - start_time
    return (run_time)
