#!/bin/bash
#sends a post request using curl
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
