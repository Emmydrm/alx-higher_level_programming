#!/bin/bash
# sends a custom header variable
curl -s -H "X-School-User-Id: 98" "$1"
