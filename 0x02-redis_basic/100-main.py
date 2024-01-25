#!/usr/bin/env python3

import redis


red = redis.Redis()
get_page = __import__('web').get_page

url = 'http://slowwly.robertomurray.co.uk'

print(get_page(url))
print(red.get(f'count:{url}'))
