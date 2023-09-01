#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""

import requests
from sys import argv

if __name__ == "__main__":
    letters = "" if len(argv) == 1 else argv[1]
    payload = {"q": letters}
    url = "http://0.0.0.0:5000/search_user"

    req = requests.post(url, data=payload)
    try:
        html = req.json()
        if html == {}:
            print('No result')
        else:
            print("[{}] {}".format(html.get("id", html.get("name")))
    except ValueError:
        print("Not a valid JSON")
