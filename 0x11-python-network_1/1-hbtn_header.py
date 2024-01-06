#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id"""

import sys
import urllib.request

url = sys.argv[1]

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    content = dict(response.headers)
    req_num = content.get("X-Request-Id")
    print(req_num)
