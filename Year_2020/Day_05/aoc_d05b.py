"""
Year 2020, Day 5, Part 2

Problem description: See https://adventofcode.com/2020/day/5

My solution:
Part 1:

"""

# Imports
from pprint import pprint


# Constants

MAX_SEAT_NR = int('1111111111', base=2)

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


    all_seats = []

    for i in range(MAX_SEAT_NR + 1):
        if i in seats:
            all_seats.append(True)
        else:
            all_seats.append(False)

    for i in range(1, MAX_SEAT_NR):
        if not all_seats[i]:
            if all_seats[i-1] and all_seats[i+1]:
                return i

    raise RuntimeError("No empty seat found.")

    return 'day 5b'


if __name__ == '__main__':
    pass