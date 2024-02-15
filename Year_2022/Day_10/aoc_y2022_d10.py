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
        self.cycle = 0
        self.x = 1
        self.instrs = deque(lines)
        self.sig_strs = {}
        self.picture = ''
        self.crt_pos = 0


    def process_instrs(self) -> None:
        while len(self.instrs) > 0:
            self.process_next_instr()


    def process_next_instr(self) -> None:
        instr_line = self.instrs.popleft()
        self.inc_cyle()

        m = re.match(r'addx (-?\d+)$', instr_line)

        if m:
            self.inc_cyle()
            self.x += int(m.group(1))


    def inc_cyle(self) -> None:
        self.cycle += 1

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
        return sum(self.sig_strs.values())
    

    def print(self) -> None:
        print(self.picture)


# Main functions
def get_solution_part1(lines: list[str]) -> int:
    '''Main function'''

    cpu = Cpu(lines)
    cpu.process_instrs()

    return cpu.get_total_sig_strs()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str]) -> int:
    '''Main function'''

    cpu = Cpu(lines)
    cpu.process_instrs()
    cpu.print()

    # return 'part_2 ' + __name__


if __name__ == '__main__':
    pass