"""
Year 2017, Day 5

Problem description: See https://adventofcode.com/2017/day/5

The following class is used:
- OffsetList: the list containing the offsets

Part 1: Walk through the list. Determine each time the new position.
Exit if the position is outside the list. Just before moving to the new
position, increase the value of the current postition.

Part 2: Just add an extra check: if it is larger than 3, then decrease
by one instead.
This way it takes considerable longer to break out: more than 10 seconds.

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

class OffsetList(list[int]):
    '''List of Offset instructions (which are just ints) '''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(int(line))


    def run(self, part=1) -> int:
        '''Run the OffsetList returning the number of steps it takes
        to get out of the list'''
        steps = 0
        cur_pos = 0

        while True:
            steps += 1
            new_pos = cur_pos + self[cur_pos]
            
            if new_pos < 0 or new_pos >= len(self):
                return steps
            
            # If part 2 and value is 3 or larger
            if part == 2 and self[cur_pos] >= 3:
                self[cur_pos] -= 1
            else:
                self[cur_pos] += 1

            cur_pos = new_pos


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    offsets = OffsetList(lines)

    return offsets.run()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    offsets = OffsetList(lines)

    return offsets.run(part=2)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
