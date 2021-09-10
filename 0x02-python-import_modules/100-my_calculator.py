#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    count = len(sys.argv)
    if count != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    op = sys.argv[2]

    def not_found():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    options = {
        "+": "{} + {} = {}".format(num1, num2, add(num1, num2)),
        "-": "{} - {} = {}".format(num1, num2, sub(num1, num2)),
        "*": "{} * {} = {}".format(num1, num2, mul(num1, num2)),
        "/": "{} / {} = {}".format(num1, num2, div(num1, num2))
        }

    if op in options.keys():
        print(options[op])
    else:
        not_found()
