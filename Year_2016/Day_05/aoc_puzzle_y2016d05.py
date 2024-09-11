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

Part 2 was achieved by pre-formatting the result into _'s and then filling them in
gradually until all the _'s were gone.
I was a bit confused what the action required was when you get a position that was
already filled in: ignore it or replace it?
Using the test-input and the required result, I found out that you have to ignore it.
Part 2 took 37 seconds.

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

    # Class variables
    pos_chars = ''
    for i in range(PASSWD_LEN):
        pos_chars += chr(ord('0') + i)

    def __init__(self, line:str) -> None:
        self.id = line


    def get_password_p1(self, zeros=5) -> str:
        '''Get the 8 lowest numbers where the MD5 hash for the combined string starts
        with zeros amount of leading 0's and store the 6th char'''
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


    def get_password_p2(self, zeros=5) -> str:
        '''Get the 8 lowest numbers where the MD5 hash for the combined string starts
        with zeros amount of leading 0's and store the 7th char in the position of the
        6th char'''
        nr = 0
        result = [ '_' for i in range(PASSWD_LEN)]
        zeros_str = '0' * zeros

        while True:
            comb_str = self.id + str(nr)
            md5_obj = hashlib.md5(comb_str.encode())
            md_hash_str = md5_obj.hexdigest()

            if md_hash_str[:zeros] == zeros_str:
                pos_str = md_hash_str[zeros]

                # Ignore if not 8 positions
                if pos_str not in self.pos_chars:
                    print(f'Ignoring nr {nr}, hash {md_hash_str}')
                    nr += 1
                    continue

                pos = int(pos_str)

                # If number already occupied
                if result[pos] != "_":
                    print(f'Double pos {pos} for nr {nr}, hash {md_hash_str}')
                    nr += 1
                    continue

                result[pos] = md_hash_str[zeros + 1]

                print(f"Result is now {''.join(result)} for nr {nr}"
                      f", hash {md_hash_str}")

                if '_' not in result:
                    return ''.join(result)

            nr += 1


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    door_id = DoorId(lines[0])

    return door_id.get_password_p1()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    door_id = DoorId(lines[0])

    return door_id.get_password_p2()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
