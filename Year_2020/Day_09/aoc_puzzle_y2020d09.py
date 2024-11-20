"""
Year 20xx, Day xx

Problem description: See https://adventofcode.com/20xx/day/xx

<Include solution description>

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import RootLogger

# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False

    # Variable that will be used for holding the logger object
    log = None


# Classes


# Functions

def define_global_variables(
        test=False, 
        logger:RootLogger|None=None,
        **kwargs,
    ) -> None:
    '''Standard function to define the Gv class variables'''
    Gv.test = test
    Gv.log = logger


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    define_global_variables(**kwargs)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    define_global_variables(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
