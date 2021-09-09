#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    arg_len = len(sys.argv)
    if arg_len > 1:
        if arg_len == 2:
            print("{0} argument:\n{0}: {1}".format(arg_len - 1, sys.argv[1]))
        else:
            print("{} arguments:".format(arg_len - 1))
            for i in range(arg_len):
                if i != 0:
                    print("{}: {}".format(i, sys.argv[i]))
    else:
        print("0 arguments.")
