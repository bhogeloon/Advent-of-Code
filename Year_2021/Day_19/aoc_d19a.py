"""
Day 19, Part 1

Problem description: See https://adventofcode.com/2021/day/19

My solution:
Part 1:
- First read the input. Create a list of scanners. Each scanner has a number of (dict)
  properties. One of them is 'beacon_coords': the list of Beacon Coördinates

"""

# Imports

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


def retrieve_scanners(lines):
    '''Returns a list of scanners'''
    scanners = []
    current_scanner = {}

    for line_nr, line in enumerate(lines):
        if line[:3] == '---':
            current_scanner['name'] = line
            current_scanner['beacon_coords'] = []
            continue

        if line == '':
            scanners.append(current_scanner)
            current_scanner = {}
            continue

        coords = [int(nr) for nr in line.split(',')]

        current_scanner['beacon_coords'].append(coords)

        if line_nr == len(lines) - 1:
            scanners.append(current_scanner)

    return scanners


def get_nr_of_beacons(lines):
    '''Main function'''
    scanners = retrieve_scanners(lines)

    print(scanners)

    return 0


if __name__ == '__main__':
    lines = read_input('input.txt')
    # lines = read_input('example1.txt')
    print("Number of Beacons:", get_nr_of_beacons(lines))
