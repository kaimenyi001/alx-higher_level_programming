#!/usr/bin/python3
"""
A text-indentation function
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    t = text[:]

    for j in ".?:":
        list_text = t.split(j)
        t = ""
        for i in list_text:
            i = i.strip(" ")
            t = i + j if t is "" else t + "\n\n" + i + j

    print(t[:-3], end="")
