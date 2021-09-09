#!/usr/bin/python3
def uppercase(str):
    ustr = str
    for i in range(len(ustr)):
        if ord(ustr[i]) >= 97 <= 122:
            uc = chr(ord(ustr[i]) - 32)
            ustr = ustr.replace(ustr[i], uc)
    print("{}".format(ustr))
