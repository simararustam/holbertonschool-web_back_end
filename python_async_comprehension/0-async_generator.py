#!/usr/bin/env python3
import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields random floating-point numbers.

    This coroutine asynchronously yields 10 random floating-point numbers,
    each between 0 and 10. It waits for 1 second between each yield.

    Yields:
        float: A random floating-point number between 0 and 10.

    Example:
        async for number in async_generator():
            print(number)
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
