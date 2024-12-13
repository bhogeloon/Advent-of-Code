"""
Year 2021, Day 12

Problem description: See https://adventofcode.com/2021/day/12

The following classes are used:
- Cave: A cave with a name and a list of neighbours
- Maze: A dict container class of Cave objects

Part 1: First I store all relations in the Cave objects and store all Cave 
objects in the Maza object.
Note that the start point can be the A end or the B end (because you
can also travel the other way).
Then I start iterating over each possible destination, calling the same
function recursively. In the mean time we keep track of the current path in a 
list. If we see the end as the destination, we found a proper path. If we see a 
small cave, which is already in the list, we have found a dead end and we are 
not going to proceed.

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

class Cave:
    '''A cave with a list of connections to other caves'''
    def __init__(self, name:str):
        self.name = name
        self.neighbours = []


class Maze(dict[str,Cave]):
    '''A dict container class of Cave objects'''
    def __init__(self, lines:list[str]):
        for line in lines:
            caves = line.split('-')

            for cave in caves:
                if cave not in self.keys():
                    self[cave] = Cave(cave)

            for i in range(2):
                if self[caves[1-i]] not in self[caves[i]].neighbours:
                    self[caves[i]].neighbours.append(self[caves[1-i]])

        self.current_path = []


    def calculate_path(self, start_point: str) -> int:
        '''Recursive function to calculate the path'''
        # If this point is a small cage we already visited, don't bother
        if start_point.islower() and start_point in self.current_path:
            return 0

        # If the current start_point is 'end', then we have a valid path
        if start_point == 'end':
            return 1

        # Then add this point to the path
        self.current_path.append(start_point)
        paths_found = 0

        for end_cave in self[start_point].neighbours:
            paths_found += self.calculate_path(end_cave.name)
        
        # Now remove the current point before returning
        self.current_path.pop()

        return paths_found


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    maze = Maze(lines)

    return maze.calculate_path('start')

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
