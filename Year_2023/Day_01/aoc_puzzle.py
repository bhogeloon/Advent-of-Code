"""
Year 2023, Day 1

Problem description: See https://adventofcode.com/2023/day/1

For this puzzle I created the following classes:
- CalibrationDoc, which contains all callibration lines
- CalibrationItem

For part 1, I simply go through the list and collect the first and last
appearing digit and glue them together.

For part 2, for each line, I'm walking through the string character by character.
If the character is a digit, then also threat it like a digit. If it as a
alphabetic character, then try to match the remainder of the string
with a number in letters. If this is the case, then consider this digit
as well.
Then finally, take the first and last digit again.
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

    # Conversion table between alphabetical name and digit
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
        '''Evaluation of the item in part 1
        This function only looks at real digits'''

        # Make first digit empty (= not found)
        self.first_digit = ''

        for char in self.item:

            # If char is a digit
            if char in string.digits:

                # If first digit found
                if self.first_digit == '':
                    self.first_digit = char

                # Update last digit
                # Will be updated each time during the loop,
                # so in the end, it will contain the last one
                self.last_digit = char

        # If nothing has been found
        if self.first_digit == '':
            raise RuntimeError("no digit: {}".format(self))
        
        print(self.item)
        print(self.first_digit + self.last_digit)

        # Return intereger value of combined digits
        return int(self.first_digit + self.last_digit)
    

    def evaluate_with_strings(self) -> int:
        '''This is the evaluation for part 2, taking into
        consideration of named digits'''


        # Make first digit empty (= not found)
        self.first_digit = ''

        for i in range(len(self.item)):
            # Make digit for this round empty
            digit = ''

            # if char is a digit, do the normal thing
            if self.item[i] in string.digits:
                digit = self.item[i]
            else:
                # If not, try to match the remainder of the item
                # line to one of the table entries
                for (word, number) in self.conv_table.items():
                    m = re.match(word, self.item[i:])

                    if m:
                        digit = number
                        break

            # In case we found something
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

        # This will contain the eventual solution
        self.cal_value = 0


    def evaluate(self) -> None:
        '''Evaluation of the item in part 1
        This function only looks at real digits'''

        for cal_item in self:
            self.cal_value += cal_item.evaluate()


    def evaluate_with_strings(self) -> None:
        '''This is the evaluation for part 2, taking into
        consideration of named digits'''
        for cal_item in self:
            self.cal_value += cal_item.evaluate_with_strings()


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for part 1'''

    caldoc = CalibrationDoc(lines)
    caldoc.evaluate()

    return caldoc.cal_value
    # return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for part 2'''

    caldoc = CalibrationDoc(lines)
    caldoc.evaluate_with_strings()

    return caldoc.cal_value

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass