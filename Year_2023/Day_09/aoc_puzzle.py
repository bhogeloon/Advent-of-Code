"""
Year 2023, Day 9

Problem description: See https://adventofcode.com/2023/day/9

For this one I created the following classes:
ValueHistory: This contains a list of deques which contain the
history data. Initially, this will contain one deque containing one line
of puzzle input.
ValueHistories: The container class containing all the ValueHistory objects.

For part 1, I first start filling all the next levels of history data, by
each time considering the difference between two data entries.
After that, I go the opposite way by adding the most right value of the
previous deque to the current one. That will be the new right most value.

For part 2, the first part is the same, but in stead of adding the right value,
I sustract the left value.

"""

# Imports
from pprint import pprint
from collections import deque

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


# Classes
class ValueHistory(list[deque[int]]):
    '''A list of deques of value History data'''

    def __init__(self, line: str) -> None:
        self.append(deque([int(c) for c in line.split()]))
        # These values will contain the solution
        self.next_value_r = 0
        self.next_value_l = 0
    

    def analyse(self) -> None:
        '''First fill all the history data levels'''
        all_zeroes = False
        i = 0

        while not all_zeroes:
            all_zeroes = True
            new_list = deque()

            # For each value, except the last one
            for j in range(len(self[i])-1):
                # Get the difference from the next value
                new_value = self[i][j+1] - self[i][j]
                new_list.append(new_value)

                if new_value != 0:
                    all_zeroes = False

            self.append(new_list)
            i += 1


    def get_next_value_r(self) -> None:
        '''This function will get the solution to part 1'''

        # Go back from the end to 1
        for i in range(len(self)-1,0,-1):
            # Append the value on the previous level by adding
            # the last entry of this level to the last entry
            # of the previous one. 
            self[i-1].append(self[i-1][-1] + self[i][-1])

        # The last entry of the first level contains the solution
        self.next_value_r = self[0][-1]


    def get_next_value_l(self) -> None:
        '''This function will get the solution to part 2'''

        # Go back from the end to 1
        for i in range(len(self)-1,0,-1):
            # Now substract the left value of the current level
            # from the left value of the previous level
            # and append to the left.
            self[i-1].appendleft(self[i-1][0] - self[i][0])

        # The first entry of the first level contains the solution
        self.next_value_l = self[0][0]


class ValueHistories(list[ValueHistory]):
    '''Container class for ValueHistory objects'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(ValueHistory(line))


    def analyse(self) -> None:
        for histval in self:
            histval.analyse()

        # pprint(self)
            

    def get_next_values_r(self) -> None:
        for histval in self:
            histval.get_next_value_r()


    def get_next_values_l(self) -> None:
        for histval in self:
            histval.get_next_value_l()


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    histdata = ValueHistories(lines)
    histdata.analyse()
    histdata.get_next_values_r()

    return sum([d.next_value_r for d in histdata])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    histdata = ValueHistories(lines)
    histdata.analyse()
    histdata.get_next_values_l()

    # pprint(histdata)

    return sum([d.next_value_l for d in histdata])

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass