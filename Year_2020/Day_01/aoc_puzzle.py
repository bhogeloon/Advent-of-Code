"""
Year 2020, Day 1

Problem description: See https://adventofcode.com/2020/day/1

Part 1: Go through the list of expenses one by one and from there go
each time to the remaining list. As soon as the sum of the two result in
2020, return the product.

Part 2: Similar, but one level deeper.

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
    

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    expenses = [ int(line) for line in lines ]

    # For each expense
    for (i, expense_a) in enumerate(expenses):

        # Check sum for each remaining expense
        for expense_b in expenses[i+1:]:

            # If the two add up to 2020, return the product
            if expense_a + expense_b == 2020:
                return expense_a * expense_b

    raise RuntimeError("No result found.")

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    expenses = [ int(line) for line in lines ]

    # For each expense
    for (i, expense_a) in enumerate(expenses):

        # Then examine the remaining list
        for (j, expense_b) in enumerate(expenses[i+1:]):

            # Again examine the remaining list
            for expense_c in expenses[j+1:]:

                # If the three add up together to 2020, return
                # the product
                if expense_a + expense_b + expense_c == 2020:
                    return expense_a * expense_b * expense_c

    raise RuntimeError("No result found.")

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
