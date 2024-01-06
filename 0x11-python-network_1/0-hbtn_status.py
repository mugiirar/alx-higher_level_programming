#!/usr/bin/env python3
import urllib.request

""" Python script that fetches https://alx-intranet.hbtn.io/status"""


req = urllib.request.Request("https://alx-intranet.hbtn.io/status")

with urllib.request.urlopen(req) as response:
    content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode("utf-8")))
