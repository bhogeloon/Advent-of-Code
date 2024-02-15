"""
Year 2022, Day 12

Problem description: See https://adventofcode.com/2022/day/12

"""

# Imports
from pprint import pprint
import numpy as np
import sys

sys.setrecursionlimit(2000)

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


# Classes

class Location():
    '''Location on map with a certain height'''

    def __init__(self, indicator: str) -> None:
        self.endpoint = False
        if indicator == 'S':
            self.height = 1
        elif indicator == 'E':
            self.height =26
            self.endpoint = True
        else:
            self.height = ord(indicator) - ord('a') + 1

        self.dist_to_start = 999999999
        self.dist_to_end = -1


class Map():
    '''Matrix of locations'''

    def __init__(self, lines: list[str]) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        self.locations = np.full((self.x_size, self.y_size), None)
        self.set_locations(lines)
        self.cur_path = []


    def set_locations(self, lines: list[str]) -> None:
        for x in range(self.x_size):
            for y in range(self.y_size):
                self.locations[x,y] = Location(lines[y][x])
                if lines[y][x] == 'S':
                    self.startpoint = (x,y)
                elif lines[y][x] == 'E':
                    self.endpoint = (x,y)
                    # pprint(self.endpoint)


    def start_path_search(self) -> int:
        s_x, s_y = self.startpoint
        self.investigate_path(s_x, s_y, 0)

        e_x, e_y = self.endpoint
        return self.locations[e_x,e_y].dist_to_start


    def investigate_path(self, x:int, y:int, height: int) -> int:
        location = self.locations[x,y]

        if location.height > height + 1:
            return -1

        if (x,y) in self.cur_path:
            return -1
        
        dist_to_start = len(self.cur_path)

        if dist_to_start >= location.dist_to_start:
            return -1

        location.dist_to_start = dist_to_start

        if location.endpoint:
            # pprint(self.cur_path)
            # pprint(dist_to_start)
            location.dist_to_end = 0
            return 0
        
        self.cur_path.append((x,y))
    
        if x < self.x_size - 1:
            self.investigate_path(x+1,y, location.height)

        if y < self.y_size - 1:
            self.investigate_path(x,y+1, location.height)

        if x > 0:
            self.investigate_path(x-1,y, location.height)

        if y > 0:
            self.investigate_path(x,y-1, location.height)

        self.cur_path.pop()

        return



# Main functions
def get_solution_part1(lines: list[str]) -> int:
    '''Main function'''

    map = Map(lines)
    # print(map.start_point, map.end_point)

    return map.start_path_search()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str]) -> int:
    '''Main function'''


    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass