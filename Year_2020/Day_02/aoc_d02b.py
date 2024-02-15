"""
Year 2020, Day 2, Part 2

Problem description: See https://adventofcode.com/2020/day/2

My solution:
Part 2:

"""

# Imports
import re

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

    valid_pwd_count = 0

    for line in lines:
        m = re.fullmatch(r'(\d+)-(\d+)\s+([a-z]):\s+([a-z]+)', line)

        if not m:
            raise RuntimeError("No match found for {}".format(line))

        # change!!!
        min_pos = int(m[1]) - 1
        max_pos = int(m[2]) - 1
        char = m[3]
        password = m[4]

        if password[min_pos] == char and password[max_pos] == char:
            pass
        elif password[min_pos] == char or password[max_pos] == char:
            valid_pwd_count += 1

    return valid_pwd_count


if __name__ == '__main__':
    pass