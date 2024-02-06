#!/usr/bin/python3
""" a function that writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """ The function then returns the number of char... written"""
    line_number = 0
    with open(filename, mode='w+', encoding='utf-8') as a_file:
        for a_line in a_file:
            line_number += 1
    return line_number
