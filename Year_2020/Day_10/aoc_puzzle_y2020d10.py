"""
Year 2020, Day 10

Problem description: See https://adventofcode.com/2020/day/10

The following class is used:
- Adapters: List class representing the joltage values of the adapters.

Part 1: First sort the list on joltage level and then add the built in device
(max+3). Then walk through the list, registering the amount of times the 
difference is either 1, 2 or 3. Then at the end mulitply the 1 and 3 values.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger

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

class Adapters(list):
    '''List class of adapter joltages'''
    def __init__(self, lines: list[str]) -> None:
        # Read in all adapters
        for line in lines:
            self.append(int(line))

        # Sort them, so they can be processed in order (so not to skip any)
        self.sort()
        # Add the built-in adapter: max+3
        self.append(max(self.adapters)+3)

        # Current output joltage
        self.current_joltage = 0
        self.nr_chains = 0


    def calculate_chain(self):
        '''Return the product of the amount of 1-joltage diffences and
        3-joltage differences (the answer to part 1)'''
        # Keep track of the number of times the difference is 1,2 and 3
        nr_diff = {}

        for adapter in self:
            diff = adapter - self.current_joltage
            # Increase the diff counter or create one if it doesn't exist
            nr_diff[diff] = nr_diff.get(diff, 0) + 1
            # Update the current joltage
            self.current_joltage = adapter

        return nr_diff.get(1, 0) * nr_diff.get(3, 0)


    def _connect(self, index = 0) -> None:
        if index == len(self) - 1:
            self.nr_chains += 1
            return

        for j in range(index+1, len(self)):
            if j - index > 3:
                break

            self._connect(j)


    def get_nr_of_chains(self) -> int:
        self.nr_chains = 0
        self._connect()

        return self.nr_chains


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    adapters = Adapters(lines)

    return adapters.calculate_chain()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
