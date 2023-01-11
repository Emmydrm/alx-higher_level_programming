#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = None
    denominator = None
    for tuple in my_list:
        if denominator is None:
            denominator = tuple[-1]
        else:
            denominator += tuple[-1]

        mult = 1
        for i in tuple:
            mult *= i

        if numerator is None:
            numerator = mult
        else:
            numerator += mult

     return numerator / denominator
