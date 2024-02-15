"""
Year 2020, Day 14, Part 2

Problem description: See https://adventofcode.com/2020/day/14

"""

# Imports
from pprint import pprint
import re

# Constants

MASK = []

for i in range(36):
    MASK.append(2**i)


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


    def store_mem_v2(self, mem_address: int, mem_value: int) -> None:
        # Replace 1's
        flip1_str = self.mask.replace('X', '0')
        flip1_int = int(flip1_str, base=2)
        mem_address = mem_address | flip1_int

        all_mems = [mem_address]
        mem_address_bin = format(mem_address, '036b')

        for i in range(len(mem_address_bin)):
            if self.mask[i] == 'X':
                all_mems_len = len(all_mems)
                for j in range(all_mems_len):
                    all_mems.append(all_mems[j] ^ MASK[35-i])
                    # print(i, j, all_mems[j], MASK[35-i], all_mems[-1])

        for store_mem in all_mems:
            self.mem[store_mem] = mem_value


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
        comp_sys.store_mem_v2(mem_address, mem_value)

    # pprint(comp_sys.mem)

    return comp_sys.sum()

    return __name__


if __name__ == '__main__':
    pass