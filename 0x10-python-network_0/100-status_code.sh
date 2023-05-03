#!/bin/bash
# Get response status code without piping
curl -s -o /dev/null -I -w "%{http_code}" "$1"
