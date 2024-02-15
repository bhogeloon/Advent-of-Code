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

        self.adapters.sort()
        self.adapters.append(max(self.adapters)+3)

        self.current_joltage = 0
        self.nr_chains = 0


    def calculate_chain(self):
        nr_diff = {}
        for adapter in self.adapters:
            diff = adapter - self.current_joltage
            nr_diff[diff] = nr_diff.get(diff, 0) + 1
            self.current_joltage = adapter

        return nr_diff.get(1, 0) * nr_diff.get(3, 0)


    def _connect(self, index = 0) -> None:
        if index == len(self.adapters - 1):
            self.nr_chains += 1
            return

        for j in range(index+1, len(self.adapters)):
            if j - index > 3:
                break

            self._connect(j)


    def get_nr_of_chains(self) -> int:
        self.nr_chains = 0
        self._connect()

        return self.nr_chains


# Functions



# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    adapters = Adapters(lines)

    return adapters.calculate_chain()

    return __name__


if __name__ == '__main__':
    pass