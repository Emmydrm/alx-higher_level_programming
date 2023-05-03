#!/usr/bin/python3
"""Sends a request to a URL and handles urllib.error.HTTPError"""
import urllib.request
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content = response.read()
            print("{}".format(content.decode('utf-8')))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
