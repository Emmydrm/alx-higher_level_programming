#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns all multiples of 2 in a list

    Args:
        my_list: list of integers

        Returns:
            a list of True or False
        """

        if len(my_list) == 0:
            return my_list

        new_list = []
        for i in my_list:
            if i % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)

        return new_list
