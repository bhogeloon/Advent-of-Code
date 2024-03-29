"""
Year 2016, Day 2

Problem description: See https://adventofcode.com/2016/day/2

<Include solution description>

"""

# Imports
from pprint import pprint
import numpy as np


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Keypad():
    '''This is the keypad containing the numbers 1 to 9 in a matrix form.
    It has addtional attributes cur_x and cur_y to indicate the current position'''
    def __init__(self) -> None:
        self.keys = np.full((3,3), None)
        # Fill the keypad with numbers 1 to 9
        fill_nr = 1
        for y in range(3):
            for x in range(3):
                self.keys[x,y] = fill_nr
                fill_nr += 1

        # Set current key to 5 (middle one)
        self.cur_x = 1
        self.cur_y = 1


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    keypad = Keypad()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
