#!/usr/bin/python3
"""sends a request to the github api to retrieve a users id"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    res = requests.get("https://api.github.com/user", auth=(username, token))
    print(res.json().get('id'))
