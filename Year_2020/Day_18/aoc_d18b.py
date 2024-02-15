"""
Year 2020, Day 18, Part 2

Problem description: See https://adventofcode.com/2020/day/18

"""

# Imports
from pprint import pprint
import re

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Homework():
    def __init__(self, line) -> None:
        self.value = line
        self.result = None
        self.oper = None
        self.ruler = 0


    def read_brackets(self) -> int:
        stack = 0
        i = self.ruler + 1

        while stack > 0 or self.value[i] != ')':
            if self.value[i] == '(':
                stack += 1
            elif self.value[i] == ')':
                stack -= 1
            i += 1

        sub_hw = Homework(self.value[self.ruler+1:i])

        self.ruler = i

        return sub_hw.evaluate()


    def evaluate(self) -> int:
        if type(self.value) == int:
            return self.value

        if len(self.value) == 1:
            return int(self.value)

        while self.ruler < len(self.value):

            if self.oper == '*':
                sub_hw = Homework(self.value[self.ruler:])
                return self.result * sub_hw.evaluate()

            if self.value[self.ruler] == '(':
                new_value = self.read_brackets()

            else:
                new_value = int(self.value[self.ruler])

            if self.ruler == len(self.value) - 1:
                new_oper = '!'
                self.ruler += 1
            else:
                new_oper = self.value[self.ruler+2]
                self.ruler += 4

            if self.oper == None:
                self.result = new_value
            elif self.oper == '+':
                self.result += new_value
            else:
                raise RuntimeError('Unknown operator: {}'.format(self.oper))

            self.oper = new_oper

        return self.result


# Functions



# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    total = 0

    for nr, line in enumerate(lines):
        hw = Homework(line)
        new_result = hw.evaluate()
        print(nr, new_result, line)
        total += new_result

    return total

    return __name__


if __name__ == '__main__':
    pass