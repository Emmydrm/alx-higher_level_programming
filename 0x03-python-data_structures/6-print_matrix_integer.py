#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
        matrix: Matrix of integers
    """
    if not matrix[0]:
        print()

        for i in matrix:
            for j in i:
                if i.index(j) == (len(i) - 1):
                    # if item is the last element
                    print("{:d}".format(j))
                else:
                    print("{:d}".format(j), end=" ")
