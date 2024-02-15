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

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

# Functions

# Main function
def get_solution(lines: list) -> int:
    '''Main function'''

    trees = []

    for line in lines:
        y_trees = []
        for char in line:
            y_trees.append(char)

        trees.append(y_trees)

    nr_of_trees = 0
    x_pos = 0
    y_pos = 0

    while True:
        if trees[y_pos][x_pos] == "#":
            nr_of_trees += 1

        y_pos += Y_INC

        if y_pos >= len(trees):
            break

        x_pos += X_INC

        if x_pos >= len(trees[y_pos]):
            x_pos -= len(trees[y_pos])

    return nr_of_trees


if __name__ == '__main__':
    pass