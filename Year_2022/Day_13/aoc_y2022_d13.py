"""
Year 2022, Day 13

Problem description: See https://adventofcode.com/2022/day/13

"""

# Imports
from pprint import pprint
import json

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


# Classes

class Pairs(dict):
    '''Container class of pairs'''
    
    def __init__(self, lines: list[str]) -> None:
        i = 0
        pair_index = 1

        while i < len(lines):
    
            if lines[i] == '':
                i += 1
                next

            self[pair_index] = Pair(lines[i], lines[i+1])
            i += 2
            pair_index += 1


class Pair():
    '''Pair of left_packet and right_packet'''

    def __init__(self, left_line:str , right_line: str) -> None:
        self.left = Packet(json.loads(left_line))
        self.right = Packet(json.loads(right_line))


class Packet(list):
    '''Packet, containing integers and lists'''

    def __init__(self, packet_list: list) -> None:
        for packet_item in packet_list:
            if type(packet_item) == int:
                self.append(packet_item)
            elif type(packet_item) == list:
                self.append(Packet(packet_item))
            else:
                raise RuntimeError('Wrong type: {}, item {}'.format(
                    type(packet_item), packet_item,
                ))


# Main functions
def get_solution_part1(lines: list[str]) -> int:
    '''Main function'''

    pairs = Pairs(lines)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str]) -> int:
    '''Main function'''


    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass