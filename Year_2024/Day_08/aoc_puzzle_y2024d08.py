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
    '''An location on the map with a frequency and an x and y coordinate'''
    def __init__(self, freq: str):
        if freq == '.':
            self.freq = None
        else:
            self.freq = freq

        # Indicates whether an antinode will be present
        self.antinode = False


class Frequencies(dict[str,list[Location]]):
    '''Dict class with frequence as key pointing to a list of antenna locations'''
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


    def calulate_antinodes(self) -> None:
        '''Calculate the positions of the antinodes'''
        for (freq, antennas) in self.freqs.items():
            # ignore if only one antenna
            if len(antennas) == 1:
                continue

            # List of coordinates (tuples) that need to contain
            # an antinode list
            antinode_coords = []

            # Now calculate for each pair
            for i in range(len(antennas)-1):
                for j in range(i+1,len(antennas)):
                    Gv.log.debug(
                        f"Calculating coords for ({antennas[i].x},"
                        f"{antennas[i].y}), ({antennas[j].x},"
                        f"{antennas[j].y}), freq: {freq}")
                    antinode_coords.extend(self.get_new_coord(
                        (antennas[i].x, antennas[i].y),
                        (antennas[j].x, antennas[j].y)
                    ))


            # Add antinodes if possible
            for c in antinode_coords:
                if (c[0] >= 0 and c[0] < self.size_x and 
                    c[1] >= 0 and c[1] < self.size_y):
                    self.grid[c[0],c[1]].antinode = True
                    Gv.log.debug(f"Adding antinode at ({c[0]},{c[1]})")
                else:
                    Gv.log.debug(f"Skipping for: ({c[0]},{c[1]})")


    def get_new_coord(self, c1:tuple[int], c2: tuple[int]) -> list[tuple[int]]:
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

        result.append((new_x1, new_y1))
        result.append((new_x2, new_y2))

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

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
