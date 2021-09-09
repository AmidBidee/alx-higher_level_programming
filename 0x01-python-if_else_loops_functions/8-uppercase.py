#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    ustr = str
    for i in range(len(ustr)):
        if islower(ustr[i]):
            un = ord(ustr[i]) - 32
            uc = chr(un)
            ustr = ustr.replace(ustr[i], uc)
    return print(ustr)
