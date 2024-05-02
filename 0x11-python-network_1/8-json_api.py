#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = {'q': ""}
    else:
        letter = {'q': sys.argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            j_id = response.get('id')
            name = reponse.get('name')
            print(f"[{j_id}] {name}")
    except ValueError:
        print("Not a valid JSON")
