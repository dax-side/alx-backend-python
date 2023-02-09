#!/usr/bin/env python3
""" annotate a funciton and add documentation"""
from typing import Sequence, Any, Union
import typing


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> typing.Union[Any, type(None)]:
    """return a list if argument is a list
        else return None
    """
    if lst:
        return lst[0]
    else:
        return None
