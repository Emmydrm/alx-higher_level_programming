#!/usr/bin/python3
for c in "abcdefghijklmnopqrstuvwxyz":
    if c == "e" or c == "q":
        continue
    print("{}".format(c), end="")
