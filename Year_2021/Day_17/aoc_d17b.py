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

Part 2:
Now we consider also the X value.
To calculate the minimal X start velocity, I've written a small separate script
to calculate the lowest speed at which it reduces to zero after it has reached the 
target area.
The maximum is where it goes beyond the target area at the first step.

The maximum Y start velocity we learned in part 1 (122).
The minimum again is where it goes off the chart in the first step.

So what remains is to evaluate all possible values.

"""

# Imports

# Constants
MIN_X = 124
MAX_X = 174
MIN_Y = -123
MAX_Y = -86
MIN_START_VELO_X = 16
MAX_START_VELO_X = MAX_X
MIN_START_VELO_Y = MIN_Y
MAX_START_VELO_Y = 122

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def count_valid_start_points():
    '''Main function'''

    nr_target_hits = 0

    for start_velo_x in range(MIN_START_VELO_X, MAX_START_VELO_X + 1):
        for start_velo_y in range(MIN_START_VELO_Y, MAX_START_VELO_Y + 1):
            x = 0
            y = 0
            velo_x = start_velo_x
            velo_y = start_velo_y

            while True:
                x += velo_x
                y += velo_y
                if velo_x > 0:
                    velo_x -= 1
                velo_y -= 1

                if x >= MIN_X and x <= MAX_X and y >= MIN_Y and y <= MAX_Y:
                    nr_target_hits += 1
                    break

                if y < MIN_Y or x > MAX_X:
                    break

    return nr_target_hits


if __name__ == '__main__':
    # lines = read_input('input.txt')
    # lines = read_input('example1.txt')
    print("amount of starting points:", count_valid_start_points())
