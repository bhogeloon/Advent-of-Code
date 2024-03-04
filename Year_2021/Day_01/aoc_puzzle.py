"""
Year 2021, Day 1

Problem description: See https://adventofcode.com/2021/day/1

First part is simple: Walk through the list and count the increases.

For part 2, I created a new list of all the summaries of depth in a
sliding window of 3 samples. I then calculated the nr of increases in
the same way as in part 1.

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
    

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    depths = []

    for line in lines:
        depths.append(int(line))

    nr_of_increases = 0

    for i in range(1, len(depths)):
        # If it is an increase, increase counter
        if depths[i] > depths [i-1]:
            nr_of_increases += 1

    # print("Nr of increases is:", nr_of_increases)

    return nr_of_increases

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    depths = []

    for line in lines:
        depths.append(int(line))

    # Keep track of all the sliding windows sums
    depth_sums = []

    for i in range(2, len(depths)):
        depth_sums.append(sum(depths[i-2:i+1]))

    nr_of_increases = 0

    # Then calculate the nr of increases in the same way
    for i in range(1, len(depth_sums)):
        if depth_sums[i] > depth_sums[i-1]:
            nr_of_increases += 1

    # print("Nr of increases is:", nr_of_increases)

    return nr_of_increases

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
