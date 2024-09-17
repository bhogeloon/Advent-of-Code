"""
Year 2019, Day 2

Problem description: See https://adventofcode.com/2019/day/2

We have a single class called Intcode, representing the Integer Code of the computer.

For part 1, we first replace the 1 and 2 positions with the values that are provided in 
part 1. Then we go through the program, replacing values in the list by making the 
computation on the values of the locations given in argument 1 and 2 and store the result
in the location given in argument 3.
As soon as we get to 99, halt program and return the value in position 0.

For part 2, we run exactly the same program, but we try a different input combination for
the fix each time. As soon as we hit the right value, we return the result.
(Note that part 2 does not run with the test input).
"""

# Imports
from pprint import pprint
from copy import deepcopy


# Constants

# The result value that we are looking for 
TARGET_VALUE = 19690720

# Maximum range of values of verbs and nouns to be looking for
MAX_RANGE = 100

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Intcode():
    def __init__(self, line:str) -> None:
        self.codes = [ int(nr) for nr in line.split(',') ]
        # Indicates where the program is
        self.ptr = 0


    def fix(self, val1 = 12, val2 = 2) -> None:
        '''Fix the initial values'''
        self.codes[1] = val1
        self.codes[2] = val2


    def run_program(self) -> int:
        '''Run through the program and return value in position 0'''
        while True:
            # If we detect value 99, end program
            if self.codes[self.ptr] == 99:
                return self.codes[0]

            # Get the arguments and the store location
            arg1 = self.codes[self.codes[self.ptr+1]]
            arg2 = self.codes[self.codes[self.ptr+2]]
            store_loc = self.codes[self.ptr+3]

            # If opcode = 1, add the args
            if self.codes[self.ptr] == 1:
                self.codes[store_loc] = arg1 + arg2
 
            # If opcode = 2, multiply the args
            elif self.codes[self.ptr] == 2:
                self.codes[store_loc] = arg1 * arg2

            else:
                raise RuntimeError("Unknown operator {}.".format(self.codes[self.ptr]))

            # Jump ahead 4 positions
            self.ptr += 4


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    intcode = Intcode(lines[0])

    # Make initial correction, but not on the test input
    if not Gv.test:
        intcode.fix()

    return intcode.run_program()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    intcode = Intcode(lines[0])

    # Try out all combination
    for noun in range(MAX_RANGE):
        for verb in range(MAX_RANGE):
            # Make a copy, so you can start with the original in the
            # next loop
            new_intcode = deepcopy(intcode)
            # Then do the fix with this combination
            new_intcode.fix(noun, verb)

            # If we hit the right value, return the formula
            if new_intcode.run_program() == TARGET_VALUE:
                return 100 * noun + verb

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
