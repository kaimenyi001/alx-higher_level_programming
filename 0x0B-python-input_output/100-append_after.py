#!/usr/bin/python3
"""
Module of a function that inserts a line of text to a file,
after each line containing a specific string 
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that appends a new line when a string is found
    """

    new_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            new_line += [line]
            if line.find(search_string) != -1:
                new_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(new_line))
