#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    arg_len = len(sys.argv)
    if arg_len > 1:
        s = 0
        for i in range(arg_len):
            if i != 0:
                s += int(sys.argv[i])
        print("{}".format(s))
