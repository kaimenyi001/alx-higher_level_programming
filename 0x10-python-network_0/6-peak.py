#!/usr/bin/python3
""" Finds a peak inside a list of unsorted integers """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    mid = int(length / 2)
    loi = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return loi[mid]
    elif mid - 1 < 0:
        return loi[mid] if loi[mid] > loi[mid + 1] else loi[mid + 1]
    elif mid + 1 >= length:
        return loi[mid] if loi[mid] > loi[mid - 1] else loi[mid - 1]

    if loi[mid - 1] < loi[mid] > loi[mid + 1]:
        return loi[mid]

    if loi[mid + 1] > loi[mid - 1]:
        return find_peak(loi[mid:])
    return find_peak(loi[:mid])
