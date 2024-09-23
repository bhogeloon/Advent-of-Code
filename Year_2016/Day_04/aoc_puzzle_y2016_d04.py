"""
Year 2016, Day 4

Problem description: See https://adventofcode.com/2016/day/4

We use the following classes:
- Room: Represents a room with a name, sector_id, checksum and a dict which keeps track of how many
    occurences there are of each character (for this I use a inhereted class that I have extended with
    sort methods)
- Rooms: List container class of Room objects.

Part 1: Count all the character occurences of each room and sort those occurences on value and then key.
Then get the top 5 and compare those with the checksum.

Part 2: For every room name, add the offset (sector_id % 26) and make sure you get back to a if behind z.
Then search for the string 'north' and print the sector_id
"""

# Imports
from pprint import pprint
import re
from collections import Counter
# From aoc_lib
from sortable_dict import SortableDict


# Constants

# Alphabet size
AB_SIZE = 26
AB_BASE = ord('a')


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

        # Create SortableDict with the character occurences
        self.count_chars()
        # Sort on key (secondary)
        self.char_occ.sort_by_key()
        # Sort on value (primary) and reverse order
        self.char_occ.sort_by_value(reverse=True)
        

    def count_chars(self) -> None:
        '''Count all the chars in the name and store in char_occ'''
        ctr = Counter(self.name)

        # Delete any '-'s
        if '-' in ctr.keys():
            del ctr['-']

        # Then store result in a Sortable Dict
        self.char_occ = SortableDict(ctr)        



    def is_real(self) -> bool:
        '''Check if the room is real'''
        # Get first 5 keys in the char_occ dict and store in a set
        top5 = set(list(self.char_occ.keys())[:5])

        return top5 == self.checksum
    

    def get_real_name(self) -> str:
        '''Returns the real name of the room, preceeded by the sector_ID and followed by \n'''
        offset = self.sector_id % AB_SIZE

        real_name = ''

        for char in self.name:
            if char == '-':
                real_name += ' '
            else:
                new_char = chr(((ord(char) - AB_BASE + offset) % AB_SIZE) + AB_BASE)
                real_name += new_char

        return str(self.sector_id) + ': ' + real_name + '\n'


class Rooms(list[Room]):
    '''List container class of Room objects'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Room(line))


    def get_sector_sum_of_real_rooms(self) -> int:
        '''Get the solution of part 1'''
        result = 0

        for room in self:
            if room.is_real():
                result += room.sector_id

        return result


    def get_real_room(self) -> list:
        '''Returns all the real names of the rooms, preceed by their sector_ID'''
        result = '\n'

        for room in self:
            real_name = room.get_real_name()
            if re.search(r'north', real_name):
                result += real_name

        return result


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    rooms = Rooms(lines)

    return rooms.get_sector_sum_of_real_rooms()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    rooms = Rooms(lines)

    return rooms.get_real_room()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
