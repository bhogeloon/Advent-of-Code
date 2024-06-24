"""
Year 2022, Day 4

Problem description: See https://adventofcode.com/2022/day/4

We use the following class:
- ElfPair: Pair of elves, each responsible for one section

Part 1: Check for each pair if one is completely part of the other or vice versa.

Part 2: Determine the shared sections and see if that is empty or not.
"""

# Imports
from pprint import pprint


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Elf_pair():
    '''Pair of Elves whith assigned sections per Elf'''

    def __init__(self, line: str) -> None:
        lineparts = line.split(',')
        self.elf_sections = []

        for linepart in lineparts:
            # Determin start and end of range
            (start_sec, end_sec) = [ int(x) for x in linepart.split('-') ]
            # Define the range itself
            range_sec = [ x for x in range(start_sec, end_sec+1) ]
            # Assign the range to a section (one Elf)
            self.elf_sections.append(set(range_sec))

        return


    def contains(self) -> bool:
        '''Check if one section completely contains the other'''
        check1 = self.elf_sections[0] <= self.elf_sections[1]
        check2 = self.elf_sections[0] >= self.elf_sections[1]
        return check1 or check2


    def overlap(self) -> bool:
        '''Check if there is overlap at all'''

        shared_secs = self.elf_sections[0] & self.elf_sections[1]

        return len(shared_secs) > 0


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    counter = 0

    for line in lines:
        elf_pair = Elf_pair(line)

        # If one fully contains the other, increase counter
        if elf_pair.contains():
            counter += 1

    return counter

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    counter = 0

    for line in lines:
        elf_pair = Elf_pair(line)

        if elf_pair.overlap():
            counter += 1

    return counter

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
