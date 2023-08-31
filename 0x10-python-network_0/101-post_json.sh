#!/bin/bash
# a Bash script that sent JSON POST request to the URL
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
