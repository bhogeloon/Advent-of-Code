"""
Year 2020, Day 14, Part 1

Problem description: See https://adventofcode.com/2020/day/14

"""

# Imports
from pprint import pprint
import re

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class CompSystem():
    def __init__(self) -> None:
        self.mem = {}
        self.mask = 'X' * 36


    def store_mem(self, mem_address: int, mem_value: int) -> None:
        flip0_str = self.mask.replace('X', '1')
        flip0_int = int(flip0_str, base=2)
        mem_value = mem_value & flip0_int

        flip1_str = self.mask.replace('X', '0')
        flip1_int = int(flip1_str, base=2)
        mem_value = mem_value | flip1_int

        self.mem[mem_address] = mem_value


    def sum(self) -> int:
        return sum(self.mem.values())


# Functions


# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    comp_sys = CompSystem()

    for line in lines:
        if line[:4] == 'mask':
            comp_sys.mask = line[7:]
            continue

        m = re.fullmatch(r'mem\[(\d+)\] = (\d+)', line)
        mem_address = int(m.group(1))
        mem_value = int(m.group(2))
        comp_sys.store_mem(mem_address, mem_value)

    return comp_sys.sum()

    return __name__


if __name__ == '__main__':
    pass