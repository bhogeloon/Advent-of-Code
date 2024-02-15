"""
Year 2020, Day 3, Part 1

Problem description: See https://adventofcode.com/2020/day/3

My solution:
Part 1:

"""

# Imports

# Constants
X_INC = 3
Y_INC = 1

XY_INC = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2),
]

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

# Functions
def get_nr_of_trees(trees: list, x_inc, y_inc):
    '''Get number of trees (# chars)'''

    nr_of_trees = 0
    x_pos = 0
    y_pos = 0

    while True:
        if trees[y_pos][x_pos] == "#":
            nr_of_trees += 1

        y_pos += y_inc

        if y_pos >= len(trees):
            break

        x_pos += x_inc

        if x_pos >= len(trees[y_pos]):
            x_pos -= len(trees[y_pos])

    return nr_of_trees


# Main function
def get_solution(lines: list) -> int:
    '''Main function'''

    trees = []

    for line in lines:
        y_trees = []
        for char in line:
            y_trees.append(char)

        trees.append(y_trees)

    result = 1

    for (x_inc, y_inc) in XY_INC:
        nr_of_trees = get_nr_of_trees(trees, x_inc, y_inc)
        result *= nr_of_trees

    return result


if __name__ == '__main__':
    pass