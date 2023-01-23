#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    length = len(roman_string)
    lengt = length - 1
    number = 0
    i = 0
     while i < length:
        if i < lengt and roman[roman_string[i]] < roman[roman_string[i + 1]]:
            number += roman[roman_string[i + 1]] - roman[roman_string[i]]
            i += 1
        else:
            number += roman[roman_string[i]]
        i += 1
     return number
