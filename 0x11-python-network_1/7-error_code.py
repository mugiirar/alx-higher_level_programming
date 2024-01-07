#!/usr/bin/python3
"""Python script that takes in a URL
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.status_code)
