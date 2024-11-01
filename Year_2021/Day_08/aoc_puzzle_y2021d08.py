"""
Year 2021, Day 8

Problem description: See https://adventofcode.com/2021/day/8

The following classes are used:
- Signal: Has an input and output attibute. Each of them contains a list of
    strings
- Signals: List container class of Signal objects.

Part 1: Check for each output digit if the length indicates that it is a 
digit with a unique pattern length.

Part 2: This one was a little trickier.
I started by processing the easy records, the one with unique length.
These I could easily correlate with a value.
Then I tried to figure out how to recognise the others and came up
with a solution to count the overlapping segments (or characters) with a
known value. For that reason I chose to use sets to store the character
as I could more easily calculate the overlap.
Then I stored all mappings in a dict, using a string with sorted letters
as not all letters were in the same order in the output section.
Then it was just a question of sorting the characters on the output section
and reading the mappings.
"""

# Imports
from __future__ import annotations
from pprint import pprint


# Constants
# The digits which have a unique number of display units
UNIQUE_PATTERN = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Signal:
    '''A signal has an input and output attribute'''

    def __init__(self, line: str) -> None:
        (input_str, output_str) = line.split(' | ')
        self.input = input_str.split()
        self.output = output_str.split()


    def get_unique_digits(self) -> int:
        '''Return the amount of unique digits in the output field'''
        nr_of_hits = 0

        for digit in self.output:
            if len(digit) in UNIQUE_PATTERN.values():
                nr_of_hits += 1

        return nr_of_hits
    

    def decipher_input(self) -> dict:
        '''
        This function returns a mapping (dict) from digit_string 
        to digit decimal value (0 - 9).
        '''
        # This will be the mapping from set to value
        digit_value = {}
        # This one will be the reverse mapping (used in this function only)
        digit_set = {}

        # In the firs cycle, we only look at the 'easy' values, which
        # are recogonisable by length
        for input_str in self.input:
            input_set = set(input_str)
            input_sort = ''.join(sorted(input_set))
            if len(input_set) == 2:
                digit_value[input_sort] = 1
                digit_set[1] = input_set
            elif len(input_set) == 3:
                digit_value[input_sort] = 7
                digit_set[7] = input_set
            elif len(input_set) == 4:
                digit_value[input_sort] = 4
                digit_set[4] = input_set
            elif len(input_set) == 7:
                digit_value[input_sort] = 8
                digit_set[8] = input_set

        # In the next cycle, we only look at length 6 and 5
        for input_str in self.input:
            input_set = set(input_str)
            input_sort = ''.join(sorted(input_set))
            # This one can be eiter 0, 6 or 9
            if len(input_set) == 6:
                # if both letters of digit 1 appear, it 0 or 9
                # otherwise it must be 6
                if len(input_set & digit_set[1]) < 2:
                    digit_value[input_sort] = 6
                    digit_set[6] = input_set
                # if all letters of digit 4 overlap, it must be 9
                elif len(input_set & digit_set[4]) == 4:
                    digit_value[input_sort] = 9
                    digit_set[9] = input_set
                # and if not, it must be 0
                else:
                    digit_value[input_sort] = 0
                    digit_set[0] = input_set

            # This one is either 2, 3 or 5:
            elif len(input_set) == 5:
                # if it overlaps with digit 1, it must be 3
                if len(input_set & digit_set[1]) == 2:
                    digit_value[input_sort] = 3
                    digit_set[3] = input_set
                # if the overlap with digit 4 is only 2, it must be 2
                elif len(input_set & digit_set[4]) == 2:
                    digit_value[input_sort] = 2
                    digit_set[2] = input_set
                # and what remains is 5
                else:
                    digit_value[input_sort] = 5
                    digit_set[5] = input_set

        return digit_value
    

    def get_output_number(self) -> int:
        '''Get the output digits as an integer'''
        # Retrieve digit mapping
        digit_value = self.decipher_input()

        output_digits_str = ''

        # For each output digit string
        for output_str in self.output:
            # Create a set and sort it
            output_set = set(output_str)
            output_sort = ''.join(sorted(output_set))
            # Apply mapping
            output_digits_str += str((digit_value[output_sort]))

        # Convert to integer
        number = int(output_digits_str)

        return number


class Signals(list[Signal]):
    '''List container class of Signal attributes'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Signal(line))


    def get_unique_digits(self) -> int:
        '''Return the amount of unique digits in the output fields.'''
        nr_of_hits = 0

        for signal in self:
            nr_of_hits += signal.get_unique_digits()

        return nr_of_hits
    

    def get_total(self) -> int:
        '''Get the total amount of output digits'''
        total = 0

        for signal in self:
            total += signal.get_output_number()

        return total


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    signals = Signals(lines)

    return signals.get_unique_digits()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    signals = Signals(lines)

    return signals.get_total()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
