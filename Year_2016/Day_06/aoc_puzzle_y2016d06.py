"""
Year 2016, Day 6

Problem description: See https://adventofcode.com/2016/day/6

The following class is used:
- Messages: Grid containing the messages character. Each message is plotted
    over the x-axis

Part 1: Keep a Counter object per column and then use the most_common function
to get the character per column.

Part 2: Now use the most_common function to get all the occurences and then 
check the last one in the list.

"""

# Imports
from pprint import pprint
from collections import Counter
from grid import Grid2D


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Messages(Grid2D):
    '''Grid containing the message. A message is plotted on the x-axis. The 
    y-axis contains all messages'''
    def __init__(self, lines: list[str]) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)

        super().__init__(
            sizes=(self.x_size,self.y_size),
            input_lines=lines,
        )

        # Set up Counter objects
        self.col_counters = [
            Counter(list(self.grid[c,:])) for c in range(self.x_size)
        ]

        if Gv.test:
            pprint(self.col_counters[0].items())


    def get_message(self) -> str:
        '''Get the most common char for each column'''
        result = ''

        for c in range(self.x_size):
            result += self.col_counters[c].most_common(1)[0][0]

        return result


    def get_real_message(self) -> str:
        '''Get the least common char for each column'''
        result = ''

        for c in range(self.x_size):
            # Now retrieve all most_common chars and retrieve the last one
            result += self.col_counters[c].most_common()[-1][0]

        return result


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    msgs = Messages(lines)

    return msgs.get_message()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    msgs = Messages(lines)

    return msgs.get_real_message()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
