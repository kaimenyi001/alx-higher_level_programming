#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    while True:
        try:
            if c < x:
                print(my_list[c], end='')
                c += 1
            else:
                print()
                return c
        except IndexError:
            print()
            return (c)
