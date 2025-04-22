"""
Module for input handling routines
"""

def split_input(input_lines: list, sep='') -> list[list]:
    '''This function will split the input_lines in different sections using the
     sep string as seperator (default is empty line).'''
    result = []

    while sep in input_lines:
        i = input_lines.index(sep)
        result.append(input_lines[0:i])
        input_lines = input_lines[i+1:]

    result.append(input_lines)

    return result