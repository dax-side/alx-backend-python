#!/usr/bin/env python3
""" Defines a type annotated function make_multiplier"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
        Write a type-annotated function make_multiplier that takes
        param: (multiplier: float)
            and
        returns: a function that multiplies a float by multiplier
    """

    return (lambda x: x * multiplier)
