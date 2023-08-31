#!/bin/bash
# a Bash script that sent request to the URL, displays the allowed HTTP method
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
