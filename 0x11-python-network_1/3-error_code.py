#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""

import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as err:
        html = err.code
        print('Error code:'.format(html.decode("utf-8")))
