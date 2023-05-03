#!/bin/bash
# Displays all HTTP methods the server will accecpcurl -X HEAD -s "$1"
curl -sX OPTIONS "$1" -i | grep -i Allow:| awk '{$1=""; sub(/^[ \t]+/, ""); print}'
