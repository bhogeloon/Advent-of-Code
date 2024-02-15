"""
Day 22, Part 2

Problem description: See https://adventofcode.com/2021/day/22

My solution:
Part 1:

"""

# Imports
import re

# Constants
LOW_LIMIT = -50
HIGH_LIMIT = 50

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

# Functions

def create_reactor_core() -> dict:
    '''Create a Core with all cubes off'''

    core = {}

    for x in range(LOW_LIMIT, HIGH_LIMIT + 1):
        y_values = {}
        for y in range(LOW_LIMIT, HIGH_LIMIT + 1):
            z_values = {}
            for z in range(LOW_LIMIT, HIGH_LIMIT + 1):
                z_values[z] = False
            y_values[y] = z_values
        core[x] = y_values

    return core


def process_line(core: dict, line: str) -> None:
    '''interpret the line and change core accordingly'''

    match_number = r'([\d-]+)'
    match_dots = r'\.\.'
    match_pattern = r'^(\w+) x={n}{d}{n},y={n}{d}{n},z={n}{d}{n}$'.format(
        n=match_number,
        d=match_dots,
    )
    m = re.match(match_pattern, line)

    action = m[1]
    x_min = max(LOW_LIMIT - 1, int(m[2]))
    x_max = min(HIGH_LIMIT + 1, int(m[3]))
    y_min = max(LOW_LIMIT - 1, int(m[4]))
    y_max = min(HIGH_LIMIT + 1, int(m[5]))
    z_min = max(LOW_LIMIT - 1, int(m[6]))
    z_max = min(HIGH_LIMIT + 1, int(m[7]))

    if action == 'on':
        new_cube_value = True
    else:
        new_cube_value = False

    # Change the core
    for x in range(x_min, x_max + 1):
        if x < LOW_LIMIT or x > HIGH_LIMIT:
            next
        
        for y in range(y_min, y_max + 1):
            if y < LOW_LIMIT or y > HIGH_LIMIT:
                next

            for z in range(z_min, z_max + 1):
                if z < LOW_LIMIT or z > HIGH_LIMIT:
                    next

                core[x][y][z] = new_cube_value
            
    return


def count_cubes_on(core: dict) -> int:
    '''count all cubes which have vale True'''
    count = 0

    for x in range(LOW_LIMIT, HIGH_LIMIT + 1):
        for y in range(LOW_LIMIT, HIGH_LIMIT + 1):
            for z in range(LOW_LIMIT, HIGH_LIMIT + 1):
                if core[x][y][z]:
                    count += 1

    return count


# Main function
def get_solution(lines: list) -> int:
    '''Main function'''
    core = create_reactor_core()

    for line in lines:
        process_line(core, line)

    return count_cubes_on(core)


if __name__ == '__main__':
    pass