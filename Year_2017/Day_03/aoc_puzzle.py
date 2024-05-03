"""
Year 2017, Day 3

Problem description: See https://adventofcode.com/2017/day/3

We use the following class:
- MemoryGrid: contains a grid which is filled with memory point values. The filling take
place in a spiral form.

Part 1: The way we fill the grid is keep track of the current position and of the direction.
After each move, we try to change the direction, but we only actually change the direction if 
we find an empty grid entry on this position.
Once the end value is reached, we record the position and aftwards we calculate the distance.

For part 2 we use the same method to go through the spiral, but instead of filling in the memory
point, we fill in the memory value. Initially this is 1, but when we move to the next point,
the value is calculated as the sum of the sub_grid of the surrounding area (3x3).
As soon as we hit a value higher than the input, we record this number and stop.

"""

# Imports
from pprint import pprint
import numpy as np


# Constants

# Limit of the 'infinite' grid
GRID_SIZE = 1000
GRID_START = 1000//2

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class MemoryGrid():
    '''Grid containing memory items'''

    def __init__(self, limit: int, part = 1) -> None:
        self.grid = np.full((GRID_SIZE,GRID_SIZE), 0)

        self.limit = limit
        # Starting point
        self.cur_x = GRID_START
        self.cur_y = GRID_START
        # Direction that the points are moving
        self.dir_x = 1
        self.dir_y = 0

        if part == 1:
            self._init_part1()
        elif part == 2:
            self._init_part2()
        else:
            raise RuntimeError("Weird part number: {}".format(part))


    def _init_part1(self) -> None:
        '''Create the grid according to part 1'''
        # Memory point, starting at 1 and increasing in each loop
        mem_pt = 1

        while True:
            # Fill current memory point
            self.grid[self.cur_x,self.cur_y] = mem_pt

            # If at end point
            if mem_pt == self.limit:
                self.end_x = self.cur_x
                self.end_y = self.cur_y
                return
            
            # Move the pointer
            self.cur_x += self.dir_x
            self.cur_y += self.dir_y

            # Check if you have to move direction
            self._change_dir()

            # Increase memory point
            mem_pt += 1


    def _init_part2(self) -> None:
        '''Create the grid according to part 2'''
        # First memory value
        mem_val = 1

        while True:
            # Fill current memory point
            self.grid[self.cur_x,self.cur_y] = mem_val

            # If at end point
            if mem_val > self.limit:
                self.end_x = self.cur_x
                self.end_y = self.cur_y
                self.max_value = mem_val
                return
            
            # Move the pointer
            self.cur_x += self.dir_x
            self.cur_y += self.dir_y

            # New value is sum of surrounding area
            mem_val=self.grid[self.cur_x-1:self.cur_x+2,self.cur_y-1:self.cur_y+2].sum()

            # Check if you have to move direction
            self._change_dir()


    def _change_dir(self) -> None:
        '''Check if you have to move direction and if so do so'''
        if self.dir_x == 1:
            if self.grid[self.cur_x,self.cur_y+1] == 0:
                self.dir_x = 0
                self.dir_y = 1
        elif self.dir_x == -1:
            if self.grid[self.cur_x,self.cur_y-1] == 0:
                self.dir_x = 0
                self.dir_y = -1
        elif self.dir_y == 1:
            if self.grid[self.cur_x-1,self.cur_y] == 0:
                self.dir_x = -1
                self.dir_y = 0
        elif self.dir_y == -1:
            if self.grid[self.cur_x+1,self.cur_y] == 0:
                self.dir_x = 1
                self.dir_y = 0
        else:
            raise RuntimeError("Wrong xy combination: {},{}".format(self.dir_x,self.dir_y))


    def get_distance(self) -> int:
        '''Return the Manhattan distance between start an end point'''
        return abs(self.end_x - GRID_START) + abs(self.end_y - GRID_START)


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    square_nr = int(lines[0])
    memgrid = MemoryGrid(square_nr)

    return memgrid.get_distance()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    square_nr = int(lines[0])
    memgrid = MemoryGrid(square_nr, part=2)

    return memgrid.max_value

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
