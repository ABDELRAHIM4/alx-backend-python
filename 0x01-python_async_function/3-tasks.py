#!/usr/bin/env python3
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


"""task_wait_random that takes an integer"""
def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random that takes an integer"""
    task = asyncio.create_task(wait_random(max_delay))
    return (task)
