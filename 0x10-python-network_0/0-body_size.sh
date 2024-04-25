#!/bin/bash
# This script takes a URL, sends a request, and displays the size of the response body

# Send a GET request to the URL and store the response body in a temporary file
curl -s -o temp_body.txt "$1"

# Get the size of the response body in bytes and display it
cat temp_body.txt | wc -c

# Clean up temporary file
rm temp_body.txt
