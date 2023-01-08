#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list

    Args:
        my_list: list of where item should be retrieved from
        idx: index of element to be retrieved

    Returns:
        Element at idx in my_list
    """

    if idx < 0:
        return None
    if idx > (len(my_list) - 1):
        # idx is out of range
        return None

    return my_list[idx]
