#!/bin/bash
# Script that takes in a URL as an arugment, sends a GET request, a header variable is also sent with a value
curl -s -H "X-School-User-Id: 98" "$1"
