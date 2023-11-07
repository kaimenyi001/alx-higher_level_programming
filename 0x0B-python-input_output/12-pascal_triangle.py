#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """
    Function that returns the pascal triangle
    """

    triangle = []
    tri = []

    for i in range(n):
        my_list = []
        r1 = -1
        r2 = 0
        for j in range(len(tri) + 1):
            if r1 == -1 or r2 == len(tri):
                my_list += [1]
            else:
                my_list += [tri[r1] + tri[r2]]
            r1 += 1
            r2 += 1
        triangle.append(my_list)
        tri = my_list[:]

    return triangle
