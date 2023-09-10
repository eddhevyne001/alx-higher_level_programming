#!/usr/bin/python3
def no_c(my_string):

    strings = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            strings += my_string[i]
    return strings
