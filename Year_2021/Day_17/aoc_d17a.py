"""
Day 17, Part 1

Problem description: See https://adventofcode.com/2021/day/17

My solution:
Part 1:

For the first problem, we don't consider the x velocity as we 
can always find a velocity at which the the speed eveuntually
reduces to zero in the target area.

So we only look at the y velocity and of course only at a positive one.
The problem is: where do we stop? For now, I will try to look at any
value between 1 and 100000.
"""

# Imports

# Constants
MIN_X = 124
MAX_X = 174
MIN_Y = -123
MAX_Y = -86

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def get_max_y():
    '''Main function'''

    heighest_y_plus_target = 0

    for start_velo_y in range(1, 10001):
        heighest_y = 0
        y = 0
        velo_y = start_velo_y
        target_area_reached = False

        while True:
            y += velo_y

            if y > heighest_y:
                heighest_y = y

            velo_y -= 1

            if y >= MIN_Y and y <= MAX_Y:
                target_area_reached = True
                break

            if y < MIN_Y:
                break

        if target_area_reached and heighest_y > heighest_y_plus_target:
            heighest_y_plus_target = heighest_y
            print("height reached: {} at velocity {}".format(
                str(heighest_y_plus_target),
                str(start_velo_y),
            ))

    return heighest_y_plus_target


if __name__ == '__main__':
    # lines = read_input('input.txt')
    # lines = read_input('example1.txt')
    print("Heighest y reached:", get_max_y())
