#!/bin/bash
# a Bash script that sent POST request to the URL, displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
