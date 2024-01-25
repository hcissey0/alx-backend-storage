#!/usr/bin/env python3

Web = __import__('web').Web

web = Web()
url = 'http://slowwly.robertomurray.co.uk'
text = web.get_page(url)
print(text)

print(web._redis.get(f'count:{url}'))
