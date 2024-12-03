"""
Year 2024, Day 1

Problem description: See https://adventofcode.com/2024/day/1

The following class is used:
- Locations: A list of locations. We have one for left and one for right

Part 1: Compose the list, sort them and go through them in parallel. Keep track
of the absolute value of the difference of each pair and return the total.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger

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

class Locations(list[int]):
    '''Simple list class containing location information'''


# Functions

def create_loc_lists(
        loc_left: Locations, 
        loc_right: Locations,
        lines: list[str]
    ) -> None:
    '''Create the two location lists'''
    for line in lines:
        values = [int(v) for v in line.split()]
        loc_left.append(values[0])
        loc_right.append(values[1])

    # Sort so they can be compared
    loc_left.sort()
    loc_right.sort()

    Gv.log.debug(loc_left)
    Gv.log.debug(loc_right)


def get_distances(loc_left: Locations, loc_right: Locations) -> int:
    '''Get the total differences between the locations'''
    total = 0

    for i in range(len(loc_left)):
        total += abs(loc_left[i] - loc_right[i])

    return total


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    left_loc = Locations()
    right_loc = Locations()

    create_loc_lists(left_loc, right_loc, lines)

    return get_distances(left_loc, right_loc)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
