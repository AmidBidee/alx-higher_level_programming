#!/usr/bin/python3


def islower(c):
    if ord(c) >= 97 <= 122:
        return True
    False


def uppercase(str):
    ustr = str
    for i in range(len(ustr)):
        if islower(ustr[i]):
            un = ord(ustr[i]) - 32
            uc = chr(un)
            ustr = ustr.replace(ustr[i], uc)
    print(ustr)
