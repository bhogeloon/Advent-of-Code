"""
Year 2025, Day 1

Problem description: See https://adventofcode.com/2025/day/1

The following classes are used:
- Dial: The Safe Dial with the position attribute, initialised at 50. It also 
  has a zero_cntr attribute counting the amount of times it ends up at 
  point 0
- Instruction: A single instruction containing the amount of clicks. Positive is
  Right click, negative is Left click

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger

# Constants

DIAL_START_POS = 50
DIAL_MAX_POS = 99

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

class Dial():
    """A Dial with a position and zero counter"""
    def __init__(self, start_pos=DIAL_START_POS):
        self.position = start_pos
        self.zero_cntr = 0
        self.max_pos = DIAL_MAX_POS


    def get_password(self, instrs: Instructions) -> int:
        """Return the amount of times the dial ends up on 0"""
        for instr in instrs:
            self.move(instr)

        return self.zero_cntr
    

    def move(self, instr: Instruction):
        """Process the instruction"""
        self.position += instr.amount

        self.position %= 100

        Gv.log.debug(f"Position: {self.position}")

        if self.position == 0:
            self.zero_cntr += 1


class Instruction():
    """Single instruction"""
    def __init__(self, line: str):
        dir = line[0]
        self.amount = int(line[1:])

        if dir == "L":
            self.amount = -self.amount

        Gv.log.debug(f"Dir: {dir}, Amount: {self.amount}")


class Instructions(list):
    """Container class of Instruction objects"""
    def __init__(self, lines: list[str]):
        for line in lines:
            self.append(Instruction(line))


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    dial = Dial()
    instrs = Instructions(lines)

    return dial.get_password(instrs)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
