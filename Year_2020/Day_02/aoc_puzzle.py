"""
Year 2020, Day 2

Problem description: See https://adventofcode.com/2020/day/2

We have the following classes:
- Password: Represents a password with the restrictions.
- PasswordDB: Password Database, which is a list container class of Password objects.

For part 1: Use the Counter module to count the number of appearances of char.

For part 2: Compare the char with the character of position 1 and 2. If exactly one
of them matches, it is a valid password.
"""

# Imports
from pprint import pprint
import re
from collections import Counter


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Password():
    '''Password to be validated'''

    def __init__(self, line:str) -> None:
        # Analyse input =
        # ddd-ddd c: <password>
        m = re.fullmatch(r'(\d+)-(\d+)\s+([a-z]):\s+([a-z]+)', line)

        if not m:
            raise RuntimeError("No match found for {}".format(line))

        # Minimal occurences (part 1)
        self.min_occ = int(m[1])
        # Maximum occurences (part 1)
        self.max_occ = int(m[2])

        # First possible position of char (part 2)
        self.min_pos = int(m[1]) - 1
        # Second possible position of char (part 2)
        self.max_pos = int(m[2]) - 1

        # The character to be matched
        self.char = m[3]
        # The password itself
        self.password = m[4]


    def valid1(self) -> bool:
        '''Check if a password is valid according to policy in part 1'''

        # Make counter object from password
        c = Counter(self.password)
        # count the amount of occurences of char
        act_occ = c[self.char]

        # Return True if counter is between boundaries
        return act_occ >= self.min_occ and act_occ <= self.max_occ
    

    def valid2(self) -> bool:
        '''Check if a password is valid according to policy in part 2'''

        # If two positions match, not valid
        if self.password[self.min_pos] == self.char and self.password[self.max_pos] == self.char:
            return False

        # If either positions match (which now means exactly one), valid
        elif self.password[self.min_pos] == self.char or self.password[self.max_pos] == self.char:
            return True

        # Otherwise (no match), not valid
        else:
            return False


class PasswordDB(list[Password]):
    '''Password Database: list container class of Password objects'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Password(line))


    def get_valid_pws(self, policy = 1) -> int:
        '''Count all valid passwords according to policy part 1 or 2'''
        valid_pws = 0

        for pw in self:
            if (policy == 1 and pw.valid1()) or (policy == 2 and pw.valid2()):
                valid_pws += 1

        return valid_pws


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    pwdb = PasswordDB(lines)

    return pwdb.get_valid_pws()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    pwdb = PasswordDB(lines)

    return pwdb.get_valid_pws(2)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
