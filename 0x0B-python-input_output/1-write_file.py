#!/usr/bin/python3
"""write_file with two arguments"""


def number_of_lines(filename="", text=""):
    """reads file with utf-8"""
    with open(filename, "w", encoding='UTF-8') as f:
        return f.write(text)
