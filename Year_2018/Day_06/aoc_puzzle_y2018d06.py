"""
Year 2018, Day 6

Problem description: See https://adventofcode.com/2018/day/6

The following classes are used:
- Location: a location on the grid
- Map: A grid containing Location objects
- Target: Represents a target. Contains coordinates and a link to the Location
- Targets: List container class of Target objects

Part 1:
- Build a map of Locations
- Build a list of Targets from the puzzle input
- For each location on the map, calculate the distances to each Target and
    register the nearest Target (None if more than one exists). Keep track of
    amount of locations which has this Target as nearest target (area)
- Go through the borders of the Map and mark all nearest targets there as 
    being infinite
- Report the largest area for all Targets which are not marked as infinite.

Part 2:
After the first two steps of part 1, go through the whole map and add all
the distances to the targets together. After that count all locations with
a small enough total distance.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from grid import Grid2D


# Constants

# Grid positions are all below 400
GRID_SIZE = 400
MAX_DISTANCE = 10000
MAX_DISTANCE_TEST = 32

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Location:
    '''Represents a location on the grid.'''
    def __init__(self) -> None:
        self.is_target = False
        self.nearest_target = None
        self.distance = 2 * GRID_SIZE
        # Total distance to all targets
        self.total_distance = 0


    def mark_infinite(self) -> None:
        '''Mark the nearest target on this location infinite'''
        if self.nearest_target != None:
            self.nearest_target.infinite = True


class Map(Grid2D):
    '''The grid map of locations'''
    def __init__(self) -> None:
        super().__init__(sizes=(GRID_SIZE,GRID_SIZE), cell_class=Location)

        if Gv.test:
            self.max_dist = MAX_DISTANCE_TEST
        else:
            self.max_dist = MAX_DISTANCE


    def calculate_nearest_target(self, targets: Targets):
        '''Calculate the nearest target'''
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                loc = self.grid[x,y]

                # If this is a target itself, don't bother
                if loc.is_target:
                    continue

                for target in targets:
                    this_dist = target.get_distance_to_loc(x,y)

                    # If equal distance, set nearest target back to None
                    if this_dist == loc.distance:
                        loc.nearest_target = None
                    # Else if smaller change the nearest target
                    elif this_dist < loc.distance:
                        loc.nearest_target = target
                        loc.distance = this_dist

                # Increase area size
                if loc.nearest_target != None:
                    loc.nearest_target.area += 1


    def calculate_total_distance(self, targets: Targets) -> None:
        '''Calculate per location the total distance to all targets'''
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                loc = self.grid[x,y]

                for target in targets:
                    this_dist = target.get_distance_to_loc(x,y)
                    loc.total_distance += this_dist


    def mark_infinite(self) -> None:
        '''Mark all nearest targets at the borders as infinite'''
        for x in range(GRID_SIZE):
            self.grid[x,0].mark_infinite()
            self.grid[x,GRID_SIZE-1].mark_infinite()

        for y in range(GRID_SIZE):
            self.grid[0,y].mark_infinite()
            self.grid[GRID_SIZE-1,y].mark_infinite()


    def get_safe_area(self) -> int:
        '''Calculate the total area of safe locations'''
        area_size = 0

        for loc in self.grid.flat:
            if loc.total_distance < self.max_dist:
                area_size += 1

        return area_size


class Target:
    '''Represents a target with coordinates and a link to a Location
    on the map'''
    def __init__(self, line: str, map: Map) -> None:
        (x_str, y_str) = line.split(', ')
        self.x = int(x_str)
        self.y = int(y_str)
        self.location = map.grid[self.x, self.y]
        self.location.is_target = True
        self.location.nearest_target = self
        self.location.distance = 0
        self.infinite = False
        self.area = 1


    def get_distance_to_loc(self, loc_x: int, loc_y: int):
        '''Get the Manhatten distance between the target and the given
        coordinates of the location'''
        return abs(loc_x-self.x) + abs(loc_y-self.y)
    

class Targets(list[Target]):
    '''List container class of Target objects'''
    def __init__(self, lines: list[str], map: Map) -> None:
        for line in lines:
            self.append(Target(line, map))


    def get_largest_area(self) -> int:
        '''Return the largest non-infinite area'''
        max_area = 0

        for target in self:
            if not target.infinite and target.area > max_area:
                max_area = target.area

        return max_area


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    map = Map()
    targets = Targets(lines, map)
    map.calculate_nearest_target(targets)
    map.mark_infinite()

    return targets.get_largest_area()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    map = Map()
    targets = Targets(lines, map)
    map.calculate_total_distance(targets)

    return map.get_safe_area()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
