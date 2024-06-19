"""
Year 2020, Day 3

Problem description: See https://adventofcode.com/2020/day/3

We use the following classes:
-   GridSpot: contains a boolean tree to indicate that a tree is present or not
-   Grid: numpy class containing all the trees

Part 1: We walk across the grid using the Toboggan pattern and count the trees until we are 
at the bottom. If we encounter the far right we go back to the start from the left.
 
"""

# Imports
from pprint import pprint
# Use function in aoc_lib
from grid import Grid2D


# Constants
X_INC = 3
Y_INC = 1


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
        )

        for y in range(self.y_size):
            for x in range(self.x_size):
                self.grid[x,y] = GridSpot(lines[y][x])


    def count_encountered_trees(self) -> int:
        '''Count the encountered trees following the Tobbogan pattern'''
        nr_of_trees = 0
        x_pos = 0
        y_pos = 0

        while True:
            # Increase if tree has veen found
            if self.grid[x_pos,y_pos].tree:
                nr_of_trees += 1

            # Increase y coordinate
            y_pos += Y_INC

            # If at the bottom, stop
            if y_pos >= self.y_size:
                break

            # Increas x coordinate
            x_pos += X_INC

            # If at the far right, start from the left again
            if x_pos >= self.x_size:
                x_pos -= self.x_size

        return nr_of_trees


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

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
