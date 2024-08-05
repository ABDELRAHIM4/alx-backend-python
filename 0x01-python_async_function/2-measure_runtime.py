#!/usr/bin/env python3
import time
import asyncio
"""measure_time function with integers n and max_delay"""
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time function with integers n and max_delay"""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    elap = end_time - start_time
    return (elap / n)
