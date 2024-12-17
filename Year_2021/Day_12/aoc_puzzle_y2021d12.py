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

Part 2: If a small duplicate is found, permit one duplicate. Keep track of that
one with a special flag. This flag needs to be cleared at the end of the 
recursive function instance.

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
        # Flag to indicate that a small duplicat is already present
        self.small_dupl_present = False


    def calculate_path(self, start_point: str, part=1) -> int:
        '''Recursive function to calculate the path'''
        # If the current start_point is 'end', then we have a valid path
        if start_point == 'end':
            Gv.log.debug(self.str_path())
            return 1

        # Flag to indicate that a small duplicate has been detected, so the
        # generic flag needs to be cleared at the end of this cycle
        dupl_in_this_cycle = False

        # If this point is a small cage we already visited (twice in part 2), 
        # don't bother
        if start_point.islower() and start_point in self.current_path:
            if part == 1 or start_point == 'start' or self.small_dupl_present:
                return 0
            elif self.current_path.count(start_point) > 1:
                return 0
            else:
                self.small_dupl_present = True
                dupl_in_this_cycle = True

        # Then add this point to the path
        self.current_path.append(start_point)
        paths_found = 0

        for end_cave in self[start_point].neighbours:
            paths_found += self.calculate_path(end_cave.name,part=part)
        
        # Now remove the current point before returning
        self.current_path.pop()

        # Reset the duplicate flag if required:
        if dupl_in_this_cycle:
            self.small_dupl_present = False

        return paths_found
    

    def str_path(self) -> str:
        '''String representation of current path'''
        result = ''
        for cave_name in self.current_path:
            result += f'{cave_name},'

        result += 'end'
        return result


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

    maze = Maze(lines)

    return maze.calculate_path('start',part=2)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
