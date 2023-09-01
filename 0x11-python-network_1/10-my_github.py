#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    name = argv[1]
    psword = argv[2]
    authkey = HTTPBasicAuth(name, psword)

    url = "https://api.github.com/user"

    req = requests.post(url, auth=authkey)
    html = req.json()
    print(html.get("id"))
