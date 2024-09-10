"""
Year 2022, Day 5

Problem description: See https://adventofcode.com/2022/day/5

Please note that for this puzzle I slightly modified the puzzle input
manually to be able to read it more easily (that is: line by line in stead
of top to bottom).

The following classes are used:
- Stack: A stack of crates (list class)
- Stacks: List container class of Stack objects.

Part 1: I started with creating the Stack objects using the first part
of the puzzle input.
Then I start to process each instruction line, moving them one at the time.
Finally I just get all the top crates and report them.

Part 2:
Exactly the same, but instead of moving them one at the time, we're taking
all of the crates in each step and put them on top of the new stack in the
same order.
"""

# Imports
from pprint import pprint
import re

# Constants

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Stack(list):
    '''Stack of crates'''

    def __init__(self, line: str, i:int) -> None:
        self.extend(line.split())
        # Store index
        self.i = i
        return


    def get_top_crate(self) -> str:
        return self[-1]


class Stacks(dict):
    '''Container class of stacks'''

    def __init__(self, lines: list[str]) -> None:
        '''Get all stack info from input'''
        for i in range(1,10):
            self[i] = Stack(lines[i], i)

        return


    def move_crates(self, line: str) -> None:
        '''Move crates based on the instruction line'''

        m = re.match(r'move (\d+) from (\d+) to (\d+)', line)

        amount = int(m.group(1))
        from_stack = int(m.group(2))
        to_stack = int(m.group(3))

        for i in range(amount):
            crate = self[from_stack].pop()
            self[to_stack].append(crate)

        return


    def move_crates_9001(self, line: str) -> None:
        '''Move crates based on the instruction line
        using the multiple crates crane'''

        m = re.match(r'move (\d+) from (\d+) to (\d+)', line)

        amount = int(m.group(1))
        from_stack = int(m.group(2))
        to_stack = int(m.group(3))

        crates = self[from_stack][-amount:]
        del self[from_stack][-amount:]
        self[to_stack] += crates

        return


    def get_top_crates(self) -> str:
        top_crates = ''

        for i in range(1, len(self)+1):
            top_crates += self[i].get_top_crate()

        return top_crates



# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    stacks = Stacks(lines)

    del lines[:11]

    for line in lines:
        stacks.move_crates(line)

    return stacks.get_top_crates()

    # return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    stacks = Stacks(lines)

    del lines[:11]

    for line in lines:
        stacks.move_crates_9001(line)

    return stacks.get_top_crates()

    # return 'part_2 ' + __name__


if __name__ == '__main__':
    pass