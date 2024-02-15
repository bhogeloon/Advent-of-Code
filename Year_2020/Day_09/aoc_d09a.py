"""
Year 2020, Day 9, Part 1

Problem description: See https://adventofcode.com/2020/day/9

"""

# Imports
import numbers
from pprint import pprint

# Constants

PREAMBLE = 25

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes
class XmasSeq():

    def __init__(self, lines: list[str]) -> None:
        self.numbers = []

        for line in lines:
            self.numbers.append(int(line))


    def _check_number(self, nr: int) -> bool:
        '''Check validity of one number'''

        for i in range(nr-PREAMBLE-1, nr-1):
            for j in range(i+1, nr):
                if self.numbers[nr] == self.numbers[i] + self.numbers[j]:
                    return True

        return False


    def validate(self) -> int:
        '''Return first number found which is invalid.
        Return -1 if no invalid number is found'''

        for nr in range(PREAMBLE+1, len(self.numbers)):
            if not self._check_number(nr):
                return self.numbers[nr]

        return -1


# Functions



# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    xmas_seq = XmasSeq(lines)

    return xmas_seq.validate()

    return __name__


if __name__ == '__main__':
    pass