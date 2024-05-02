#!/usr/bin/python3
"""The Holberton School staff evaluates candidates applying
for a back-end position with multiple technical challenges,
like this one:
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://developer.github.com/v3/repos/{}/{}/commits/".format(
            sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
