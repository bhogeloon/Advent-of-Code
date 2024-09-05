"""
Year 2020, Day 4

Problem description: See https://adventofcode.com/2020/day/4

We have the following classes:
- Passport: dict class. Contains all the key/value items in the passport
- Passports: List container class of Passport objects

Part 1: Look at all the keys and see if all the mandatory keys are in it.
"""

# Imports
from pprint import pprint
import re


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Passport(dict):
    '''Dict class Representing passport.'''

    # Class variables
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

    def __init__(self) -> None:
        pass


    def is_valid(self) -> bool:
        '''Checks if the passport is valid'''
        # Turn the keys into a set
        pp_keys = set(self.keys())

        # Check if all the mandatory keys are in the key_set
        if self.mandatory_fields.issubset(pp_keys):
            return True
        else:
            return False


class Passports(list[Passport]):
    '''List container class of Passport objects'''
    def __init__(self, lines: list[str]) -> None:
        current_pp = Passport()

        for (i, line) in enumerate(lines):
            # If empty line, Store Passport and create a new one to process
            if re.fullmatch(r'\s*', line):
                self.append(current_pp)
                current_pp = Passport()
                continue

            # Split line in whitespaces, to get seperate key, value pairs
            line_parts = line.split()

            for line_part in line_parts:
                # Split the key and value part
                (pp_key, pp_value) = line_part.split(':')
                # Store the key and value in current Passport
                current_pp[pp_key] = pp_value

            # If we are at the end of the file
            if len(lines) == i+1:
                self.append(current_pp)


    def get_valid_nr(self) -> int:
        '''Get the number of valid passports'''
        result = 0

        for passport in self:
            if passport.is_valid():
                result += 1

        return result

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    passports = Passports(lines)

    return passports.get_valid_nr()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
