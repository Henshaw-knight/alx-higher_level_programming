#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a  "You got me!" message in the response body
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
