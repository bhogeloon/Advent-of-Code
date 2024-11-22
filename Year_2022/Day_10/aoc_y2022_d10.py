"""
Year 2022, Day 10

Problem description: See https://adventofcode.com/2022/day/10

"""

# Imports
from pprint import pprint
from collections import deque
import re

# Constants

CHECK_POINTS = (20, 60, 100, 140, 180, 220)

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


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


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    cpu = Cpu(lines)
    cpu.process_instrs()

    return cpu.get_total_sig_strs()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    cpu = Cpu(lines)
    cpu.process_instrs()
    cpu.print()

    # return 'part_2 ' + __name__


if __name__ == '__main__':
    pass