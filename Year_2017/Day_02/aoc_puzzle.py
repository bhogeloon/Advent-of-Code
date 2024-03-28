"""
Year 2017, Day 2

Problem description: See https://adventofcode.com/2017/day/2

The following classes are used:
- Row: list subclass which is a list of all row numbers
- Spreadsheet: List container of Row objects

Part 1: Substract max and min for each row and summarise the results.

Part 2: For each row: loop through all the numbers and then again through all the
numbers. As soon as one divides to the other in an integer then return that value.
In the end return the sum of all those values.

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
class Row(list):
    '''Row (list) of numbers in the Spreadsheet'''
    def __init__(self, line: str) -> None:
        self.extend([int(n) for n in line.split()])


    def get_diff_min_max(self) -> int:
        '''Return the max minus min value'''
        return max(self) - min(self)
    

    def get_even_division_result(self) -> int:
        '''Find the value of two numbers that can be devided to each other
        evenly.'''

        # Go through all the numbers
        for i, nr1 in enumerate(self):
            # Then go through the list again
            for j, nr2 in enumerate(self):
                # Skip if the same number
                if i == j:
                    continue

                # Check if nr1 is dividable by nr2
                intdiv = nr1//nr2
                if intdiv == nr1/nr2:
                    return intdiv

        raise RuntimeError('No dividable nrs found for row {}'.format(str(self)))


class Spreadsheet(list[Row]):
    '''Contains a list of Rows'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Row(line))


    def get_checksum(self) -> int:
        '''Result of part 1'''
        diffs = []

        # Get the diff for each row
        for row in self:
            diffs.append(row.get_diff_min_max())

        # Return sum
        return sum(diffs)


    def get_sum_of_divisions(self) -> int:
        '''Result of part 2'''
        divs = []

        # Get the division result for each row
        for row in self:
            divs.append(row.get_even_division_result())

        # Return the sum
        return sum(divs)


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    spreadsheet = Spreadsheet(lines)

    return spreadsheet.get_checksum()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    spreadsheet = Spreadsheet(lines)

    return spreadsheet.get_sum_of_divisions()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
