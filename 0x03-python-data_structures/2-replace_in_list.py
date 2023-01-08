#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at specific position

    Args:
        my_list: list of items
        idx: index of item to be replaced
        element: new element to be used

        Returns:
            Updated list
        """

        if idx < 0:
            return my_list
        if idx > (len(my_list) - 1):
            # idx is out of range
            return my_list

        my_list[idx] = element
        return my_list
