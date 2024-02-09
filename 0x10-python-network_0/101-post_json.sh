#!/bin/bash
# Bah script that sends a JSON POST request to a URL passed as the first arument, the filename is passed as a second argument
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
