"""
Year 2017, Day 1

Problem description: See https://adventofcode.com/2017/day/1

I created the following classes:
- Captcha: Circular list of Digit objects
- Digit: contains a nr and a next attribute, pointing the next Digit in
the list.

In part 1, we add all numbers together if the next digit is equal.

In part 2, I added an attribute 'half' to the Digit object, pointing to 
the object on the other half of the list. I then did the same as in
part 1, but then looking at this pointer instead.

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

class Captcha(list):
    '''Circular structure of Digit objects'''
    def __init__(self, line: str) -> None:
        # fill the list with Digit objects
        for char in line:
            self.append(Digit(char))

        # set the circular relationships
        for (i, digit) in enumerate(self):
            # Set next digit relationship
            if i == len(self) - 1:
                digit.next = self[0]
            else:
                digit.next = self[i+1]

            # Now set the halfway relationship
            h = (i + len(self)//2) % len(self)
            digit.half = self[h]


    def solve(self) -> int:
        '''Solve the Captcha by adding up all digits that match the
        next digit'''
        sum = 0

        for digit in self:
            # If nr is same as in the next digit
            if digit.nr == digit.next.nr:
                sum += digit.nr

        return sum


    def solve_half(self) -> int:
        '''Solve the captcha in part 2, looking at halfway'''
        sum = 0

        for digit in self:
            # If nr is same as in the next digit
            if digit.nr == digit.half.nr:
                sum += digit.nr

        return sum


class Digit():
    '''Object containing digit and next (pointer to next objec)'''
    def __init__(self, char: str) -> None:
        self.nr = int(char)


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    captcha = Captcha(lines[0])

    return captcha.solve()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    captcha = Captcha(lines[0])

    return captcha.solve_half()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
