#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST
"""
import sys
import responses


if __name__ == "__main__":
    if len(sys.argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": sys.argv[1]}

    req = responses.get(url, data=data)

    try:
        content = req.json()
        if content == {}:
            print("No result")
        else:
            print("[{}] {}".format(content.get("id"), content.get("name")))
    except ValueError:
        print("Not a valid JSON")
