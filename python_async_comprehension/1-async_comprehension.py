#!/usr/bin/env python3

async_generator = __import__('0-async_generator').async_generator
"""Async Comprehensions"""
from typing import List

async def async_comprehension() -> List[int]:
    """Async Comprehensions"""
    result = [i async for i in async_generator()]
    return result
