#!/usr/bin/env python3
"""This is the redis exercise file"""

import redis
import uuid
import typing


class Cache:
    """This is the redis class"""

    def __init__(self):
        """This is the constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """This is going to create a random key
        and save it nd return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: typing.Optional[typing.Callable] = None) -> typing.Union[
                    str, bytes, int, float]:
        """Thisi s the get function to get a key"""
        val = self._redis.get(key)
        if fn is not None and val is not None:
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        """this function is used to get strings"""
        val = self.get(key, fn=lambda x: x.decode())
        return val

    def get_int(self, key: str) -> int:
        """This function is used to get integers"""
        val = self.get(key, fn=int)
        return val
