"""
Year 2021, Day 10

Problem description: See https://adventofcode.com/2021/day/10

The following classes are used:
- Chunks: Represents a line in the Navigational Subsystem
- NavigationalSubsystem: A list container class of Chunks objects

Part 1: For each line, create a stack. The is filled with the open character and
the upper stack entry will be removed again if the closing character is
found. If a non-matching closing character is found, it means that the line
is corrupt. The score is then updated with the matching character and
then we move on to the next line.
At the end of each line, the stack should be empty, otherwise we have
an incomplete line. For part 1, this can be ignored, so just return score 0.

Part 2:
So now we keep the same code to check for corrupt lines, but instead
of keeping the score, we just ignore them.
For the ones that make it to the end, we will investigate the remaining 
characters in the stack and calculate all the score for those by peeling off the
remainder of the stack.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger

# Constants

CORRUPT_SCORE_TABLE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

MATCH_TABLE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

COMPL_SCORE_TABLE = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


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

class Chunks:
    '''A line with several chunks'''
    def __init__(self, line: str) -> None:
        self.line = line
        # The stack of chunks
        self.chunk_stack = []


    def get_invalid_score(self) -> int:
        '''Get the score of all invalid trunks in this line'''
        for char in self.line:
            # If opening character, store it and continue
            if char in MATCH_TABLE.keys():
                self.chunk_stack.append(char)
                continue

            # Now investigate closing brackets one by one
            # If this is the first char, return the matching score
            if len(self.chunk_stack) == 0:
                return CORRUPT_SCORE_TABLE[char]
            
            # else if the character matches the current opening bracket
            # continue with the rest of the line
            if char == MATCH_TABLE[self.chunk_stack.pop()]:
                continue

            # else return score
            return CORRUPT_SCORE_TABLE[char]
        
        # If nothing invalid find, return 0
        return 0


    def get_completion_score(self) -> int:
        '''Return the completion score result for this line'''
        Gv.log.debug(f'{self.line}: {self.chunk_stack}')

        line_score = 0

        for i in range(len(self.chunk_stack)):
            line_score *= 5
            line_score += COMPL_SCORE_TABLE[self.chunk_stack.pop()]

        return line_score


class NavigationalSubsystem(list[Chunks]):
    '''List container class of Chunks objects'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Chunks(line))


    def get_invalid_score(self) -> int:
        '''Return the total score of invalid chunks'''
        total = 0

        for chunks in self:
            total += chunks.get_invalid_score()

        return total


    def get_completion_score(self) -> int:
        '''Return the middle score of all completion score results'''
        all_results = []

        for chunks in self:
            inv_score = chunks.get_invalid_score()

            # If not an invalid score it will be 0
            if inv_score == 0:
                all_results.append(chunks.get_completion_score())

        return middle_score(all_results)
    

# Functions

def middle_score(my_list: list) -> int:
    '''This function determines the middle score of a list
    of integers'''
    list_len = len(my_list)

    # Raise exception if not on odd number
    if (list_len % 2) == 0:
        raise RuntimeError("Even number of scores: {}".format(list_len))

    # Sort the list
    my_list.sort()

    # Determine the middle entry
    middle = list_len // 2

    Gv.log.debug(f'{list_len} {middle}')

    for my_value in my_list:
        Gv.log.debug(my_value)

    return my_list[middle]


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    system = NavigationalSubsystem(lines)

    return system.get_invalid_score()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    system = NavigationalSubsystem(lines)

    return system.get_completion_score()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
