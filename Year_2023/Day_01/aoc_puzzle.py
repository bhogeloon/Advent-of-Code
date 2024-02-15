"""
Year 2023, Day 1

Problem description: See https://adventofcode.com/2023/day/1

"""

# Imports
from pprint import pprint
import string
import re

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


# Classes

class CalibrationItem():
    '''Item (line) within a CalibrationDoc object'''

    # Class variables
    conv_table = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    def __init__(self, line: str) -> None:
        self.item = line


    def evaluate(self) -> int:
        self.first_digit = ''

        for char in self.item:

            # If char is a digit
            if char in string.digits:

                # If first digit found
                if self.first_digit == '':
                    self.first_digit = char

                # Update last digit
                self.last_digit = char

        if self.first_digit == '':
            raise RuntimeError("no digit: {}".format(self))
        
        print(self.item)
        print(self.first_digit + self.last_digit)

        # Return intereger value of combined digits
        return int(self.first_digit + self.last_digit)
    

    def evaluate_with_strings(self) -> int:
        self.first_digit = ''

        for i in range(len(self.item)):
            digit = ''

            # if char is a digit
            if self.item[i] in string.digits:
                digit = self.item[i]
            else:
                for (word, number) in self.conv_table.items():
                    m = re.match(word, self.item[i:])

                    if m:
                        digit = number
                        break

            if digit != '':
                # If first digit found
                if self.first_digit == '':
                    self.first_digit = digit

                # Update last digit
                self.last_digit = digit

        if self.first_digit == '':
            raise RuntimeError("no digit: {}".format(self))
        
        print(self.item)
        print(self.first_digit + self.last_digit)

        # Return intereger value of combined digits
        return int(self.first_digit + self.last_digit)


class CalibrationDoc(list):
    '''Calibration document content'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(CalibrationItem(line))

        self.cal_value = 0


    def evaluate(self) -> None:
        for cal_item in self:
            self.cal_value += cal_item.evaluate()


    def evaluate_with_strings(self) -> None:
        for cal_item in self:
            self.cal_value += cal_item.evaluate_with_strings()


# Main functions
def get_solution_part1(lines: list[str]) -> int:
    '''Main function'''

    caldoc = CalibrationDoc(lines)
    caldoc.evaluate()

    return caldoc.cal_value
    # return 'part_1 ' + __name__


def get_solution_part2(lines: list[str]) -> int:
    '''Main function'''

    caldoc = CalibrationDoc(lines)
    caldoc.evaluate_with_strings()

    return caldoc.cal_value


    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass