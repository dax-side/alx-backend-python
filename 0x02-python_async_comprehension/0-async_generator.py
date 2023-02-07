#!/usr/bin/env python3
""" Defines a coroutine called async_generator that takes no arguments."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        loops 10 times and asynchronously wait 1 second,
        then yield a random number between 0 and 10.
    """

    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
