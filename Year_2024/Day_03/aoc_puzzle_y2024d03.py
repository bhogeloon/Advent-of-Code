"""
Year 2024, Day 3

Problem description: See https://adventofcode.com/2024/day/3

No classes are used.

Part 1: Extract all the mul statements from the string and multiply the
numbers. Add everything up.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
import re

# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False

    # Variable that will be used for holding the logger object
    log = None

    def __init__(self, test: bool, logger: Logger, **kwargs) -> None:
        '''Initialize the global variables'''
        Gv.test = test
        Gv.log = logger


# Classes


# Functions

def get_sum_of_muls(lines: list[str]) -> int:
    '''Get the sum of all mul operations'''
    # First glue all lines together
    big_line = ''.join(lines)
    Gv.log.debug(big_line)
    
    # Then get all correct mul instances
    all_muls = re.findall(r'mul\(\d+,\d+\)', big_line)
    Gv.log.debug(all_muls)

    total = 0

    for mul in all_muls:
        m = re.fullmatch(r'mul\((\d+),(\d+)\)', mul)
        total += int(m.group(1)) * int(m.group(2))

    return total


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    return get_sum_of_muls(lines)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
