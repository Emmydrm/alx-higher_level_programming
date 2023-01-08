#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string

    Args:
        my_string: string of characters

        Returns:
            new string
        """

        new-string = ""

        # iterate through my_string
        for char in my_string:
            if char == 'c' or char == 'C':
                # remove all c, C by skipping them
                continue
            # append new string
            new_string = new_string + char

        return new_string
