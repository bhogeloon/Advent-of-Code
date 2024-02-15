"""
Day 18, Part 1

Problem description: See https://adventofcode.com/2021/day/18

My solution:
Part 1:

This puzzle needs to be done step by step.
- We begin with reading the input. For this we use the json module.
- Next we will turn the snail_fishes into a deque, so that we can pop two of them
  from the left and return the result of an addition again to the left.
- Now comes the trickier part: The reducing. We try each time first to explode and
  if that has no result to split. Once no action has taken place, move on to the
  next addition.
- In order to explode, we turn the list back into a json string and manipulate
  the string according the rules (doing it with recursive functions proved to be
  far too complex).
- For the split we use a recursive function.
- Finally for calculating the magnitude, we use a recursive function again.
"""

# Imports
import json
from collections import deque
import re

# Constants

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def read_snail_fish(lines):
    '''Returns a list of snail_fish objects'''
    snail_fishes = deque()

    for line in lines:
        snail_fish = json.loads(line)
        snail_fishes.append(snail_fish)

    return snail_fishes


def replace_left(left_str: str, left_val:int) -> str:
    '''Returns the string which has added left_val to the right most number'''
    m = re.search(r'(\d+)([,\[\]]+)\[$', left_str)

    # if not found, return str unchanged else, kindly do the needful
    if m:
        new_value = int(m.group(1)) + left_val

        return left_str[:m.start(1)] + str(new_value) + m.group(2)
    else:
        return left_str[:-1]


def replace_right(right_str: str, right_val:int) -> str:
    '''Returns the string which has added left_val to the right most number'''
    m = re.match(r'^\]([,\[\]]+)(\d+)', right_str)

    # if not found, return str unchanged else, kindly do the needful
    if m:
        new_value = int(m.group(2)) + right_val

        return m.group(1) + str(new_value) + right_str[m.end(2):]
    else:
        return right_str[1:]


def explode_fish(fish: list) -> list:
    '''Attempts to explode a fish. Returns the modified list or an empty
    list if nothing has been changed'''
    # First, convert fish list into a json string
    fish_str = json.dumps(fish, separators=(',',';'))
    level = 0

    for i in range(len(fish_str)):
        if fish_str[i] == '[':
            level += 1
        elif fish_str[i] == ']':
            level -= 1
        elif level > 4:
            m = re.match(r'^(\d+),(\d+)\]', fish_str[i:])

            if m:
                left_val = int(m.group(1))
                right_val = int(m.group(2))

                left_str = fish_str[:i]
                left_str = replace_left(left_str, left_val)
                right_str = fish_str[i + m.end(2):]
                right_str = replace_right(right_str, right_val)

                new_str = left_str + '0' + right_str

                return json.loads(new_str)

    return []


def split_fish(fish: list) -> bool:
    '''Performs split on fish. Returns True if split has taken place'''
    left_el, right_el = fish

    if type(left_el) == int:
        if left_el >= 10:
            fish[0] = [
                left_el // 2,
                (left_el // 2) + (left_el % 2),
            ]

            return True

    elif type(left_el) == list:
        if split_fish(left_el):
            return True

    else:
        raise RuntimeError("weird type: {}".format(type(left_el)))

    if type(right_el) == int:
        if right_el >= 10:
            fish[1] = [
                right_el // 2,
                (right_el // 2) + (right_el % 2),
            ]

            return True

    elif type(right_el) == list:
        if split_fish(right_el):
            return True

    else:
        raise RuntimeError("weird type: {}".format(type(right_el)))

    return False


def add_snail_fish(fish1: list, fish2: list) -> list:
    '''Returns the result of addition of fish1 and fish2'''
    new_fish = [fish1, fish2]

    # Repeat process until no reduction has taken place:
    reduced = True

    while reduced:
        reduced_fish = explode_fish(new_fish)

        if len(reduced_fish) == 0:
            reduced = split_fish(new_fish)
        else:
            reduced = True
            new_fish = reduced_fish

    return new_fish


def calculate_magnitude(fish: list) -> int:
    '''Recursive function to return the magnitude'''
    magnitude = 0

    left_el, right_el = fish

    if type(left_el) == int:
        magnitude += 3 * left_el
    elif type(left_el) == list:
        magnitude += 3 * calculate_magnitude(left_el)
    else:
        raise RuntimeError("weird type: {}".format(type(left_el)))

    if type(right_el) == int:
        magnitude += 2 * right_el
    elif type(right_el) == list:
        magnitude += 2 * calculate_magnitude(right_el)
    else:
        raise RuntimeError("weird type: {}".format(type(right_el)))

    return magnitude


def get_final_magnitude(lines):
    '''Main function'''
    snail_fishes = read_snail_fish(lines)

    while len(snail_fishes) > 1:
        fish1 = snail_fishes.popleft()
        fish2 = snail_fishes.popleft()

        new_fish = add_snail_fish(fish1, fish2)
        snail_fishes.appendleft(new_fish)

    print(snail_fishes[0])

    return calculate_magnitude(snail_fishes[0])


if __name__ == '__main__':
    lines = read_input('input.txt')
    # lines = read_input('example1.txt')
    print("Magnitude of final sum:", get_final_magnitude(lines))
