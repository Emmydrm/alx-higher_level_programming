#!/bin/bash
# Send a GET request to the provided URL with a header variable X-School-User-Id set to 98 using
curl -sH "X-School-User-Id: 98" "$1"
