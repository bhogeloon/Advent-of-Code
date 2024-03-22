"""
Year 2015, Day 1

Problem description: See https://adventofcode.com/2015/day/1

For part 1: just follow the input characters and go up or down one floor each time.

For part 2: stop as soon as you find floor = -1

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
def get_to_next_floor(floor: int, char: str) -> int:
    '''get to the next floor, up or down'''
    if char == '(':
        floor += 1
    elif char == ')':
        floor -=1
    else:
        raise RuntimeError('Unknown char: {}'.format(char))
    
    return floor


def get_floor(line: str) -> int:
    '''Determine floor based on input'''
    floor = 0

    for char in line:
        floor = get_to_next_floor(floor, char)        

    return floor


def find_basement_pos(line: str) -> int:
    '''Find position of char where we reach floor = -1'''
    floor = 0

    for i, char in enumerate(line):
        floor = get_to_next_floor(floor, char)

        if floor == -1:
            # Increase i as we start with pos 1, not 0
            return i+1

    raise RuntimeError("Basement not found.")


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    return get_floor(lines[0])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return find_basement_pos(lines[0])

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
