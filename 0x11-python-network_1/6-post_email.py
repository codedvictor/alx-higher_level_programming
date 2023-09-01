#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in
the response header"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    val = {
            'email': argv[2]
            }

    html = requests.post(url, data=val)

    print("Your email is: {}".format(html.text))
