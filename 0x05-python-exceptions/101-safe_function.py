#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as msg:
        print("Exception: {}".format(msg), file=sys.stderr)
        return None
