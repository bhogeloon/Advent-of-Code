"""
Year 2020, Day 14

Problem description: See https://adventofcode.com/2020/day/14

The following class is used:
- CompSystem: The computer system, containing an active mask and a dict
    containing memory entries

Part 1: Change the active mask every time one is detected in the input. Then
manipulate the bitmask by replacing all X's by 1's and then do a logical AND
with the value being store. This will replace all 0's.
Next manipulate the bitmask to replace all X's by 0's and do a logical OR with
the value being stored. This will replace all 1's.
Then store the result at the memory address specified. In the end calculate the
sum of all memory values.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
import re

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

class CompSystem():
    '''Computer System class'''
    def __init__(self) -> None:
        self.mem = {}
        self.mask = 'X' * 36


    def store_mem(self, mem_address: int, mem_value: int) -> None:
        '''Store mem_value in mem_address, taking into account the mask'''
        # Prepare the string to replace the 0's
        flip0_str = self.mask.replace('X', '1')
        flip0_int = int(flip0_str, base=2)
        mem_value = mem_value & flip0_int

        # Prepare the string to replace the 1's
        flip1_str = self.mask.replace('X', '0')
        flip1_int = int(flip1_str, base=2)
        mem_value = mem_value | flip1_int

        self.mem[mem_address] = mem_value


    def sum(self) -> int:
        # Return the sum of all values
        return sum(self.mem.values())


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    comp_sys = CompSystem()

    for line in lines:
        # If mask detedted
        if line[:4] == 'mask':
            # Update mask
            comp_sys.mask = line[7:]
            continue

        # Otherwise analyse line for operation
        m = re.fullmatch(r'mem\[(\d+)\] = (\d+)', line)
        # Address to write to
        mem_address = int(m.group(1))
        # Value to attempt writing
        mem_value = int(m.group(2))
        comp_sys.store_mem(mem_address, mem_value)

    return comp_sys.sum()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
