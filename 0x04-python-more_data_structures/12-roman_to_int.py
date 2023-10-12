#!/usr/bin/python3
def to_subtract(list_num):
    max_num = max(list_num)
    return max_num - sum(n for n in list_num if n < max_num)

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    last_rom = 0

    for i in roman_string:
        if i in rom_n:
            if rom_n[i] <= last_rom:
                num += to_subtract([rom_n[i]])
            else:
                num += rom_n[i]
            last_rom = rom_n[i]

    return num
