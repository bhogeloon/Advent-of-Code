"""
Year 2020, Day 12

Problem description: See https://adventofcode.com/2020/day/12

The following classes are used:
- Instruction: A single instruction containing an action and an amount
- Instructions: Deque container class of Instruction objects
- Ship: A ship with a position (x,y) and a dir indicating the direction

Part 1: Move the ship according to each instruction and read the position it
has finished in (it started at 0,0)
"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from collections import deque

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

class Instruction:
    '''Represents an instruction with an action attribute and an amount
    attribute'''
    def __init__(self, line: str):
        self.action = line[0]
        self.amount = int(line[1:])


class Instructions(deque[Instruction]):
    '''deque container class of Instruction objects'''
    def __init__(self, lines: list[str]):
        for line in lines:
            self.append(Instruction(line))


class Ship:
    '''Represents a ship with a pos(ition), a dir(ection) and a reference
    to the Instructions'''
    def __init__(self, lines: list[str]) -> None:
        self.pos = (0,0)
        # Initial direction East
        self.dir = (1,0)
        self.instructions = Instructions(lines)


    def move(self):
        '''Move the ship with a single instruction'''
        instruction = self.instructions.popleft()

        # If we need to change direction
        if instruction.action == 'R' or instruction.action == 'L':
            nr_turns = instruction.amount // 90
            if instruction.action == 'R':
                for i in range(nr_turns):
                    self.dir = (self.dir[1], -self.dir[0])
            elif instruction.action == 'L':
                for i in range(nr_turns):
                    self.dir = (-self.dir[1], self.dir[0])

            return

        # If we have to move the ship, set chdir to the direction it has to 
        # change to
        if instruction.action == 'E':
            chdir = (1,0)
        elif instruction.action == 'S':
            chdir = (0,-1)
        elif instruction.action == 'W':
            chdir = (-1,0)
        elif instruction.action == 'N':
            chdir = (0,1)
        # If forward instruction, use current direction
        elif instruction.action == 'F':
            chdir = self.dir
        else:
            raise RuntimeError('Invalid command {}'.format(instruction.action))

        # Change the position according to the given direction and amount
        self.pos = (
            self.pos[0] + instruction.amount * chdir[0],
            self.pos[1] + instruction.amount * chdir[1],
        )


    def move_all(self):
        '''Execute all instructions'''
        while len(self.instructions) > 0:
            self.move()


    def get_manhattan_dist(self) -> int:
        '''Return the Manhatten distance to the original position (0,0)'''
        return abs(self.pos[0]) + abs(self.pos[1])


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    ship = Ship(lines)
    ship.move_all()

    return ship.get_manhattan_dist()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
