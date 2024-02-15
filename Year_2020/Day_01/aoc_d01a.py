"""
Year 2020, Day 1, Part 1

Problem description: See https://adventofcode.com/2020/day/1

My solution:
Part 1:

"""

# Imports

# Constants

# Global variables

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
        for expense_b in expenses[i+1:]:
            if expense_a + expense_b == 2020:
                return expense_a * expense_b

    raise RuntimeError("No result found.")

    return 0


if __name__ == '__main__':
    pass