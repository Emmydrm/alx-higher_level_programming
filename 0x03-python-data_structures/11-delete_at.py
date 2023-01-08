#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list

    Args:
        my_list: list of items
        idx: index of item to be deleted

    Returns:
        return new list
    """

    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    item = my_list[idx]
    my_list.remove(item)
    return my_list
