"""
Year 2024, Day 1

Problem description: See https://adventofcode.com/2024/day/1

The following class is used:
- Locations: A list of locations. We have one for left and one for right (this
could have been kept a normal list, of course).

Part 1: Compose the list, sort them and go through them in parallel. Keep track
of the absolute value of the difference of each pair and return the total.

Part 2: For each location on the left, count the numbers on the right, multiply
and add to the total.
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
        left_locs: Locations, 
        right_locs: Locations,
        lines: list[str]
    ) -> None:
    '''Create the two location lists'''
    for line in lines:
        values = [int(v) for v in line.split()]
        left_locs.append(values[0])
        right_locs.append(values[1])

    # Sort so they can be compared
    left_locs.sort()
    right_locs.sort()

    Gv.log.debug(left_locs)
    Gv.log.debug(right_locs)


def get_distances(left_locs: Locations, right_locs: Locations) -> int:
    '''Get the total differences between the locations'''
    total = 0

    for i in range(len(left_locs)):
        total += abs(left_locs[i] - right_locs[i])

    return total


def get_similarity_score(left_locs: Locations, right_locs: Locations) -> int:
    '''Return the similarity score'''
    total = 0

    for left_loc in left_locs:
        total += left_loc * right_locs.count(left_loc)

    return total


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    left_locs = Locations()
    right_locs = Locations()

    create_loc_lists(left_locs, right_locs, lines)

    return get_distances(left_locs, right_locs)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    left_locs = Locations()
    right_locs = Locations()

    create_loc_lists(left_locs, right_locs, lines)

    return get_similarity_score(left_locs, right_locs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
