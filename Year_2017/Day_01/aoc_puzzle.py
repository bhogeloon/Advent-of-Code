"""
Year 2017, Day 1

Problem description: See https://adventofcode.com/2017/day/1

<Include solution description>

"""

# Imports
from pprint import pprint


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Captcha():
    '''Circular structure of Digit objects'''
    def __init__(self, line: str) -> None:
        self.first_digit = Digit(line[0])

        for (i,digit) in enumerate(line):
            pass



class Digit():
    '''Object containing digit and next (pointer to next objec)'''
    def __init__(self, digit: str) -> None:
        self.digit = digit


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    captcha = Captcha(lines[0])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
