#!/usr/bin/env python3

""" Defines a type annotated function sum_mixed_list"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
        a type-annotated function which takes a
        param: (list mxd_lst of integers and floats)
            and
        returns: their sum as a float.
    """
    return float(sum(mxd_lst))
