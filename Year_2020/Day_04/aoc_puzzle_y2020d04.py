"""
Year 2020, Day 4

Problem description: See https://adventofcode.com/2020/day/4

We have the following classes:
- Passport: dict class. Contains all the key/value items in the passport
- Passports: List container class of Passport objects

Part 1: Look at all the keys and see if all the mandatory keys are in it.

Part 2: First do the part 1 check and then check the specific attributes one
by one.
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

    ECL_VALS = (
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth',
    )
   

    def __init__(self) -> None:
        pass


    def is_valid_p1(self) -> bool:
        '''Checks if the passport is valid (according the part 1 rules)'''
        # Turn the keys into a set
        pp_keys = set(self.keys())

        # Check if all the mandatory keys are in the key_set
        if self.mandatory_fields.issubset(pp_keys):
            return True
        else:
            return False


    def is_valid_p2(self) -> bool:
        '''Checks if the passport is valid (according the part 2 rules)'''
        # Check if all mandatory fields are actually there
        if not self.is_valid_p1():
            return False
        
        # Check byr
        if not self.check_year(self['byr'], 1920, 2002):
            return False

        # Check iyr
        if not self.check_year(self['iyr'], 2010, 2020):
            return False

        # Check eyr
        if not self.check_year(self['eyr'], 2020, 2030):
            return False

        # Check hgt
        if re.fullmatch(r'\d+cm', self['hgt']):
            hgt_int = int(self['hgt'][:-2])
            if hgt_int < 150 or hgt_int > 193:
                return False
        elif re.fullmatch(r'\d+in', self['hgt']):
            hgt_int = int(self['hgt'][:-2])
            if hgt_int < 59 or hgt_int > 76:
                return False
        else:
            return False

        # Check hcl
        if not re.fullmatch(r'#[0-9a-f]{6}', self['hcl']):
            return False

        # Check ecl
        if self['ecl'] not in self.ECL_VALS:
            return False

        # Check pid
        if not re.fullmatch(r'\d{9}', self['pid']):
            return False

        return True


    def check_year(self, year_str: str, min_val: int, max_val: int) -> bool:
        '''Checks if the year format is correct and in between the values'''

        if re.fullmatch('\d{4}', year_str):
            year_int = int(year_str)
            if year_int < min_val or year_int > max_val:
                return False
            else:
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


    def get_valid_nr_p1(self) -> int:
        '''Get the number of valid passports (according the part 1 rules)'''
        result = 0

        for passport in self:
            if passport.is_valid_p1():
                result += 1

        return result


    def get_valid_nr_p2(self) -> int:
        '''Get the number of valid passports (according the part 2 rules)'''
        result = 0

        for passport in self:
            if passport.is_valid_p2():
                result += 1

        return result


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    passports = Passports(lines)

    return passports.get_valid_nr_p1()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    passports = Passports(lines)

    return passports.get_valid_nr_p2()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
