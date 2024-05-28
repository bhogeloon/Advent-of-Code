"""
Year 2018, Day 3

Problem description: See https://adventofcode.com/2018/day/3

<Include solution description>

"""

# Imports
from pprint import pprint
import numpy as np


# Constants

# Grid size
GRID_SIZE = 1000


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Fabric():
    '''Class for the fabric for Santa's outfit.
    Contains a numpy grid object'''

    def __init__(self) -> None:
        self.grid = np.full((GRID_SIZE,GRID_SIZE), None)

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                self.grid[x,y] = 0


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    fabric = Fabric()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
