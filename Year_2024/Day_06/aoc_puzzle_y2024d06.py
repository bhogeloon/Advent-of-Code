"""
Year 2024, Day 6

Problem description: See https://adventofcode.com/2024/day/6

The following classes are used:
- Position: A single position on the map
- Map: A grid class of Position objects
- Guard: Represents the guard with a position on the map

Part 1: Keep track of the visited positions. Keep trying to move the guard:
- If it walks off the map, end process
- If it runs into an obstruction, change the direction instead of the position
- Otherwise, mark the new position as visited and change it to the current
    position.
"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from grid import Grid2D

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

class Position:
    '''Position on the map'''
    def __init__(self, char: str):
        # If this is the guard
        if char == '^':
            self.obstr = False
            self.visited = True
            self.start = True
        elif char == '#':
            self.obstr= True
            self.visited = False
            self.start = False
        else:
            self.obstr = False
            self.visited = False
            self.start = False


class Map(Grid2D):
    '''Grid class of Position objects'''
    def __init__(self, lines: list[str]):
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        super().__init__(
            sizes=(self.x_size,self.y_size),
            cell_class=Position,
            input_lines=lines,
        )


    def get_visited_pos(self) -> int:
        '''Return the positions visited by the guard'''
        result = 0

        for pos in self.grid.flat:
            if pos.visited:
                result += 1

        return result


class Guard:
    '''Represents the guard'''
    def __init__(self, lines: list[str]):
        self.map = Map(lines)
        self.dir_x = 0
        self.dir_y = -1
        self.off_map = False

        # Find guard position
        for y in range(self.map.y_size):
            for x in range(self.map.x_size):
                if self.map.grid[x,y].start:
                    self.pos_x = x
                    self.pos_y = y


    def get_visited_pos(self) -> int:
        '''Return the number of visited positions'''
        return self.map.get_visited_pos()
    

    def follow(self) -> None:
        '''Follow the Guard movements until it drops out of the map'''
        while not self.off_map:
            self.move()


    def move(self) -> None:
        '''Move the guard one position further'''
        cur_pos = self.map.grid[self.pos_x,self.pos_y]
        # Calculate candidate for new position
        new_pos_x = self.pos_x + self.dir_x
        new_pos_y = self.pos_y + self.dir_y

        # See if guard drops off map
        if (
            new_pos_x < 0 or new_pos_x == self.map.x_size or
            new_pos_y < 0 or new_pos_y == self.map.y_size 
        ):
            self.off_map = True
            return
        
        new_pos = self.map.grid[new_pos_x,new_pos_y]

        # Check if new position is an obstruction
        if new_pos.obstr:
            new_coord = (-self.dir_y,self.dir_x)
            self.dir_x = new_coord[0]
            self.dir_y = new_coord[1]
            return
        
        # Otherwise set new position
        new_pos.visited = True
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    guard = Guard(lines)
    guard.follow()

    return guard.get_visited_pos()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
