"""
Year 2021, Day 9

Problem description: See https://adventofcode.com/2021/day/9

The following classes are used:
- Point: A point on the map with a height value
- HeightMap: a Grid class containing Point objects

Part 1: Walk through the matrix and consider each neighbor. If all
of those values are bigger than the current value, it is
a Low Point. Add the value to the total and add 1 extra.

Part 2:
First find all the low points as in part one, but this time keep a list
of all low points with their coordinates.

Then go through each low point and investigate their direct neighors. For each
neighbor which is not a value 9, call the same function recursively.
In the mean time, store all points found in a list so that you can:
    a) Keep track of all the points already investigated, so you don't go
        on for ever.
    b) Keep track of the amount of points.

For each low point, store the amount of found points and in the end consider
the highest 3.

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

        '''
        low_points is a list of Low Points. Each entry consists of a dict with
        the  following attributes:
            low_point: (x,y) tuple with the coordinates of the Low Point itself
            basin: List of (x,y) tuples with the points which are part of the 
                basin (This includes the low point itself)
        '''
        self.low_points = []


    def get_total_risk(self) -> int:
        '''Return the total risk level'''
        total_risk = 0

        for y in range(self.y_size):
            for x in range(self.x_size):
                if self.grid[x,y].is_low_point(self):
                    total_risk += self.grid[x,y].height + 1

        return total_risk


    def find_basin_neighbors(self, low_point: dict, x: int, y: int):
        '''This function will try to find neighbors of point (x,y), which are 
        part ofccthe basin. It is a recursive function as it calls itself for 
        all the found neighbbors'''
        # The first step is to register yourself in the basin
        low_point['basin'].append((x,y))

        # Now discover addtional neighbors on the left
        # If you're on the border, don't bother
        if x > 0:
            # Check neighbor not 9 and whether you haven't already explored it
            if (
                self.grid[x-1,y].height < 9 and 
                (x-1,y) not in low_point['basin']
            ):
                # Now call yourself for the neighbor point
                self.find_basin_neighbors(low_point, x-1, y)

        # Now discover addtional neighbors on the right
        # If you're on the border, don't bother
        if x < self.x_size - 1:
            # Check neighbor not 9 and whether you haven't already explored it
            if (
                self.grid[x+1,y].height < 9 and 
                (x+1,y) not in low_point['basin']
            ):
                # Now call yourself for the neighbor point
                self.find_basin_neighbors(low_point, x+1, y)

        # Now discover addtional neighbors above
        # If you're on the border, don't bother
        if y > 0:
            # Check neighbor not 9 and whether you haven't already explored it
            if (
                self.grid[x,y-1].height < 9 and 
                (x,y-1) not in low_point['basin']
            ):
                # Now call yourself for the neighbor point
                self.find_basin_neighbors(low_point, x, y-1)

        # Now discover addtional neighbors above
        # If you're on the border, don't bother
        if y < self.y_size - 1:
            # Check neighbor not 9 and whether you haven't already explored it
            if (
                self.grid[x,y+1].height < 9 and 
                (x,y+1) not in low_point['basin']
            ):
                # Now call yourself for the neighbor point
                self.find_basin_neighbors(low_point, x, y+1)

        return


    def get_basin_product(self):
        # Find all low points
        for y in range(self.y_size):
            for x in range(self.x_size):
                if self.grid[x,y].is_low_point(self):
                    self.low_points.append({
                        'low_point': (x,y),
                        'basin': [],
                    })

        basin_sizes = []

        # For each low point, find the basin points
        for low_point in self.low_points:
            self.find_basin_neighbors(low_point, *low_point['low_point'])
            basin_sizes.append(len(low_point['basin']))

        # Sort it, so you can extract the top 3
        basin_sizes.sort(reverse=True)

        basin_product = 1

        for i in range(3):
            basin_product *= basin_sizes[i]

        return basin_product


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

    map = HeightMap(lines)

    return map.get_basin_product()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
