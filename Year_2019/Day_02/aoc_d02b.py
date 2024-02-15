"""
Year 2019, Day 1, Part 2

Problem description: See https://adventofcode.com/2019/day/2

"""

# Imports
from copy import deepcopy
from ctypes import pointer
from pprint import pprint

# Constants

TARGET_VALUE = 19690720

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Intcode():
    def __init__(self, line:str) -> None:
        self.codes = [ int(nr) for nr in line.split(',') ]
        self.ptr = 0


    def fix(self, val1 = 12, val2 = 2) -> None:
        self.codes[1] = val1
        self.codes[2] = val2


    def run_program(self) -> int:
        while True:
            if self.codes[self.ptr] == 99:
                return self.codes[0]

            arg1 = self.codes[self.codes[self.ptr+1]]
            arg2 = self.codes[self.codes[self.ptr+2]]
            store_loc = self.codes[self.ptr+3]

            if self.codes[self.ptr] == 1:
                self.codes[store_loc] = arg1 + arg2
 
            elif self.codes[self.ptr] == 2:
                self.codes[store_loc] = arg1 * arg2

            else:
                raise RuntimeError("Unknown operator {}.".format(self.codes[self.ptr]))

            self.ptr += 4


# Functions




# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    intcode = Intcode(lines[0])

    for noun in range(100):
        for verb in range(100):
            new_intcode = deepcopy(intcode)
            new_intcode.fix(noun, verb)
            if new_intcode.run_program() == TARGET_VALUE:
                return 100 * noun + verb
  
    return __name__


if __name__ == '__main__':
    pass