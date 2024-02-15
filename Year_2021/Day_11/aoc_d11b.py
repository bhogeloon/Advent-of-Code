"""
Day 11, Part 2

Problem description: See https://adventofcode.com/2021/day/11

My solution:

The same code as part 1, but as soon as we detect all 0's, we return the
current step.
"""


# Global values

dumbos = []

def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def flash(x:int, y:int, flash_points: list) -> int:
    # Add coordinates to flash_points
    flash_points.append((x, y))

    # Set nr_of_flashes to 1
    nr_of_flashes = 1

    # Determine min and max values of neighbors
    if x == 0:
        min_x = 0
        max_x = 1
    elif x == len(dumbos[y]) - 1:
        min_x = x -1
        max_x = x
    else:
        min_x = x - 1
        max_x = x + 1

    if y == 0:
        min_y = 0
        max_y = 1
    elif y == len(dumbos) - 1:
        min_y = y -1
        max_y = y
    else:
        min_y = y - 1
        max_y = y + 1

    for neighbor_y in range(min_y, max_y + 1):
        for neighbor_x in range(min_x, max_x + 1):
            # Ignore if this is this is yourself
            if neighbor_x == x and neighbor_y == y:
                continue

            # Increase value
            dumbos[neighbor_y][neighbor_x] += 1

            if dumbos[neighbor_y][neighbor_x] > 9 and (neighbor_x,neighbor_y) not in flash_points:
                nr_of_flashes += flash(neighbor_x, neighbor_y, flash_points)

    return nr_of_flashes


def get_all_flash_step(lines):
    '''Main function to get the Number of Flashes'''
    nr_of_flashes = 0

    # Read matrix
    for line in lines:
        xs = []
        for char in line:
            xs.append(int(char))
        dumbos.append(xs)

    # Perform the steps
    step = 0
    while True:
        step += 1
        # reset flash points
        flash_points = [1]
        # Increase the points in the matrix
        for y in range(len(dumbos)):
            for x in range(len(dumbos[y])):
                # Increase the number
                dumbos[y][x] += 1

                # If bigger than 9 and not already flashed
                if dumbos[y][x] > 9 and (x,y) not in flash_points:
                    nr_of_flashes += flash(x, y, flash_points)

        all_flash = True

        # Now go through the matrix again:
        for y in range(len(dumbos)):
            for x in range(len(dumbos[y])):
                if dumbos[y][x] > 9:
                    dumbos[y][x] = 0
                else:
                    all_flash = False

        if all_flash:
            return step

    return 0

if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Step where we get all flashes:", get_all_flash_step(lines))
