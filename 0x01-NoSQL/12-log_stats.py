#!/usr/bin/env python3
"""thisisi use to log status"""

from pymongo import MongoClient


if __name__ == "__main__":
    cli = MongoClient('mongodb://127.0.0.1:27017')
    logs = cli.logs.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print(f'{logs.count_documents({})} logs')

    print('Methods:')
    for meth in methods:
        print(f'\tmethod {meth}: {logs.count_documents({"method": meth})}')

    print(f'{logs.count)_documents({"method": "GET", "path": "/status"})} status check')
