"""
Year 2016, Day 5

Problem description: See https://adventofcode.com/2016/day/5

This puzzle is actually very similar to the 2015 day 4 puzzle, so I used
some code from that puzzle and modified it a bit.

The following class is used:
- DoorId: Represent the initial Door ID

Part 1: Go over all integers starting with 0, extend the key with the integer and calculate
the MD5 key using the Python haslib until you encounter a string starting with 5 leading 0's.
Then store the 6th character and repeat this procedure until you get 8 hits.
It takes about 13 seconds to do this. I have no clue on how to optimize this.


"""

# Imports
from pprint import pprint
import hashlib


# Constants

# Length of the password
PASSWD_LEN = 8

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class DoorId():
    '''This represents the Door ID (the puzzle input)'''

    def __init__(self, line:str) -> None:
        self.id = line


    def get_password(self, zeros=5) -> str:
        '''Get the 8 lowest numbers where the MD5 hash for the combined string starts
        with zeros amount of leading 0's'''
        nr = 0
        result = ''
        zeros_str = '0' * zeros

        while True:
            comb_str = self.id + str(nr)
            md5_obj = hashlib.md5(comb_str.encode())
            md_hash_str = md5_obj.hexdigest()

            if md_hash_str[:zeros] == zeros_str:
                result += md_hash_str[zeros]

                print(f'Result is now {result} for nr {nr}, hash {md_hash_str}')

                if len(result) >= PASSWD_LEN:
                    return result

            nr += 1


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    door_id = DoorId(lines[0])

    return door_id.get_password()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
