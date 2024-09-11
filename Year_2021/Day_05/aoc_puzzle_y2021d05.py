"""
Year 2021, Day 5

Problem description: See https://adventofcode.com/2021/day/5

<Include solution description>

"""

# Imports
from pprint import pprint
from grid import Grid2D


# Constants

GRID_SIZE = 1000

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class OceanFloor(Grid2D):
    '''Represents the ocean floor, containg a numpy grid.'''
    def __init__(self) -> None:
        pass


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    floor = OceanFloor()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
