"""
Year 2021, Day 9

Problem description: See https://adventofcode.com/2021/day/9

The following classes are used:
- Point: A point on the map with a height value
- HeightMap: a Grid class containing Point objects

Part 1: Walk through the matrix and consider each neighbor. If all
of those values are bigger than the current value, it is
a Low Point. Add the value to the total and add 1 extra.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from grid import Grid2D


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes
class Point:
    '''A Point represents a point in the HeightMap. It has a height value
    and a is_low boolean'''
    def __init__(self, height: str, x: int, y: int) -> None:
        self.height = int(height)
        self.x = x
        self.y = y

    def is_low_point(self, map: HeightMap) -> bool:
        '''Return if the point is a low point or not'''
        x = self.x
        y = self.y
        grid = map.grid

        # Check left
        if x == 0:
            low_left = True
        else:
            low_left = grid[x,y].height < grid[x-1,y].height

        # Check right
        if x == map.x_size - 1:
            low_right = True
        else:
            low_right = grid[x,y].height < grid[x+1,y].height

        # Check up
        if y == 0:
            low_up = True
        else:
            low_up = grid[x,y].height < grid[x,y-1].height

        # Check down
        if y == map.y_size - 1:
            low_down = True
        else:
            low_down = grid[x,y].height < grid[x,y+1].height

        # return True if all is True
        self.is_low = (low_right and low_left and low_up and low_down)
        return self.is_low


class HeightMap(Grid2D):
    '''Grid class which contain the heights'''
    def __init__(self, lines: list[str]) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        super().__init__(
            sizes = (self.x_size, self.y_size),
            func=lambda x=None,y=None,lines=lines: Point(lines[y][x],x,y),
        )


    def get_total_risk(self) -> int:
        '''Return the total risk level'''
        total_risk = 0

        for y in range(self.y_size):
            for x in range(self.x_size):
                if self.grid[x,y].is_low_point(self):
                    total_risk += self.grid[x,y].height + 1

        return total_risk


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    map = HeightMap(lines)

    return map.get_total_risk()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
