"""
Year 2020, Day 2, Part 1

Problem description: See https://adventofcode.com/2020/day/2

My solution:
Part 1:

"""

# Imports
import re
from collections import Counter

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

        min_occ = int(m[1])
        max_occ = int(m[2])
        char = m[3]
        password = m[4]

        c = Counter(password)
        act_occ = c[char]

        if act_occ >= min_occ and act_occ <= max_occ:
            valid_pwd_count += 1

    return valid_pwd_count


if __name__ == '__main__':
    pass