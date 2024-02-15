"""
Year 2020, Day 5, Part 1

Problem description: See https://adventofcode.com/2020/day/5

My solution:
Part 1:

"""

# Imports
from pprint import pprint


# Constants

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

# Functions
# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    seats = []

    for line in lines:
        line = line.replace('F', '0')
        line = line.replace('B', '1')
        line = line.replace('L', '0')
        line = line.replace('R', '1')

        seat_nr = int(line, base=2)
        seats.append(seat_nr)

    return max(seats)

    return 'day 5a'


if __name__ == '__main__':
    pass