"""
Day 9, Part 1

Problem description: See https://adventofcode.com/2021/day/9

My solution:

Make an (x,y) matrix of the input.
Walk through the matrix and consider each neighbor. If all
of those values are bigger than the current value, it is
a Low Point.

"""


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def is_low_point(heigths, x, y):
    '''This function returns True when all neighbors values are lower'''
    # Check left
    if x == 0:
        low_left = True
    else:
        low_left = heigths[y][x] < heigths[y][x-1]

    # Check right
    if x == len(heigths[y]) - 1:
        low_right = True
    else:
        low_right = heigths[y][x] < heigths[y][x+1]

    # Check up
    if y == 0:
        low_up = True
    else:
        low_up = heigths[y][x] < heigths[y-1][x]

    # Check down
    if y == len(heigths) - 1:
        low_down = True
    else:
        low_down = heigths[y][x] < heigths[y+1][x]

    # return True if all is True
    return (low_right and low_left and low_up and low_down)


def get_total_risk(lines):
    heigths = [[int(x) for x in list(line)] for line in lines]

    total_risk = 0

    for y in range(len(heigths)):
        for x in range(len(heigths[y])):
            if is_low_point(heigths, x, y):
                total_risk += heigths[y][x] + 1

    return total_risk


if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Total risk level is:", get_total_risk(lines))
