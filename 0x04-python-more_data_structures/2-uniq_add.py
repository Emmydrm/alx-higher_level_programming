#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    result = 0

    for i in uniq:
        result += i

    return result
