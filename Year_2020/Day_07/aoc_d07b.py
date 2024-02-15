"""
Year 2020, Day 7, Part 2

Problem description: See https://adventofcode.com/2020/day/7

My solution:
Part 1:

"""

# Imports
from pprint import pprint
import re

# Constants
CHECK_COLOUR = 'shiny gold'

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

# Functions

def read_bags(lines: list[str]) -> dict[str]:
    '''Return a dict of bags'''

    bags = {}

    for line in lines:
        m = re.fullmatch(r'(.*) bags contain (.*)\.', line)

        bag_key = m.group(1)
        bag_value_parts = m.group(2).split(', ')

        bag_values = {}

        for bag_value_part in bag_value_parts:

            if bag_value_part == 'no other bags':
                break

            m = re.fullmatch(r'(\d+) (.*) bags?', bag_value_part)

            cont_amount = int(m.group(1))
            cont_bag = m.group(2)

            bag_values[cont_bag] = cont_amount

        bags[bag_key] = bag_values

    return bags


def check_bag(bags: dict, bag_col: str) -> bool:
    '''Check the bag to see if the interesting color is there'''

    if CHECK_COLOUR in bags[bag_col].keys():
        return True

    for contain_bag_col in bags[bag_col].keys():
        if check_bag(bags, contain_bag_col):
            return True
    
    return False


def get_nr_of_bags(bags: dict, bag_col: str) -> int:
    '''Return the number of bags in the bag'''

    nr_of_bags = 1

    for contain_col in bags[bag_col].keys():
        nr_of_bags += bags[bag_col][contain_col] * get_nr_of_bags(bags, contain_col)

    return nr_of_bags


# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    bags = read_bags(lines)

    return get_nr_of_bags(bags, CHECK_COLOUR) - 1

    return __name__


if __name__ == '__main__':
    pass