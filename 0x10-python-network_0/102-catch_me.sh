#!/bin/bash
# Script that causes the server to respond with a message containing
curl -sL -X PUT -H "Origin:HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
