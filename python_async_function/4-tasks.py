#!/usr/bin/env python3
"""Tasks"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 1) -> List[float]:
    """basic async"""
    delays: List[float] = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
