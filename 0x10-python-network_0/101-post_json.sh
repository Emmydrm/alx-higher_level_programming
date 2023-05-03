#!/bin/bash
# Send json post request
curl -sX POST -H 'Content-Type: application/json' -d "$(<"$2")" "$1"
