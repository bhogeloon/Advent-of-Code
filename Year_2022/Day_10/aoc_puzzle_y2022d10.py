"""
Year 20xx, Day xx

Problem description: See https://adventofcode.com/20xx/day/xx

The following class is being used:
- Cpu: The processor, containing an X register and maintaining the amount
    of cycles. It also a a list of instructions.

Part 1: Go through each instruction, increasing the cycles and updating the
X register. If a cycle in the check-point list is reach, calculate the signal
strength. Report the sum of the signal strengths.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from collections import deque
import re


# Constants

CHECK_POINTS = (20, 60, 100, 140, 180, 220)


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

class Cpu():
    '''Processor'''

    def __init__(self, lines: list[str]) -> None:
        # The amount of cycles passed
        self.cycle = 0
        # X register
        self.x = 1
        # Instructions
        self.instrs = deque(lines)
        # Signal strengths
        self.sig_strs = {}
        self.picture = ''
        self.crt_pos = 0


    def process_instrs(self) -> None:
        '''Process all the instructions'''
        while len(self.instrs) > 0:
            self.process_next_instr()


    def process_next_instr(self) -> None:
        '''Process the next instruction'''
        instr_line = self.instrs.popleft()
        # Increase cycle
        self.inc_cyle()

        m = re.match(r'addx (-?\d+)$', instr_line)

        # If this is an add instruction
        if m:
            # Extra increase cycle
            self.inc_cyle()
            # Update X register
            self.x += int(m.group(1))


    def inc_cyle(self) -> None:
        '''Increase the cycle and register signal strength in check points'''
        self.cycle += 1

        # If in checkpoint, calculate signal strength
        if self.cycle in (CHECK_POINTS):
            self.sig_strs[self.cycle] = self.cycle*self.x

        if self.crt_pos >= self.x-1 and self.crt_pos <= self.x+1:
            self.picture += '#'
        else:
            self.picture += '.'

        self.crt_pos += 1

        if self.crt_pos == 40:
            self.picture += '\n'
            self.crt_pos = 0


    def get_total_sig_strs(self) -> int:
        '''Return the sum of all signal strength in each check point'''
        return sum(self.sig_strs.values())
    

    def print(self) -> None:
        print(self.picture)


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    cpu = Cpu(lines)
    cpu.process_instrs()

    return cpu.get_total_sig_strs()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
