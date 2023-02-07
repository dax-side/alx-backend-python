#!/usr/bin/env python3
""" measure runtime """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ executes comprehesion coroutine 4 times in parallel
        measure and return the total runtime
    """
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
