#!/usr/bin/env python3
"""measures time of async comprehension"""
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function that performs time measurement
    of the async comprehension function"""
    start_time = time.time()
    await async_comprehension()
    end_time = time.time()
    total_time = (end_time - start_time)

    return total_time
