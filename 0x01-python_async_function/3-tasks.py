#!/usr/bin/env python3
""" defines a regular function"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """regular function that takes int argument
        and returns asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
