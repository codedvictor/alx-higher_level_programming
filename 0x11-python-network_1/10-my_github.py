#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    name = argv[1]
    password = argv[2]
    authkey = HTTPBasicAuth(name, password)

    url = "https://api.github.com/user"

    req = requests.get(url, auth=authkey)
    user = req.json()
    userId = user.get("id")
    print(userId)
