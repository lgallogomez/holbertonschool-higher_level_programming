#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except Exception:
        c = None
        print("Inside result: {}".format(c))
        return (c)
    finally:
        if c is not None:
            print("Inside result: {:.1f}".format(c))
            return (c)
