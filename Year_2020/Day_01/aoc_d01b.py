"""
Year 2020, Day 1, Part 2

Problem description: See https://adventofcode.com/2020/day/1

My solution:
Part 1:

"""

# Imports

# Constants

# Global variables

from cmath import exp


class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

# Functions

# Main function
def get_solution(lines: list) -> int:
    '''Main function'''

    expenses = [ int(line) for line in lines ]

    for (i, expense_a) in enumerate(expenses):
        for (j, expense_b) in enumerate(expenses[i+1:]):
            for expense_c in expenses[j+1:]:
                if expense_a + expense_b + expense_c == 2020:
                    return expense_a * expense_b * expense_c

    raise RuntimeError("No result found.")

    return 0


if __name__ == '__main__':
    pass