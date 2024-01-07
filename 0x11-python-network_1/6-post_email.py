#!/usr/bin/python3
"""Python script that takes in a URL and an email address
"""
import sys
import requests


if __name__ == "__main__":

    url = sys.argv[1]

    data = {"email" : sys.argv[2] }

    req = requests.post(url, data=data)

    print(req.text)


