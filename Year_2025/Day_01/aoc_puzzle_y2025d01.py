"""
Year 2025, Day 1

Problem description: See https://adventofcode.com/2025/day/1

The following classes are used:
- Dial: The Safe Dial with the position attribute, initialised at 50. It also 
  has a zero_cntr attribute counting the amount of times it ends up at 
  point 0
- Instruction: A single instruction containing the amount of clicks. Positive is
  Right click, negative is Left click

Part 1: Follow the instructions and use the mod function to calculate the new
position. Count the number of times the new position is 0

Part 2: Use the div function to calculate the amount of times you pass 0. This
works well for right clicks, but for left clicks (negative) there are some
exceptions to consider. 
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


    def get_password(self, instrs: Instructions, method = "orig") -> int:
        """Return the amount of times the dial ends up on 0.
        With method other than orig, use the 0x434C49434B method"""
        for instr in instrs:
            self.move(instr, method)

        return self.zero_cntr
    

    def move(self, instr: Instruction, method: str):
        """Process the instruction
        With method other than orig, use the 0x434C49434B method"""
        orig_position = self.position
        new_position = self.position + instr.amount

        self.position = new_position % 100

        if method == "orig":
            if self.position == 0:
                self.zero_cntr += 1
        else:
            # Check how many times it passes 0
            cntr_change = new_position // 100

            # If the new pos is 0 or smaller, add one, but only is orig is not 0
            if new_position < 0 and orig_position == 0:
                self.zero_cntr += abs(cntr_change) -1
            elif new_position <= 0 and self.position == 0:
                self.zero_cntr += abs(cntr_change) + 1
            else:
                self.zero_cntr += abs(cntr_change)

        Gv.log.debug(f"Instr: {instr.amount} Position: {self.position}"
                     f" Zero counter: {self.zero_cntr}")



class Instruction():
    """Single instruction"""
    def __init__(self, line: str):
        dir = line[0]
        self.amount = int(line[1:])

        if dir == "L":
            self.amount = -self.amount

        # Gv.log.debug(f"Dir: {dir}, Amount: {self.amount}")


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

    dial = Dial()
    instrs = Instructions(lines)

    return dial.get_password(instrs, method="0x434C49434B")

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
