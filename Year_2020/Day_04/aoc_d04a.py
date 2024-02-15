"""
Year 2020, Day 4, Part 1

Problem description: See https://adventofcode.com/2020/day/4

My solution:
Part 1:

"""

# Imports
from pprint import pprint
import re

# Constants
mandatory_fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
}

optional_fields = {
    'cid',
}

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

# Functions
def read_passports(lines: list) -> list:
    '''Read input and return list of passports'''

    passports = []
    current_pp = {}

    for (i, line) in enumerate(lines):
        if re.fullmatch(r'\s*', line):
            passports.append(current_pp)
            current_pp = {}
            continue

        line_parts = line.split()

        for line_part in line_parts:
            (pp_key, pp_value) = line_part.split(':')
            current_pp[pp_key] = pp_value

        if len(lines) == i+1:
            passports.append(current_pp)
    
    return passports


# Main function
def get_solution(lines: list) -> int:
    '''Main function'''

    passports = read_passports(lines)
    print(len(passports))

    valid_pps = 0

    for passport in passports:
        pp_keys = set(passport.keys())

        # if pp_keys - optional_fields == mandatory_fields:
        if mandatory_fields.issubset(pp_keys):
            valid_pps += 1

    return valid_pps


if __name__ == '__main__':
    pass