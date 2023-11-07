#!/usr/bin/python3
"""
Reads from standard input line by line and computes metrics
"""


if __name__ == "__main__":
    import sys

    stdin = sys.stdin

    d = 0
    size = 0
    p_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    m = {}

    try:
        for i in stdin:
            if d == 10:
                print("File size: {}".format(size))
                for j in sorted(st):
                    print("{}: {}".format(j, m[j]))
                d = 1
            else:
                d = d + 1

            i = i.split()

            try:
                size = size + int(i[-1])
            except (IndexError, ValueError):
                pass

            try:
                if i[-2] in p_codes:
                    if m.get(i[-2], -1) == -1:
                        m[i[-2]] = 1
                    else:
                        m[i[-2]] = m[i[-2]] + 1
            except IndexError:
                pass

        print("File size: {}".format(size))
        for j in sorted(m):
            print("{}: {}".format(j, m[j]))

    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for j in sorted(m):
            print("{}: {}".format(j, m[j]))
        raise
