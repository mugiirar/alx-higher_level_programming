#!/usr/bin/python3
"""request header
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    headers = dict(req.headers)
    idd = headers.get("X-Request-Id")
    print(idd)
