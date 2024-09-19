"""
Year 2021, Day 6

Problem description: See https://adventofcode.com/2021/day/6

The following classes are used:
- Fish: Represents a fish with days_left attribute (days left to reproduce)
- Fishes: List container class of Fish objects

Part 1: For every day, decrease days left of every fish. But if days_left is
already 0:
- Reset value to 6
- Create new Fish with days_left set to 8
"""

# Imports
from pprint import pprint


# Constants

TOTAL_DAYS = 80
DAYS_TO_REPRODUCE = 7
EXTRA_DAYS_NEW_FISH = 2


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Fish():
    '''Represents a fish with an attribute days_left (days left before it reproduces).'''
    def __init__(self, days_left: int) -> None:
        self.days_left = days_left


    def ready(self) -> bool:
        '''Returns True if Fish is ready to reproduce'''
        if self.days_left == 0:
            self.days_left = DAYS_TO_REPRODUCE - 1
            return True
        else:
            self.days_left -= 1
            return False


class Fishes(list[Fish]):
    '''List container class of Fish objects'''
    def __init__(self, line: str) -> None:
        nr_days = line.split(',')

        for nr_day in nr_days:
            self.append(Fish(int(nr_day)))


    def pass_day(self):
        '''Progress one day'''
        for i in range(len(self)):
            # If fish is ready to reproduce
            if self[i].ready():
                self.append(Fish(DAYS_TO_REPRODUCE + EXTRA_DAYS_NEW_FISH - 1))


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    fishes = Fishes(lines[0])

    for day in range(TOTAL_DAYS):
        fishes.pass_day()

    return len(fishes)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
