"""
Year 2020, Day 9

Problem description: See https://adventofcode.com/2020/day/9

The following class is being used:
- XmasSeq: List class of XMAS sequence numbers.

Part 1:
Check for all numbers (skipping the preamble) whether any combination of the
past 25 numbers add up with this number as result. As soon as one is found for
which this is not possible, report that number.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger

# Constants

PREAMBLE = 25
PREAMBLE_TEST = 5

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

class XmasSeq(list[int]):
    '''List class of XMAS sequence numbers'''

    def __init__(self, lines: list[str]) -> None:
        # Pre-amble size
        if Gv.test:
            self.preamble = PREAMBLE_TEST
        else:
            self.preamble = PREAMBLE

        Gv.log.debug(f'Preamble: {self.preamble}')

        for line in lines:
            self.append(int(line))


    def _check_number(self, nr: int) -> bool:
        '''Check validity of one number'''

        # For all previous 25 numbers
        for i in range(nr-self.preamble-1, nr-1):

            # For all remaining numbers
            for j in range(i+1, nr):

                # If the sum is correct, number is valid
                if self[nr] == self[i] + self[j]:
                    Gv.log.debug(f'{self[i]}+{self[j]}={self[nr]}')
                    return True

        return False


    def validate(self) -> int:
        '''Return first number found which is invalid.
        Return -1 if no invalid number is found'''

        # For all numbers after the preamble
        for nr in range(self.preamble+1, len(self)):

            # If not valid, return number
            if not self._check_number(nr):
                return self[nr]

        raise RuntimeError('All numbers are valid')


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)
    print(Gv.test, Gv.log)

    xmas_seq = XmasSeq(lines)

    return xmas_seq.validate()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
