#!/bin/bash
# a Bash script that sent POST request to the URL, displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
