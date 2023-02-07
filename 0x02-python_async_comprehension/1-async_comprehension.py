#!/usr/bin/env python3
""" comprehesions wth async"""

import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ collects 10 random numbers using async comprehension"""
    return [i async for i in async_generator()]
