#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
if __name__ == "__main__":
    result = 0
    i = 1
    while i <= argc:
        result += int(argv[i])
        i += 1
    print("{:d}".format(result))    
