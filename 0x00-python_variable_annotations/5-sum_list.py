#!/usr/bin/env python3

""" Defines a type annotated function sum_list"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
         a type-annotated function which takes
         param: (a list input_list of floats)
            and
        returns: their sum as a float.
    """

    return sum(input_list)
