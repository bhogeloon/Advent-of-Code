"""
Year 2020, Day 4, Part 2

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
def check_year(year_str: str, min_val: int, max_val: int) -> bool:
    '''Checks if the year format is correct and in between the values'''

    if re.fullmatch('\d{4}', year_str):
        year_int = int(year_str)
        if year_int < min_val or year_int > max_val:
            return False
        else:
            return True
    else:
        return False


def validate_pp_values(passport: dict) -> bool:
    '''Return True if all values are correct'''

    # Constants
    ECL_VALS = (
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth',
    )

    if not check_year(passport['byr'], 1920, 2002):
        return False

    if not check_year(passport['iyr'], 2010, 2020):
        return False

    if not check_year(passport['eyr'], 2020, 2030):
        return False

    if re.fullmatch(r'\d+cm', passport['hgt']):
        hgt_int = int(passport['hgt'][:-2])
        if hgt_int < 150 or hgt_int > 193:
            return False
    elif re.fullmatch(r'\d+in', passport['hgt']):
        hgt_int = int(passport['hgt'][:-2])
        if hgt_int < 59 or hgt_int > 76:
            return False
    else:
        return False

    if not re.fullmatch(r'#[0-9a-f]{6}', passport['hcl']):
        return False

    if passport['ecl'] not in ECL_VALS:
        return False

    if not re.fullmatch(r'\d{9}', passport['pid']):
        return False

    return True


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
            if validate_pp_values(passport):
                valid_pps += 1

    return valid_pps

    return 'day 4b'


if __name__ == '__main__':
    pass