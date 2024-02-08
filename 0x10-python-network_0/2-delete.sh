#!/bin/bash
# Script that sends a DELETE request to the URL passed as the first argument and displays the request body
curl -s -X DELETE "$1"
