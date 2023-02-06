#!/usr/bin/env python3
""" defines a measure time function"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        measures the total execution time for wait_n.
    """
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(wait_n(n, max_delay))
    loop.close()
    end = time.time()
    total_time = end - start
    return total_time / n
