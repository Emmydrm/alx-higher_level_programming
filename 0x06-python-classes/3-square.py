#!/usr/bin/python3
"""Creates a square

    Attributes:
        Square (class): a class that creates a square
    """


    class Square:
        """A Square class with validated private instance attribute size

        Args:
            size (int): size of square
        """

        def __init__(self, size=0):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

        def area(self):
            """Area of Square

            Returns:
                size ** 2
            """
            return self.__size ** 2
