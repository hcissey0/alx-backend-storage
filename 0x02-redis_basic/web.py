#!/usr/bin/env python3
"""This is the web redis"""

import requests
import redis
import typing
from functools import wraps


red = redis.Redis()


def count_call(method: typing.Callable) -> typing.Callable:
    """This is used to count the number of funcion calls"""
    @wraps(method)
    def wrapp(*args, **kwargs):
        red.incr(f"count:{args[0]}")
        return method(*args)
    return wrapp


def cache_page(method: typing.Callable) -> typing.Callable:
    """Thisis used to cache th apge"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        page = red.get(args[0])
        if page is not None:
            return page.decode('utf-8')
        else:
            page = method(*args)
            red.setex(args[0], 10, page)
            return page
    return wrapper


@count_call
@cache_page
def get_page(url: str) -> str:
    """Thisisi the function that gets the page"""
    return requests.get(url).text
