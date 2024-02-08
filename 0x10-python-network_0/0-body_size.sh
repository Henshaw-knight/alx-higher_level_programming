#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response
size=$(curl -X GET -s -o /dev/null -w "%{size_download}" "$1")
echo "$size"
