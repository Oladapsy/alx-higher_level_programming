#!/usr/bin/python3
""" a Python script that takes in a URL,
sends a request to the URL
and displays the body of the response."""
import sys
import requests


if __name__ == "__main_":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)
