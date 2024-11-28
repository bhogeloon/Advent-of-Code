"""
Year 2020, Day 10

Problem description: See https://adventofcode.com/2020/day/10

The following class is used:
- Adapters: List class representing the joltage values of the adapters.

Part 1: First sort the list on joltage level and then add the built in device
(max+3). Then walk through the list, registering the amount of times the 
difference is either 1, 2 or 3. Then at the end mulitply the 1 and 3 values.

Part 2: For this we use a recursive function. To calculate the number of chains
possible, we look at each next value within the range of 3 and calculate the 
number of chains from there, and so on, until we reach the end.
To prevent that we make the same recursive calculation over and over again, we
keep track of the result from each index. This way, the result could be
calculated in less than 0.05 seconds.

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

        # Add 0 as a start value
        self.append(0)
        # Add the built-in adapter: max+3
        self.append(max(self)+3)
        # Sort them, so they can be processed in order (so not to skip any)
        self.sort()

        # Current output joltage
        self.current_joltage = 0

        # Register the different chains starting from a certain index in 
        # the list
        self.chains_from_here = {}


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


    def get_nr_of_chains(self, index=0) -> int:
        '''Recursive function to calculate the number of chains from a 
        given list index'''
        # if at the end of the chain
        if index == len(self) - 1:
            return 1

        # If the number for the chain has already been calculated
        if index in self.chains_from_here.keys():
            return self.chains_from_here[index]

        nr_of_chains = 0

        # Go through the remainder of the list from this index
        for j in range(index+1, len(self)):
            # Stop as soon as the difference is larger than 3
            if self[j] - self[index] > 3:
                break

            # Start calculating from the next position
            nr_of_chains += self.get_nr_of_chains(j)

        # Register the amount chains from this index
        self.chains_from_here[index] = nr_of_chains

        return nr_of_chains


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

    adapters = Adapters(lines)

    return adapters.get_nr_of_chains()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
