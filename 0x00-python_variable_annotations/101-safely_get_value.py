#!/usr/bin/env python3
""" Add type annotations to safely_get_value looking at the output"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """" Duck typing """
    if key in dct:
        return dct[key]
    else:
        return default
