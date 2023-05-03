#!/usr/bin/python3
"""Accepts URL as a parameter, fetches it, and displays X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print("{}".format(res.headers.get('X-Request-Id')))
