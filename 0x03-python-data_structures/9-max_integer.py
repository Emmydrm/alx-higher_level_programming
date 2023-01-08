#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer in a list

    Args:
        my_list: list of integers

        Returns:
            the biggest integer
        """

        if len(my_list) == 0:
            return None

        for i in my_list:
            if my_list.index(i) == 0:
                max = i
            if i > max:
                max = i

        return max
