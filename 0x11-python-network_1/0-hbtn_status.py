#!/usr/bin/env python3
import urllib.request

""" Python script that fetches https://alx-intranet.hbtn.io/status"""

url = 'https://alx-intranet.hbtn.io/status'

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    the_page = response.read()

print (the_page)
