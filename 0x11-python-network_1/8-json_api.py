#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
"""
import sys
import requests


if __name__ == "__main__":
    if sys.argv[1] == None:
        info = {"q" : ""}

    else:
        info = {"q" : sys.argv[1] }

    url = "http://0.0.0.0:5000/search_user"

    req = request.post(url, data=info)

    try:
        cont = req.json()
        if cont == {}:
            print("Not a valid JSON")
        else:
            print("[{}] {}".format(cont.get("id"), cont.get("name"))

    except ValueError:
        print("Not a valid JSON")
