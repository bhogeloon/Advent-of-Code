"""
Year 2022, Day 12

Problem description: See https://adventofcode.com/2022/day/12

The following classes are used:
- Location: A grid location which has a certain height.
- Map: Grid class containing Location objects.

Part 1: I started at the endpoint and worked my way back to the starting point 
using a recursive function. So starting from the endpoint, a location is
investigated as follows:
- If the height difference is too much, return to the previous location
- If this point is already in the current investigation path, return (to avoid
    a loop)
- If the current path length is not smaller than the one previously 
    detected, return. Otherwise update the "dist_to_end".
- After this, start investigating all neighbor locations in the same way
When this process finished, all locations that have some sort of connection to
the endpoint, should have a "dist_to_end" value, so then it is just a question
of retrieving this value from the start point.
This process takes about 1.5 minutes.

Part 2: As I have done the investigations of all points already in part 1,
part 2 just consists of retrieving the dist_to_end values of all starting
points and return the minimum. As a result of this approach, also part 2 takes 
about 1.5 minutes.

Note: The process that I'm using is not entirely optimal. When a point is
investigated for the second time, it will again recursively investigate all
neighbors.
I made an attempt to improve on this (see branch y2022d12_alt), but in the end
did not get the same result. Also the time gain was not what I had hoped, so I
gave up on that one.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from grid import Grid2D
import sys

sys.setrecursionlimit(2000)

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

class Location():
    '''Location on map with a certain height'''

    def __init__(self, indicator: str) -> None:
        self.endpoint = False
        self.startpoint = False

        if indicator == 'S':
            self.height = 1
            self.startpoint = True
        elif indicator == 'E':
            self.height =26
            self.endpoint = True
        else:
            self.height = ord(indicator) - ord('a') + 1

        self.dist_to_start = 999999999
        self.dist_to_end = 999999999


class Map(Grid2D):
    '''Matrix of locations'''

    def __init__(self, lines: list[str]) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        super().__init__(sizes=(self.x_size,self.y_size))
        self.locations = self.grid
        self.set_locations(lines)
        self.cur_path = []


    def set_locations(self, lines: list[str]) -> None:
        '''Initialise the locations'''
        for x in range(self.x_size):
            for y in range(self.y_size):
                self.locations[x,y] = Location(lines[y][x])

                # Register start and endpoints
                if lines[y][x] == 'S':
                    self.startpoint = (x,y)
                elif lines[y][x] == 'E':
                    self.endpoint = (x,y)


    def start_path_search(self) -> int:
        '''Start the search starting from the fixed Start point'''
        e_x, e_y = self.endpoint
        self.investigate_path(e_x, e_y, 27)

        s_x, s_y = self.startpoint
        # Return te distance to end from the starting point
        return self.locations[s_x,s_y].dist_to_end
    

    def get_shortest_path(self) -> int:
        '''Get the shortes path, taking into account all a points'''
        # First repeat the part 1 investigation
        e_x, e_y = self.endpoint
        self.investigate_path(e_x, e_y, 27)

        path_lengths = []

        # Now just retrieve the dist_to_end value for all a points 
        for location in self.locations.flat:
            if location.height == 1:
                path_lengths.append(location.dist_to_end)

        # Return the minimum
        return min(path_lengths)


    def investigate_path(self, x:int, y:int, height: int):
        '''Investigate the path for this point towards the endpoint'''
        location = self.locations[x,y]

        # If the height of this location is too small
        if location.height < height - 1:
            # pprint(height, location.height)
            return

        # If this point is already part of the current path
        if (x,y) in self.cur_path:
            return
        
        dist_to_end = len(self.cur_path)

        # If the distance is larger (or equal) than already detected
        if dist_to_end >= location.dist_to_end:
            return

        # Update distance to end
        location.dist_to_end = dist_to_end
        # Append this location to the current path
        self.cur_path.append((x,y))

        # Now start to investigate the neighbors
        if x > 0:
            self.investigate_path(x-1,y, location.height)

        if y > 0:
            self.investigate_path(x,y-1, location.height)

        if x < self.x_size - 1:
            self.investigate_path(x+1,y, location.height)

        if y < self.y_size - 1:
            self.investigate_path(x,y+1, location.height)

        # Remove this location from the path before giving the control back
        self.cur_path.pop()

        return


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    map = Map(lines)

    return map.start_path_search()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    map = Map(lines)

    return map.get_shortest_path()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
