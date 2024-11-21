"""
Year 2020, Day 9

Problem description: See https://adventofcode.com/2020/day/9

The following class is being used:
- XmasSeq: List class of XMAS sequence numbers.

Part 1:
Check for all numbers (skipping the preamble) whether any combination of the
past 25 numbers add up with this number as result. As soon as one is found for
which this is not possible, report that number.

Part 2:
Consider the number found in Part 1. Now go through the list of numbers again
and for each number, look at the numbers immediately following that one. Add
all those numbers together until you either find the right ('invalid') number,
or you exceed it. Once you find it, look at all the numbers you have added
together and take the max and min and add them together.

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


    def find_weakness(self) -> int:
        '''Find the weakness'''

        # Find invalid number (so part 1)
        invalid_nr =  self.validate()

        # Go through all numbers
        for (i, nr) in enumerate(self):
            # The sum to be checked
            total = nr
            nrs = [nr]
            sum_found = False

            # Go through the remainder of numbers and add them to the total
            # one by one, until we either find the right number or we go
            # over it (as the numbers should be contiguous)
            for j in range(i+1, len(self)):
                # Increase sum
                total += self[j]
                nrs.append(self[j])

                # If total matches
                if total == invalid_nr:
                    sum_found = True
                    break
                # If total exceeds invalid number
                elif total > invalid_nr:
                    break

            # If we found the number, we add up the min and max
            if sum_found:
                return max(nrs) + min(nrs)

        raise RuntimeError('No match found')


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    xmas_seq = XmasSeq(lines)

    return xmas_seq.validate()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    xmas_seq = XmasSeq(lines)

    return xmas_seq.find_weakness()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
