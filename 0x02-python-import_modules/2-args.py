#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1

    if argc == 0:
        """0 arguments"""
        print("0 arguments.")
    elif argc == 1:
        """1 argument"""
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    else:
        """Multiple arguments"""
        print(f"{argc:d} arguments:")
        i = 1
        while i <= argc:
            print(f"{i:d}: {argv[i]:s}")
            i += 1
