#!/usr/bin/python3
"""
displays the body of the response
or the error if the HTTP status code
is above 300
"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    code = res.status_code
    if (code >= 400):
        print("Error code:", code)
    else:
        print(res.text)
