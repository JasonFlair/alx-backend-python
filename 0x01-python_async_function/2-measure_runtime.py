#!/usr/bin/env python3
"""measure_time function with integers
n and max_delay as arguments"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: float) -> float:
    """async function to solve the task"""
    start_time = time.time()
    await asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = (end_time - start_time)
    per_n_time = total_time / n
    return per_n_time
