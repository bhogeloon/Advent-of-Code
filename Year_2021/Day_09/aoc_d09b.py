"""
Day 9, Part 2

Problem description: See https://adventofcode.com/2021/day/9

My solution:

First find all the low points as in part one, but this time keep a list
of all low points with their coordinates.

Then go through each low point and investigate their direct neighors. For each
neighbor which is not a value 9. For each neighbor, call the same function
recursively. In the mean time, store all points found in a list so that you
can:
    a) Keep track of all the points already investigated, so you don't go
    on for ever.
    b) Keep track of the amount of points.

For each low point, store the amount of found points and in the end consider
the highest 3.

"""


# Global values
'''
low_points is a list of Low Points. Each entry consists of a dict with
the  following attributes:
    low_point: (x,y) tuple with the coordinates of the Low Point itself
    basin: List of (x,y) tuples with the points which are part of the basin
        (This includes the low point itself)
'''
low_points = []

def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def is_low_point(heighths, x, y):
    '''This function returns True when all neighbors values are lower'''
    # Check left
    if x == 0:
        low_left = True
    else:
        low_left = heighths[y][x] < heighths[y][x-1]

    # Check right
    if x == len(heighths[y]) - 1:
        low_right = True
    else:
        low_right = heighths[y][x] < heighths[y][x+1]

    # Check up
    if y == 0:
        low_up = True
    else:
        low_up = heighths[y][x] < heighths[y-1][x]

    # Check down
    if y == len(heighths) - 1:
        low_down = True
    else:
        low_down = heighths[y][x] < heighths[y+1][x]

    # return True if all is True
    return (low_right and low_left and low_up and low_down)


def find_basin_neighbors(heighths, low_point, x,y):
    '''This function will try to find neighbors of point (x,y), which are 
    part ofccthe basin. It is a recursive function as it calls itself for all
    the found neighbbors'''
    # The first step is to register yourself in the basin
    low_point['basin'].append((x,y))

    # Now discover addtional neighbors on the left
    # If you're on the border, don't bother
    if x > 0:
        # Check neighbor not 9 and whether you haven't already explored it
        if heighths[y][x-1] < 9 and (x-1,y) not in low_point['basin']:
            # Now call yourself for the neighbor point
            find_basin_neighbors(heighths, low_point, x-1, y)

    # Now discover addtional neighbors on the right
    # If you're on the border, don't bother
    if x < len(heighths[y]) - 1:
        # Check neighbor not 9 and whether you haven't already explored it
        if heighths[y][x+1] < 9 and (x+1,y) not in low_point['basin']:
            # Now call yourself for the neighbor point
            find_basin_neighbors(heighths, low_point, x+1, y)

    # Now discover addtional neighbors above
    # If you're on the border, don't bother
    if y > 0:
        # Check neighbor not 9 and whether you haven't already explored it
        if heighths[y-1][x] < 9 and (x,y-1) not in low_point['basin']:
            # Now call yourself for the neighbor point
            find_basin_neighbors(heighths, low_point, x, y-1)

    # Now discover addtional neighbors above
    # If you're on the border, don't bother
    if y < len(heighths) - 1:
        # Check neighbor not 9 and whether you haven't already explored it
        if heighths[y+1][x] < 9 and (x,y+1) not in low_point['basin']:
            # Now call yourself for the neighbor point
            find_basin_neighbors(heighths, low_point, x, y+1)

    return


def get_basin(lines):
    heighths = [[int(x) for x in list(line)] for line in lines]

    # Find all low points
    for y in range(len(heighths)):
        for x in range(len(heighths[y])):
            if is_low_point(heighths, x, y):
                low_points.append({
                    'low_point': (x,y),
                    'basin': [],
                })

    basin_sizes = []

    # For each low point, find the basin points
    for low_point in low_points:
        find_basin_neighbors(heighths, low_point, *low_point['low_point'])
        basin_sizes.append(len(low_point['basin']))

    # Sort it, so you can extract the top 3
    basin_sizes.sort(reverse=True)

    basin_product = 1

    for i in range(3):
        basin_product *= basin_sizes[i]

    return basin_product

if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Product is:", get_basin(lines))
