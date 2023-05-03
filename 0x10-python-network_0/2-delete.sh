#!/bin/bash

# Check if URL is provided as argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 URL"
  exit 1
fi

# Send a DELETE request to the provided URL using curl, and display the response body
curl -s -X DELETE "$1"

# Add a newline after the response body for readability
echo ""
