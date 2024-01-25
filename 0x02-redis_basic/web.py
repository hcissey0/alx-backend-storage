#!/usr/bin/env python3
"""This is the web redis"""

import requests
import redis
import typing
from functools import wraps


def count_calls(method: typing.Callable) -> typing.Callable:
    """This is used to count the number of funcion calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(f"count:{args[0]}")
        return method(self, *args, **kwargs)
    return wrapper


def cache_page(method: typing.Callable) -> typing.Callable:
    """Thisis used to cache th apge"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        page = self._redis.get(args[0])
        if page is not None:
            return page.decode('utf-8')
        else:
            page = method(self, *args, **kwargs)
            self._redis.setex(args[0], 10, page)
            return page
    return wrapper


class Web:
    """This is the web cache class"""

    def __init__(self):
        """The initializor"""
        self._redis = redis.Redis()

    @count_calls
    @cache_page
    def get_page(self, url: str) -> str:
        """Thisisi the function that gets the page"""
        return requests.get(url).text
