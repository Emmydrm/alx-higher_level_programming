#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    new_str = ""
    i = 0
    while i < n:
        new_str = new_str + str[i]
        i += 1
    i = n + 1
    while i < len(str):
        new_str = new_str + str[i]
        i += 1
    return new_str
