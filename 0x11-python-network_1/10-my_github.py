#!/usr/bin/python3
"""github"""
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]

    url = "https://api.github.com/users/" + user

    req = requests.get(url)

    ans = dict(req.json())

    print(ans.get("id"))
