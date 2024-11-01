"""
Year 2021, Day 8

Problem description: See https://adventofcode.com/2021/day/8

The following classes are used:
- Signal: Has an input and output attibute. Each of them contains a list of
    strings
- Signals: List container class of Signal objects.

Part 1: Check for each output digit if the length indicates that it is a 
digit with a unique pattern length.
"""

# Imports
from __future__ import annotations
from pprint import pprint


# Constants
# The digits which have a unique number of display units
UNIQUE_PATTERN = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Signal:
    '''A signal has an input and output attribute'''

    def __init__(self, line: str) -> None:
        (input_str, output_str) = line.split(' | ')
        self.input = input_str.split()
        self.output = output_str.split()


    def get_unique_digits(self) -> int:
        '''Return the amount of unique digits in the output field'''
        nr_of_hits = 0

        for digit in self.output:
            if len(digit) in UNIQUE_PATTERN.values():
                nr_of_hits += 1

        return nr_of_hits


class Signals(list[Signal]):
    '''List container class of Signal attributes'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Signal(line))


    def get_unique_digits(self) -> int:
        '''Return the amount of unique digits in the output fields.'''
        nr_of_hits = 0

        for signal in self:
            nr_of_hits += signal.get_unique_digits()

        return nr_of_hits


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    signals = Signals(lines)

    return signals.get_unique_digits()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
