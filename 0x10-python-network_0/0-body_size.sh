#!/bin/bash
# This script takes a URL, sends a request, and displays the size of the response body

# Send a GET request to the URL, discard header, and get the size of the body
curl -s -o /dev/null -w '%{size_download}' "$1"
