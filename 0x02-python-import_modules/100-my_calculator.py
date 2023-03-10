#!/usr/bin/python3#!

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])

        # Check operator and call relative function
        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = sub(a, b)
        elif operator == "*":
            result = mul(a, b)
        elif operator == "/":
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
