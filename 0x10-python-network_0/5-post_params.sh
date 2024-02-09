#!/bin/bash
# Script that takes in a URL, sends a POST request and displays the response body
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
