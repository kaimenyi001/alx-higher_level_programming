#!/bin/bash
# Script that sends a JSON POST request and displays the response.
curl -s -H "Content-Type: application/json" -d "$(cat $2)" "$1"
