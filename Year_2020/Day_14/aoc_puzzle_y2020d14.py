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

Part 2: Now we have change the memory address.
First replace all 1's (similar as above).
Then start maintaining a list of mem addresses starting with the one specified.
Then go bit by bit and if the mask has an X, add a new address flipping the bit
and that position.
Then store the value on all thos mem addresses and finally calculate the sum of
all memory values.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
import re

# Constants

MASK = []

for i in range(36):
    MASK.append(2**i)


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
        '''Return the sum of all values'''
        return sum(self.mem.values())


    def store_mem_v2(self, mem_address: int, mem_value: int) -> None:
        '''Store mem_value in mem_address, taking into account the mask as
        specified in part 2, so using it on the memory address.'''
        # Replace 1's
        flip1_str = self.mask.replace('X', '0')
        flip1_int = int(flip1_str, base=2)
        mem_address = mem_address | flip1_int

        # Make a list of all memory address to be stored to
        all_mems = [mem_address]
        # Make a binary representation of the mem addresss
        mem_address_bin = format(mem_address, '036b')

        for i in range(len(mem_address_bin)):
            # Floating address
            if self.mask[i] == 'X':
                # Preserve the length of the all_mems list
                all_mems_len = len(all_mems)
                # For each stored memory, add one with a different bit on the
                # i position
                for j in range(all_mems_len):
                    all_mems.append(all_mems[j] ^ MASK[35-i])
                    # print(i, j, all_mems[j], MASK[35-i], all_mems[-1])

        # Then store the same value in all the memory addresses
        for store_mem in all_mems:
            self.mem[store_mem] = mem_value


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    comp_sys = CompSystem()

    for line in lines:
        # If mask detected
        if line[:4] == 'mask':
            # Update active mask
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

    comp_sys = CompSystem()

    for line in lines:
        # If mask detected
        if line[:4] == 'mask':
            # Update active mask
            comp_sys.mask = line[7:]
            continue

        # Otherwise analyse line for operation
        m = re.fullmatch(r'mem\[(\d+)\] = (\d+)', line)
        # Initial address to write to
        mem_address = int(m.group(1))
        # Value to attempt writing
        mem_value = int(m.group(2))
        comp_sys.store_mem_v2(mem_address, mem_value)

    # pprint(comp_sys.mem)

    return comp_sys.sum()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
