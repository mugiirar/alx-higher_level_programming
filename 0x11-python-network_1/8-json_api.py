#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    arg = {"q": letter}
    
    url = "http://0.0.0.0:5000/search_user"

    req = requests.post(url, data=arg)

    try:
        content = req.json()
        if content == {}:
            print("No result")
        else:
            print("[{}] {}".format(content.get("id"), content.get("name")))
    except ValueError:
        print("Not a valid JSON")
