#!/usr/bin/env python3
"""This is the redis exercise file""""

import redis
import uuid
from typing import Union


class Cache:
    """This is the redis class"""

    def __init__(self):
        """This is the constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This is going to create a random key
        and save it nd return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
