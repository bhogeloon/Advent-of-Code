"""
Year 2020, Day 5

Problem description: See https://adventofcode.com/2020/day/5

The following class is used:
- Seats: Represents a list of seats. The seats are stored as ints.

Part 1: Convert the string in a binary number and then store it
as an int in Seats. Then just get the maximum.

Part 2: Firs sort the list. Then look for a missing number. If then
the number before and after does exist, we have a hit.

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

class Seats(list[int]):
    '''A list of seat numbers (stored as ints)'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            line = line.replace('F', '0')
            line = line.replace('B', '1')
            line = line.replace('L', '0')
            line = line.replace('R', '1')

            seat_nr = int(line, base=2)
            self.append(seat_nr)


    def get_my_seat(self) -> int:
        '''Get my seat, which is not in the list, but between
        two existing ones'''
        # First, sort the list
        self.sort()

        for i in range(1, self[-2]):
            # If it doesn't exist
            if i not in self:
                # Check if previous and next does exist
                if i-1 in self and i+1 in self:
                    # Then we have a hit!
                    return i

        # If nothing found, raise exception
        raise RuntimeError("No empty seat found.")


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    seats = Seats(lines)

    return max(seats)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    seats = Seats(lines)

    return seats.get_my_seat()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
