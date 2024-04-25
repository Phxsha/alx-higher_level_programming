#!/bin/bash
# Sends a GET request to the URL passed as the first argument, with X-School-User-Id header set to 98, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
