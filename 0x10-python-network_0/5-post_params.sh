#!/bin/bash
# Sends a POST request to the URL passed as the first argument, with email and subject parameters, and displays the body of the response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
