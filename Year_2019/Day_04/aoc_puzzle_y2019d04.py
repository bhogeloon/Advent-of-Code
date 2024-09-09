"""
Year 2019, Day 4

Problem description: See https://adventofcode.com/2019/day/4

The following classes are used:
- Passwd: str class containing a password

Part 1: We just keep track of the valid passwords using the Passwd methods.
Part 2: Use a modified function for the double char check

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

class Passwd(str):
    '''This is a str class which contains a password'''
    def check_double(self):
        '''Returns True if a double value is detected'''
        prev_char = ''
        for char in self:
            if char == prev_char:
                return True
            prev_char = char

        return False


    def check_inc(self):
        '''Returns True if there are no descending numbers in the row'''
        prev_num = 0
        for char in self:
            this_num = int(char)
            if this_num < prev_num:
                return False
            prev_num = this_num

        return True


    def validate_p1(self):
        '''Checks for double values and incrementing'''
        return self.check_double() and self.check_inc()


    def check_real_double(self):
        '''Retuns only True if the double is really only a double value
        and no more'''
        valid = False
        occ = 1
        prev_char = ''
        for char in self:
            if char == prev_char:
                occ += 1
                if occ == 2:
                    valid = True
                elif occ > 2:
                    valid = False
            else:
                if valid:
                    break
                occ = 1
            prev_char = char

        return valid


    def validate_p2(self):
        '''Checks for double values and incrementing (modified for part 2)'''
        return self.check_real_double() and self.check_inc()



# Functions
def get_valid_passwords_p1(lines: list[str]) -> int:
    input_parts = lines[0].split('-')

    min_passwd = int(input_parts[0])
    max_passwd = int(input_parts[1])

    nr_valid = 0

    for i in range(min_passwd, max_passwd + 1):
        passwd = Passwd(str(i))
        if passwd.validate_p1():
            nr_valid += 1

    return nr_valid


def get_valid_passwords_p2(lines: list[str]) -> int:
    input_parts = lines[0].split('-')

    min_passwd = int(input_parts[0])
    max_passwd = int(input_parts[1])

    nr_valid = 0

    for i in range(min_passwd, max_passwd + 1):
        passwd = Passwd(str(i))
        if passwd.validate_p2():
            nr_valid += 1

    return nr_valid


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    return get_valid_passwords_p1(lines)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return get_valid_passwords_p2(lines)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
