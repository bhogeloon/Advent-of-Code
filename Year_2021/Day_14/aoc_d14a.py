"""
Day 14, Part 1

Problem description: See https://adventofcode.com/2021/day/14

My solution:
- Read the first line and store in variable polymer
- Read the rest of the lines and store it in a dict called pair_ins
- Create function to do the insertions (pol_insert). This will create
  a new polymer string which replaces the old one.
- Execute function 10 times
- Write a function to return a dict with the amount of occurrunces
  per element (get_element_occurences)
"""

# Imports
from collections import Counter

# Global values


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def pol_insert(old_pol: str, pair_ins: dict) -> str:
    '''Returns a new string with the inserted elements'''
    new_pol = ''

    for nr in range(len(old_pol)):
        # Write current char
        new_pol += old_pol[nr]
        # Don't look ahead if last char
        if nr < len(old_pol) - 1:
            char_left = old_pol[nr]
            char_right = old_pol[nr + 1]
            combi = char_left + char_right
            # Check if a key exist
            if combi in pair_ins.keys():
                # Write extra element
                new_pol += pair_ins[combi]

    return new_pol


def create_pair_ins(lines: list) -> dict:
    '''Returns dict with the pair as key and the insertion as value'''
    pair_ins = {}

    for line in lines:
        pair, ins = line.split(' -> ')
        pair_ins[pair] = ins

    return pair_ins


def get_difference(lines):
    '''Main function to get the difference between max and min'''
    polymer = lines[0]

    pair_ins = create_pair_ins(lines[2:])

    for i in range(10):
        polymer = pol_insert(polymer, pair_ins)

    occ = Counter(polymer)

    min = -1
    max = 0

    for nr in occ.values():
        if nr > max:
            max = nr

        if min < 0 or nr < min:
            min = nr

    return max - min


if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Difference between max and min:", get_difference(lines))
