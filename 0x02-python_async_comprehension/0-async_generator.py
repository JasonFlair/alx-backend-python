#!/usr/bin/env python3
"""an async generator"""
import asyncio
import typing
import random


async def async_generator() -> typing.List['float']:
    """async generator that yields random numbers"""
    for i in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
