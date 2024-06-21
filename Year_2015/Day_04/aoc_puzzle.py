"""
Year 2015, Day 4

Problem description: See https://adventofcode.com/2015/day/4

The following class is used:
- SecretKey: Represent the initial secret key

Part 1: Go over all integers starting with 1, extend the key with the integer and calculate
the MD5 key using the Python haslib until you encounter a string starting with 5 leading 0's.

"""

# Imports
from pprint import pprint
import hashlib


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes
class SecretKey():
    '''This represents the secret key (the puzzle input)'''

    def __init__(self, line:str) -> None:
        self.key = line


    def mine_coin(self) -> int:
        '''Get the lowest number where the MD5 hash for the combined string starts
        with 5 leading 0's'''
        result = 0

        while True:
            result += 1
            comb_str = self.key + str(result)
            md5_obj = hashlib.md5(comb_str.encode())
            md_hash_str = md5_obj.hexdigest()

            if md_hash_str[:5] == '00000':
                return result


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    secret_key = SecretKey(lines[0])

    return secret_key.mine_coin()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
