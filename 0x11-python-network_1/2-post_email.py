#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        content = response.read()
        ans = content.decode("utf-8")
        print (ans)
