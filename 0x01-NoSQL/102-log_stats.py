#!/usr/bin/env python3
"""Thisis the advanced status log"""

from pymongo import MongoClient


cli = MongoClient('mongodb://localhost:27017')

db = client['logs']
nginx_col = db['nginx']


