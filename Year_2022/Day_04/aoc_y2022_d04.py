"""
Year 2022, Day 4

Problem description: See https://adventofcode.com/2022/day/4

"""

# Imports
from pprint import pprint

# Constants

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Elf_pair():
    '''Pair of Elves whith assigned sections per Elf'''

    def __init__(self, line: str) -> None:
        lineparts = line.split(',')
        self.elf_sections = []

        for linepart in lineparts:
            (start_sec, end_sec) = [ int(x) for x in linepart.split('-') ]
            range_sec = [ x for x in range(start_sec, end_sec+1) ]
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


# Main functions
def get_solution_part1(lines: list[str]) -> int:
    '''Main function'''

    counter = 0

    for line in lines:
        elf_pair = Elf_pair(line)

        if elf_pair.contains():
            counter += 1

    return counter

    # return 'part_1 ' + __name__


def get_solution_part2(lines: list[str]) -> int:
    '''Main function'''

    counter = 0

    for line in lines:
        elf_pair = Elf_pair(line)

        if elf_pair.overlap():
            counter += 1

    return counter

    # return 'part_2 ' + __name__


if __name__ == '__main__':
    pass