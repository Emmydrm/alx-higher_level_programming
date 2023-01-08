#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its
        first character

    Args:
        sentence: a string
    Returns:
        length of a string and its first letter
    """

    length = len(sentence)

    if length == 0:
        first_letter = None
    else:
        first_letter = sentence[0]

    return length, first_letter
