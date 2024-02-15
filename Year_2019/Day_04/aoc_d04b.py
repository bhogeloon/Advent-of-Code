"""
Year 2019, Day 4, Part 1

Problem description: See https://adventofcode.com/2019/day/4

"""

# Imports
from pprint import pprint

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Passwd(str):
    def check_double(self):
        prev_char = ''
        for char in self:
            if char == prev_char:
                return True
            prev_char = char

        return False


    def check_real_double(self):
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


    def check_inc(self):
        prev_num = 0
        for char in self:
            this_num = int(char)
            if this_num < prev_num:
                return False
            prev_num = this_num

        return True


    def validate(self):
        return self.check_real_double() and self.check_inc()


# Functions




# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    # print(Passwd('112233').check_real_double())

    input_parts = lines[0].split('-')

    min_passwd = int(input_parts[0])
    max_passwd = int(input_parts[1])

    nr_valid = 0

    for i in range(min_passwd, max_passwd + 1):
        passwd = Passwd(str(i))
        if passwd.validate():
            nr_valid += 1

    return nr_valid

    return __name__


if __name__ == '__main__':
    pass