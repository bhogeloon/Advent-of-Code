"""
Year 2021, Day 11

Problem description: See https://adventofcode.com/2021/day/11

The following classes are used:
- Dumbo: Represents a dumbo octopus with a certain energy level
- Cave: Grid class representing the cave grid. Each grid point holds a dumbo.

Part 1: For each of the 100 steps, walk through the matrix and increase the 
value by 1. If the values exceeds 9, start the flash process, which means go to 
every neighbor and increase the value of that neighbor. Each time, if the value
exceeds 9, start the flash process recursively.
In order to prevent items flashing multiple times, mark dumbo's as being
flashed.
At the end of each step, walk through the matrix again and reset all values
greater than 9 to 0. Also reset all dumbo flashed flags to False.

Part 2: The same as part 1, but the loop continues as long as not all Dumbo
objects are in flashed state. Count the number of loops.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from grid import Grid2D

# Constants

# nr of total steps to consider
STEPS = 100


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

class Dumbo:
    '''A single Dumbo'''
    def __init__(self, char: str) -> None:
        self.level = int(char)
        self.flashed = False


class Cave(Grid2D):
    '''Grid class of Dumbo objects'''
    def __init__(self, lines: list[str]) -> None:
        self.y_size = len(lines)
        self.x_size = len(lines[0])
        super().__init__(
            sizes=(self.x_size,self.y_size),
            func=lambda x=None,y=None,lines=lines: Dumbo(lines[y][x]),
        )
        self.dumbos = self.grid

        # This attribute will be used to track if all dumbos have flashed
        # simultanuously (as in part 2)
        self.all_flashed = False


    def flash_dumbo(self, x:int, y:int) -> int:
        '''Flash a specific dumbo with x,y coordinates'''
        # Mark dumbo as flashed
        self.dumbos[x,y].flashed = True

        # Set nr_of_flashes to 1
        nr_of_flashes = 1

        # Determine min and max values of neighbors
        if x == 0:
            min_x = 0
            max_x = 1
        elif x == self.x_size - 1:
            min_x = x -1
            max_x = x
        else:
            min_x = x - 1
            max_x = x + 1

        if y == 0:
            min_y = 0
            max_y = 1
        elif y == self.y_size - 1:
            min_y = y -1
            max_y = y
        else:
            min_y = y - 1
            max_y = y + 1

        for neighbor_y in range(min_y, max_y + 1):
            for neighbor_x in range(min_x, max_x + 1):
                # Ignore if this is this is yourself
                if neighbor_x == x and neighbor_y == y:
                    continue

                # Increase value
                self.dumbos[neighbor_x, neighbor_y].level += 1

                if (
                    self.dumbos[neighbor_x, neighbor_y].level > 9 and 
                    not self.dumbos[neighbor_x, neighbor_y].flashed
                ):
                    nr_of_flashes += self.flash_dumbo(
                        neighbor_x,
                        neighbor_y,
                    )

        return nr_of_flashes


    def flash_all_dumbos(self) -> int:
        '''Flash all dumbos and return the number of flashes'''
        nr_of_flashes = 0

        # Increase the points in the matrix
        for y in range(self.y_size):
            for x in range(self.x_size):
                # Increase the number
                self.dumbos[x,y].level += 1

                # If bigger than 9 and not already flashed
                if (
                    self.dumbos[x,y].level > 9 and
                    not self.dumbos[x,y].flashed
                ):
                    # (x,y) not in flash_points:
                    nr_of_flashes += self.flash_dumbo(x, y)

        self.all_flashed = True

        # Now go through the matrix again:
        for dumbo in self.dumbos.flat:
            if dumbo.level > 9:
                dumbo.level = 0
                dumbo.flashed = False
            # If a non-flashed dumbo has been find, set all_flashed to False
            else:
                self.all_flashed = False

        return nr_of_flashes


    def get_nr_of_flashes(self):
        '''Get the Number of Flashes'''
        nr_of_flashes = 0

        # Perform 100 steps
        for step in range(STEPS):
            nr_of_flashes += self.flash_all_dumbos()

        return nr_of_flashes


    def get_all_flashed(self) -> int:
        '''Return the number of steps after which all dumbos have flashed'''
        steps = 0

        while not self.all_flashed:
            steps += 1
            self.flash_all_dumbos()

        return steps
    

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    cave = Cave(lines)

    return cave.get_nr_of_flashes()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    cave = Cave(lines)

    return cave.get_all_flashed()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
