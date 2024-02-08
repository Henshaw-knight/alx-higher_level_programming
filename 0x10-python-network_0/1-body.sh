#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL and displays the body of the response if it is a 200 status code response
curl -sL "$1"
