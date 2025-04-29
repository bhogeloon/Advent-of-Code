"""
Year 2024, Day 8

Problem description: See https://adventofcode.com/2024/day/8

The following classes are used:
- Location: Represents a location on the map, with a frequency if an antenna
    is present and a antinode flag.
- Frequencies: Dict with as key all frequencies. The value is a list of all
    locations containing an antenna with this frequency.
- Map: Grid class containing Location objects.

Part 1: Go through the Frequencies dict and for each frequence extrapolate
each location pair in both directions. Flag those locations as antinode.
Then count the antinode locations.

Part 2: Extrapolate the location pair until you go off the grid. It was a 
little unclear that in this case also the antenna position themselves are
counted, but once I got that, I got the right result.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from grid import Grid2D

# Constants


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
    '''A location on the map with a frequency and an x and y coordinate'''
    def __init__(self, freq: str):
        if freq == '.':
            self.freq = None
        else:
            self.freq = freq

        # Indicates whether an antinode will be present
        self.antinode = False


class Frequencies(dict[str,list[Location]]):
    '''Dict class with frequence as key pointing to a list of antenna 
    locations'''
    def __init__(self, map: Map):
        for loc in map.grid.flat:
            if loc.freq is not None:
                if loc.freq not in self.keys():
                    self[loc.freq] = [loc]
                else:
                    self[loc.freq].append(loc)


class Map(Grid2D):
    '''Map containing several Antenna's'''
    def __init__(self, lines: list[str]):
        self.size_x = len(lines[0])
        self.size_y = len(lines)
        super().__init__(
            sizes=(self.size_x,self.size_y),
            cell_class=Location,
            input_lines=lines,
        )

        # Fill the frequencies table
        self.freqs = Frequencies(self)


    def get_unique_antinodes(self) -> int:
        '''Return the total amount of unique antinode locations'''
        result = 0

        for loc in self.grid.flat:
            if loc.antinode:
                result += 1

        return result


    def calulate_antinodes(self, part=1) -> None:
        '''Calculate the positions of the antinodes'''
        for (freq, antennas) in self.freqs.items():
            # ignore if only one antenna
            if len(antennas) == 1:
                continue

            # Now calculate for each pair
            for i in range(len(antennas)-1):
                for j in range(i+1,len(antennas)):
                    Gv.log.debug(
                        f"Calculating coords for ({antennas[i].x},"
                        f"{antennas[i].y}), ({antennas[j].x},"
                        f"{antennas[j].y}), freq: {freq}")
                    if part == 1:
                        self.get_new_coord(
                            (antennas[i].x, antennas[i].y),
                            (antennas[j].x, antennas[j].y)
                        )
                    else:
                        self.get_new_coord2(
                            (antennas[i].x, antennas[i].y),
                            (antennas[j].x, antennas[j].y)
                        )

                        # Now also set the antinode for the antennas themselves
                        antennas[i].antinode = True
                        antennas[j].antinode = True


    def get_new_coord(self, c1:tuple[int], c2: tuple[int]) -> None:
        '''Extrapolate the 2 points on both sides and return a list
        of new coordinates'''
        result = []
        (x1,y1) = c1
        (x2,y2) = c2

        # Take into account the different directions
        if x1 == x2:
            new_x1 = x1
            new_x2 = x2
            new_y1 = min(y1,y2) - abs(y1-y2)
            new_y2 = max(y1,y2) + abs(y1-y2)
        elif y1 == y2:
            new_x1 = min(x1,x2) - abs(x1-x2)
            new_x2 = max(x1,x2) + abs(x1-x2)
            new_y1 = y1
            new_y2 = y2
        elif (x1-x2) / (y1-y2) > 0:
            new_x1 = min(x1,x2) - abs(x1-x2)
            new_x2 = max(x1,x2) + abs(x1-x2)
            new_y1 = min(y1,y2) - abs(y1-y2)
            new_y2 = max(y1,y2) + abs(y1-y2)
        else:
            new_x1 = min(x1,x2) - abs(x1-x2)
            new_x2 = max(x1,x2) + abs(x1-x2)
            new_y2 = min(y1,y2) - abs(y1-y2)
            new_y1 = max(y1,y2) + abs(y1-y2)

        self.store_coords((new_x1,new_y1))
        self.store_coords((new_x2,new_y2))

        return result
    

    def store_coords(self, coords: tuple[int]) -> None:
        '''Store the coords if they are within the grid'''
        if self.is_in_grid(coords):
            self.grid[coords[0],coords[1]].antinode = True
            Gv.log.debug(f"Setting antinode for ({coords[0]},{coords[1]})")


    def get_new_coord2(self, c1:tuple[int], c2: tuple[int]) -> list[tuple[int]]:
        '''Extrapolate the 2 points on both sides and return a list
        of new coordinates'''
        result = []
        (x1,y1) = c1
        (x2,y2) = c2

        # Take into account the different directions
        if x1 == x2:
            # extend up
            new_x = x1
            cur_y = min(y1,y2)
            while cur_y >= 0:
                new_y = cur_y - abs(y1-y2)
                self.store_coords((new_x,new_y))
                cur_y = new_y

            # extend down
            cur_y = max(y1,y2)
            while cur_y < self.size_y:
                new_y = cur_y + abs(y1-y2)
                self.store_coords((new_x,new_y))
                cur_y = new_y
                
        elif y1 == y2:
            # extend to left
            new_y = y1
            cur_x = min(x1,x2)
            while cur_x >= 0:
                new_x = cur_x - abs(x1-x2)
                self.store_coords((new_x,new_y))
                cur_x = new_x

            # extend to right
            cur_x = max(x1,x2)
            while cur_x < self.size_x:
                new_x = cur_x + abs(x1-x2)
                self.store_coords((new_x,new_y))
                cur_x = new_x

        # Extend left up to right down
        elif (x1-x2) / (y1-y2) > 0:
            # Extend to left up
            cur_x = min(x1,x2)
            cur_y = min(y1,y2)
            while cur_x >= 0 and cur_y >=0:
                new_x = cur_x - abs(x1-x2)
                new_y = cur_y - abs(y1-y2)
                self.store_coords((new_x,new_y))
                cur_x = new_x
                cur_y = new_y

            # Extend to right down
            cur_x = max(x1,x2)
            cur_y = max(y1,y2)
            while cur_x < self.size_x and cur_y < self.size_y:
                new_x = cur_x + abs(x1-x2)
                new_y = cur_y + abs(y1-y2)
                self.store_coords((new_x,new_y))
                cur_x = new_x
                cur_y = new_y

        # Extend left down to right up
        else:
            # Extend to left down
            cur_x = min(x1,x2)
            cur_y = max(y1,y2)
            while cur_x >= 0 and cur_y < self.size_y:
                new_x = cur_x - abs(x1-x2)
                new_y = cur_y + abs(y1-y2)
                self.store_coords((new_x,new_y))
                cur_x = new_x
                cur_y = new_y

            # Extend to right up
            cur_x = max(x1,x2)
            cur_y = min(y1,y2)
            while cur_x < self.size_x and cur_y >= 0:
                new_x = cur_x + abs(x1-x2)
                new_y = cur_y - abs(y1-y2)
                self.store_coords((new_x,new_y))
                cur_x = new_x
                cur_y = new_y

        return result


    def __str__(self) -> str:
        '''String representation'''
        result = '\n'

        for y in range(self.sizes[1]):
            for x in range(self.sizes[0]):
                if self.grid[x,y].freq is None:
                    if self.grid[x,y].antinode:
                        result += '#'
                    else:
                        result += '.'
                else:
                    result += str(self.grid[x,y].freq)
            result += '\n'

        return result


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    map = Map(lines)
    map.calulate_antinodes()
    Gv.log.debug(str(map))

    return map.get_unique_antinodes()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    map = Map(lines)
    map.calulate_antinodes(part=2)
    Gv.log.debug(str(map))

    return map.get_unique_antinodes()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
