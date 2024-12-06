"""
Year 2020, Day 3

Problem description: See https://adventofcode.com/2020/day/3

We use the following classes:
-   GridSpot: contains a boolean tree to indicate that a tree is present or not
-   Grid: numpy class containing all the trees

Part 1: We walk across the grid using the Toboggan pattern and count the trees until we are 
at the bottom. If we encounter the far right we go back to the start from the left.

Part 2: Do the same thing using varying patterns and multiply all results.
"""

# Imports
from pprint import pprint
# Use function in aoc_lib
from grid import Grid2D


# Constants
# For part 1
X_INC = 3
Y_INC = 1

# For part 2
XY_INC = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2),
]


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes
class GridSpot():
    '''Spot on the grid, which either contains a tree or not'''

    def __init__(self, char: str) -> None:
        if char == '#':
            self.tree = True
        else:
            self.tree = False


class Grid(Grid2D):
    '''Numpy grid containing GridSpot objects'''

    def __init__(self, lines: list[str]) -> None:
        self.y_size = len(lines)
        self.x_size = len(lines[0])
        super().__init__(
            sizes=(self.x_size,self.y_size),
            input_lines=lines,
            cell_class=GridSpot,
        )


    def count_encountered_trees(self, x_inc=X_INC, y_inc=Y_INC) -> int:
        '''Count the encountered trees following the Tobbogan pattern'''
        nr_of_trees = 0
        x_pos = 0
        y_pos = 0

        while True:
            # Increase if tree has veen found
            if self.grid[x_pos,y_pos].tree:
                nr_of_trees += 1

            # Increase y coordinate
            y_pos += y_inc

            # If at the bottom, stop
            if y_pos >= self.y_size:
                break

            # Increas x coordinate
            x_pos += x_inc

            # If at the far right, start from the left again
            if x_pos >= self.x_size:
                x_pos -= self.x_size

        return nr_of_trees


    def multiply_all_slopes(self) -> int:
        '''Run the slope with varying patterns and multiply all results'''

        result = 1

        for (x_inc, y_inc) in XY_INC:
            result *= self.count_encountered_trees(x_inc,y_inc)

        return result
    

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    grid = Grid(lines)

    return grid.count_encountered_trees()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    grid = Grid(lines)

    return grid.multiply_all_slopes()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
