"""
Year 2020, Day 6, Part 1

Problem description: See https://adventofcode.com/2020/day/6

My solution:
Part 1:

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

# Functions
def read_group_answers(lines: list[str]) -> list:
    '''Read input and return list of passports'''

    groups = []
    answers = set()

    for (i, line) in enumerate(lines):
        if re.fullmatch(r'\s*', line):
            groups.append(answers)
            answers = set()
            continue

        answers |= set(line)

        if len(lines) == i+1:
            groups.append(answers)
    
    return groups


# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    groups = read_group_answers(lines)

    sum_of_answers = 0

    for group in groups:
        sum_of_answers += len(group)

    return sum_of_answers

    return __name__


if __name__ == '__main__':
    pass