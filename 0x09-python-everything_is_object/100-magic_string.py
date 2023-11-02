#!/usr/bin/python3
    setattr(magic_string, "i", getattr(magic_string, "i", -1) + 1)
    return "BestSchool" + ", BestSchool" * getattr(magic_string, "i", 0)
