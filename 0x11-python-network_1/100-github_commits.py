#!/usr/bin/python3
"""aa Python script that takes 2 arguments in
order to solve this challenge"""

import requests
from sys import argv

if __name__ == "__main__":
    repo_name = argv[1]
    own_name = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
            own_name, repo_name)

    req = requests.get(url)
    commit = req.json()
    try:
        for x in range(10):
            print("{}: {}".format(
                commit[x].get("sha"),
                commit[x].get("commit").get("author").get("name")))
    except IndexError:
        pass
