#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the body of the response
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.arv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            ans = response.read().decode("ascii")
            print (ans)
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
