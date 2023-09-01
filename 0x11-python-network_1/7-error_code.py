#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    req = requests.get(url)
    html = req.status_code
    if html >= 400:
        print('Error code: {}'.format(html))
    else:
        print(req.text)
