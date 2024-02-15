"""
Year 2020, Day 10, Part 1

Problem description: See https://adventofcode.com/2020/day/9

"""

# Imports
from pprint import pprint
from sqlite3 import adapters

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes
class Adapters():
    def __init__(self, lines: list[str]) -> None:
        self.adapters = []

        for line in lines:
            self.adapters.append(int(line))

        self.adapters.append(max(self.adapters)+3)
        self.adapters.append(0)
        self.adapters.sort()

        self.current_joltage = 0

        self.chains_from_here = {}


    def calculate_chain(self):
        nr_diff = {}
        for adapter in self.adapters:
            diff = adapter - self.current_joltage
            nr_diff[diff] = nr_diff.get(diff, 0) + 1
            self.current_joltage = adapter

        return nr_diff.get(1, 0) * nr_diff.get(3, 0)


    def _connect(self, index = 0) -> int:
        if index == len(self.adapters) - 1:
            return 1

        if index in self.chains_from_here.keys():
            return self.chains_from_here[index]

        nr_of_chains = 0

        for j in range(index+1, len(self.adapters)):
            if self.adapters[j] - self.adapters[index] > 3:
                break

            nr_of_chains += self._connect(j)

        self.chains_from_here[index] = nr_of_chains

        return nr_of_chains


    def get_nr_of_chains(self) -> int:
        return self._connect()


# Functions



# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    adapters = Adapters(lines)

    return adapters.get_nr_of_chains()

    return __name__


if __name__ == '__main__':
    pass