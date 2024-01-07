#!/usr/bin/python3
"""git hub commits
"""
import sys
import requests


if __name__ == "__main__":
    user = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/"+ user + "/" + repo +"/commits/"

    req = responses.get(url)

    comits = req.json()


    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
