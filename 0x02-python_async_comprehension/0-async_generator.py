#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments"""
import random
import asyncio
"""coroutine called async_generator that takes no arguments"""


async def async_generator():
    """coroutine called async_generator that takes no arguments"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
