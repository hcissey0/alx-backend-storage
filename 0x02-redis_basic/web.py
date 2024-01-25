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
    def wrapp(url):
        red.incr(f"count:{url}")
        return method(url)
    return wrapp


def cache_page(method: typing.Callable) -> typing.Callable:
    """Thisis used to cache th apge"""
    @wraps(method)
    def wrapper(url):
        page = red.get(url)
        if page is not None:
            return page.decode('utf-8')
        else:
            page = method(url)
            red.setex(url, 10, page)
            return page
    return wrapper


@count_call
@cache_page
def get_page(url: str) -> str:
    """Thisisi the function that gets the page"""
    return requests.get(url).text


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
