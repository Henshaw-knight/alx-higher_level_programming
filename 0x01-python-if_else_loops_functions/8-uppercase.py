#!/usr/bin/python3
def uppercase(str):
    length = len(str) - 1
    for i in str:
        if (ord(i) in range(97, 123)):
            i = chr(ord(i) - 32)
        if (length != 0):
            print("{}".format(i), end="")
        else:
            print("{}".format(i))
        length -= 1
