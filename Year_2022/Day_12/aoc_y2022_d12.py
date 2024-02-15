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
        self.startpoint = False
        if indicator == 'S':
            self.height = 1
            self.startpoint = True
        elif indicator == 'E':
            self.height =26
            self.endpoint = True
        else:
            self.height = ord(indicator) - ord('a') + 1

        self.dist_to_start = 999999999
        self.dist_to_end = 999999999


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
        e_x, e_y = self.endpoint
        self.investigate_path(e_x, e_y, 27)

        s_x, s_y = self.startpoint
        return self.locations[s_x,s_y].dist_to_end
    

    def get_shortest_path(self) -> int:
        e_x, e_y = self.endpoint
        self.investigate_path(e_x, e_y, 27)

        path_lengths = []

        for location in self.locations.flat:
            if location.height == 1:
                path_lengths.append(location.dist_to_end)

        return min(path_lengths)


    def investigate_path(self, x:int, y:int, height: int):
        location = self.locations[x,y]

        if location.height < height - 1:
            # pprint(height, location.height)
            return

        if (x,y) in self.cur_path:
            return
        
        dist_to_end = len(self.cur_path)

        if dist_to_end >= location.dist_to_end:
            return

        location.dist_to_end = dist_to_end
        # pprint(dist_to_end)

        # if location.startpoint:
        #     return
        
        self.cur_path.append((x,y))
    
        if x > 0:
            self.investigate_path(x-1,y, location.height)

        if y > 0:
            self.investigate_path(x,y-1, location.height)

        if x < self.x_size - 1:
            self.investigate_path(x+1,y, location.height)

        if y < self.y_size - 1:
            self.investigate_path(x,y+1, location.height)

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

    map = Map(lines)

    return map.get_shortest_path()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass