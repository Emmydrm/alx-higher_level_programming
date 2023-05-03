#!/usr/bin/python3
"""
sends a param via post request and
check if the response body is a valid
json
"""
import requests
import sys


if __name__ == "__main__":
    if (len(sys.argv) == 2):
        param_data = {'q': sys.argv[1]}
    else:
        param_data = {'q': ""}
    res = requests.post("http://0.0.0.0:5000/search_user", data=param_data)
    try:
        json = res.json()
        if (len(json) == 0):
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except Exception as exception:
        print("Not a valid JSON")
