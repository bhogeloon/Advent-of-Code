"""
Year 2022, Day 3, Part 2

Problem description: See https://adventofcode.com/2022/day/3

The following classes are used:
- Rucksack: This contains sets of items for comp1 and comp2
- Elfgroup: This is a list class containing three rucksacks (for each elf group)

For part 1: get the common items for comp1 and comp2, check if it is exactly one
and then determine the priority (based on the ASCII value).

For part 2: Create an Elfgroup object for each three elves and then find the single
common item. Then get the priority of that one.

"""

# Imports
from pprint import pprint


# Constants

ASCII_LOWER_BASE = ord('a') - 1
ASCII_UPPER_BASE = ord('A') - 1


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Rucksack():
    '''Rucksack containg two compartments'''

    def __init__(self, line:str) -> None:
        self.line = line
        line_size = len(line)

        if line_size % 2 > 0:
            raise RuntimeError('uneven amount of items: {}'.format(line))

        self.comp1 = set(line[:line_size//2])
        self.comp2 = set(line[line_size//2:])
        # Get sum of all items
        self.all_comps = self.comp1 | self.comp2
        # print(line, str(self.comp1), str(self.comp2))

        return


    def get_common_item(self) -> None:
        '''Collect all common items'''
        common_items = self.comp1 & self.comp2

        # If no common items found
        if len(common_items) == 0:
            raise RuntimeError('No common items found: {}'.format(self.line))

        # If more than one common item found
        if len(common_items) > 1:
            raise RuntimeError('More than one common item found: {}.'.format(self.line))

        # Extract the one common item
        self.common_item = common_items.pop()

        return


    def get_priority(self) -> int:
        '''get the priority of the common item'''

        return get_item_priority(self.common_item)


class ElfGroup(list[Rucksack]):
    '''Group of 3 rucksacks'''

    def get_common_item(self) -> None:
        '''Get the common item of all three rucksacks'''
        common_items = self[0].all_comps & self[1].all_comps & self[2].all_comps

        if len(common_items) == 0:
            raise RuntimeError('No common items found: {}'.format(self.line))

        if len(common_items) > 1:
            raise RuntimeError('More than one common item found: {}.'.format(self.line))

        self.common_item = common_items.pop()

        return


    def get_priority(self) -> int:
        '''get the priority of the common item'''

        return get_item_priority(self.common_item)


# Functions

def get_item_priority(char: str) -> int:
    '''function to get prio of a character'''

    if char.isupper():
        return ord(char) - ASCII_UPPER_BASE + 26
    else:
        return ord(char) - ASCII_LOWER_BASE


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    prio_sum = 0

    for line in lines:
        rucksack = Rucksack(line)
        rucksack.get_common_item()
        prio_sum += rucksack.get_priority()

    return prio_sum

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    prio_sum = 0

    for i in range(0, len(lines), 3):
        rucksacks = ElfGroup()

        for j in range(i, i+3):
            rucksacks.append(Rucksack(lines[j]))

        rucksacks.get_common_item()
        prio_sum += rucksacks.get_priority()

    return prio_sum

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
