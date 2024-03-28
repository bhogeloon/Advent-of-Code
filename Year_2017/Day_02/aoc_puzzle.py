"""
Year 2017, Day 2

Problem description: See https://adventofcode.com/2017/day/2

The following classes are used:
- Row: list subclass which is a list of all row numbers
- Spreadsheet: List container of Row objects

Part 1: Substract max and min for each row and summarise the results.

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

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
