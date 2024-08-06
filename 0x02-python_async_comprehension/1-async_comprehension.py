#!/usr/bin/env python3
import asyncio
async_generator = __import__('0-async_generator').async_generator
"""write a coroutine called async_comprehension that takes no arguments"""


async def async_comprehension():
    """write a coroutine called async_comprehension that takes no arguments"""
    return [i async for i in async_generator()]
