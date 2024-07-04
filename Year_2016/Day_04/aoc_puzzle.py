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

"""

# Imports
from pprint import pprint
import re
# From aoc_lib
from sortable_dict import SortableDict


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

        # Create empty (sortable) dict        
        self.char_occ = SortableDict()
        # Fill the dict with the character occurences
        self.count_chars()
        # Sort on key (secondary)
        self.char_occ.sort_by_key()
        # Sort on value (primary) and reverse order
        self.char_occ.sort_by_value(reverse=True)
        

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


    def is_real(self) -> bool:
        '''Check if the room is real'''
        # Get first 5 keys in the char_occ dict and store in a set
        top5 = set(list(self.char_occ.keys())[:5])

        return top5 == self.checksum


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

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
