"""
Year 2016, Day 4

Problem description: See https://adventofcode.com/2016/day/4

<Include solution description>

"""

# Imports
from pprint import pprint
import re


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Room:
    '''Represents a room with a name, sector_id, checksum and char_occ.
    char_occ is a dict with occuring characters as key and the amount of occurences as value'''

    def __init__(self, line: str) -> None:
        m = re.fullmatch(r'([a-z-]+)-(\d+)\[([a-z]+)\]', line)

        if not m:
            raise RuntimeError('Could not match <{}>'.format(line))
        
        self.name = m.group(1)
        self.sector_id = int(m.group(2))
        self.checksum = set(m.group(3))

        if len(self.checksum) != 5:
            raise RuntimeError('Invalid checksum: {}'.format(m.group(3)))
        
        self.char_occ = {}
        
        self.count_chars()
        

    def count_chars(self) -> None:
        '''Count all the chars in the name and store in char_occ'''
        for char in self.name:
            # Ignore if dash
            if char == "-":
                continue

            if char in self.char_occ.keys():
                self.char_occ[char] += 1
            else:
                self.char_occ[char] = 1

        pprint(self.char_occ)


class Rooms(list):
    '''List container class of Room objects'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Room(line))


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    rooms = Rooms(lines)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
