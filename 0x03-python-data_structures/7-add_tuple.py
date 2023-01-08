#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples together

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        A tuple with two integers
    """

    list_a = list(tuple_a)
    list_b = list(tuple_b)
    new_list = []

    # check length of list_a
    if len(list_a) == 0:
        list_a.append(0)
        list_a.append(0)
    elif len(list_a) == 1:
        list_a.append(0)
    # check length of list_b
    if len(list_b) == 0:
        list_b.append(0)
        list_b.append(0)
    elif len(list_b) == 1:
        list_b.append(0)

    new_list.append(list_a[0] + list_b[0])
    new_list.append(list_a[1] + list_b[1])
    new_tuple = tuple(new_list)

    return new_tuple
