#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specified position
    without modifying the original list

    Args:
        my_list: list of elements
        idx: index of element to be replaced
        element: new element

        Returns:
            A copy of my_list
        """

        new_list = my_list[:]

        if idx < 0:
            return new_list
        if idx > (len(my_list) - 1):
            # idx is out of range
            return new_list

        new_list[idx] = element
        return new_list
