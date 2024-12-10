"""
Year 2022, Day 12

Problem description: See https://adventofcode.com/2022/day/12

<Include solution description>

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from grid import Grid2D
import sys

sys.setrecursionlimit(10000)

# Constants

# Very Large Number. Start value of the distances
VLN = 99999999999

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False

    # Variable that will be used for holding the logger object
    log = None

    def __init__(self, test: bool, logger: Logger, **kwargs) -> None:
        '''Initialize the global variables'''
        Gv.test = test
        Gv.log = logger


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

        self.dist_to_start = VLN
        self.dist_to_end = VLN


class Map(Grid2D):
    '''Matrix of locations'''

    def __init__(self, lines: list[str]) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        super().__init__(sizes=(self.x_size,self.y_size))
        self.locations = self.grid
        self.set_locations(lines)
        self.cur_path = []


    def set_locations(self, lines: list[str]) -> None:
        '''Initialise the locations'''
        for x in range(self.x_size):
            for y in range(self.y_size):
                self.locations[x,y] = Location(lines[y][x])

                # Register start and endpoints
                if lines[y][x] == 'S':
                    self.startpoint = (x,y)
                elif lines[y][x] == 'E':
                    self.endpoint = (x,y)
                    # pprint(self.endpoint)


    def find_path_from_start(self, start:tuple|None=None) -> int:
        '''Find the path from the given start point (by default the original
        starting point will be used). Return the path length'''
        if start is None:
            s_x, s_y = self.startpoint
        else:
            s_x, s_y = start

        self.get_next_in_path(s_x,s_y,1)
        return self.locations[s_x,s_y].dist_to_end

        e_x, e_y = self.endpoint
        # Return te distance to start from the end point
        return self.locations[e_x,e_y].dist_to_start


    def get_next_in_path(self, x:int, y:int, height: int):
        '''Investigate the path for this point towards the endpoint'''
        location = self.locations[x,y]
        msg = f'inv. loc. {x}, {y}: dist_to_end: {location.dist_to_end}'
        Gv.log.debug(msg)

        # If the height of this location is too large
        if location.height > height + 1:
            msg = f'\tHeight diff too large: {location.height-height}. '
            msg += f'Returning {VLN}'
            Gv.log.debug(msg)
            return VLN

        # If this point is already part of the current path
        if (x,y) in self.cur_path:
            msg = f'\tpoint in path. returning {VLN}'
            Gv.log.debug(msg)
            return VLN
        
        # If the distance to end is already known, just return it + 1
        if location.dist_to_end < VLN:
            msg = f'\tenddist already known. returning {location.dist_to_end+1}'
            Gv.log.debug(msg)
            return location.dist_to_end + 1

        # If the endpoint is found, return 1 (as dist to endpoint)
        if location.endpoint:
            msg = f'\tEnd point found. returning 1'
            Gv.log.debug(msg)
            return 1
        
        dist_to_start = len(self.cur_path)

        # If the distance is larger (or equal) than already detected
        if dist_to_start >= location.dist_to_start:
            msg = f'\tdist_to_start not smaller than known. '
            msg += f'known: {location.dist_to_start} '
            msg += f'new: {dist_to_start}. Returning {VLN}'
            Gv.log.debug(msg)
            return VLN

        # Update distance to start
        location.dist_to_start = dist_to_start
        # Append this location to the current path
        self.cur_path.append((x,y))

        # Now start to investigate the neighbors
        if x > 0:
            msg = f'\t\tMoving to {x-1}, {y}.'
            Gv.log.debug(msg)
            dist_to_end = self.get_next_in_path(x-1,y, location.height)
            msg = f'\t\t{x}, {y}: result from {x-1}, {y}: {location.dist_to_end}'
            Gv.log.debug(msg)
            if dist_to_end < location.dist_to_end:
                location.dist_to_end = dist_to_end

        if y > 0:
            msg = f'\t\tMoving to {x}, {y-1}.'
            Gv.log.debug(msg)
            dist_to_end = self.get_next_in_path(x,y-1, location.height)
            msg = f'\t\t{x}, {y}: result from {x-1}, {y}: {dist_to_end}'
            Gv.log.debug(msg)
            if dist_to_end < location.dist_to_end:
                location.dist_to_end = dist_to_end

        if x < self.x_size - 1:
            msg = f'\t\tMoving to {x+1}, {y}.'
            Gv.log.debug(msg)
            dist_to_end = self.get_next_in_path(x+1,y, location.height)
            msg = f'\t\t{x}, {y}: result from {x-1}, {y}: {dist_to_end}'
            Gv.log.debug(msg)
            if dist_to_end < location.dist_to_end:
                location.dist_to_end = dist_to_end

        if y < self.y_size - 1:
            msg = f'\t\tMoving to {x}, {y+1}.'
            Gv.log.debug(msg)
            dist_to_end = self.get_next_in_path(x,y+1, location.height)
            msg = f'\t\t{x}, {y}: result from {x-1}, {y}: {dist_to_end}'
            Gv.log.debug(msg)
            if dist_to_end < location.dist_to_end:
                location.dist_to_end = dist_to_end

        # Remove this location from the path before giving the control back
        self.cur_path.pop()

        # Return the distance to end + 1
        msg = f'\t{x}, {y}: After investigating: Returning {location.dist_to_end+1}'
        Gv.log.debug(msg)
        return location.dist_to_end + 1


    def start_path_search(self) -> int:
        '''Start the search starting from the fixed Start point'''
        e_x, e_y = self.endpoint
        self.investigate_path(e_x, e_y, 27)

        s_x, s_y = self.startpoint
        # Return te distance to end from the starting point
        return self.locations[s_x,s_y].dist_to_end
    

    def get_shortest_path(self) -> int:
        e_x, e_y = self.endpoint
        self.investigate_path(e_x, e_y, 27)

        path_lengths = []

        for location in self.locations.flat:
            if location.height == 1:
                path_lengths.append(location.dist_to_end)

        return min(path_lengths)


    def get_shortest_path_from_any_a(self) -> int:
        '''Find the shortes path from any a point as starting point'''
        self.find_path_from_start()
        path_lengths = []

        for location in self.locations.flat:
            if location.height == 1:
                path_lengths.append(location.dist_to_end)

        return min(path_lengths)


    def investigate_path(self, x:int, y:int, height: int):
        '''Investigate the path for this point towards the endpoint'''
        location = self.locations[x,y]

        # If the height of this location is too large
        if location.height < height - 1:
            # pprint(height, location.height)
            return

        # If this point is already part of the current path
        if (x,y) in self.cur_path:
            return
        
        dist_to_end = len(self.cur_path)

        # If the distance is larger (or equal) than already detected
        if dist_to_end >= location.dist_to_end:
            return

        # Update distance to end
        location.dist_to_end = dist_to_end
        # Append this location to the current path
        self.cur_path.append((x,y))

        # Now start to investigate the neighbors
        if x > 0:
            self.investigate_path(x-1,y, location.height)

        if y > 0:
            self.investigate_path(x,y-1, location.height)

        if x < self.x_size - 1:
            self.investigate_path(x+1,y, location.height)

        if y < self.y_size - 1:
            self.investigate_path(x,y+1, location.height)

        # Remove this location from the path before giving the control back
        self.cur_path.pop()

        return


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    map = Map(lines)

    return map.find_path_from_start()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    map = Map(lines)

    return map.get_shortest_path()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
