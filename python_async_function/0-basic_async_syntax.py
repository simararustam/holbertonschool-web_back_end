#!/usr/bin/env python
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay: float = 10):
    """Basics of asyn"""

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(random.uniform(0, max_delay))
    return delay
