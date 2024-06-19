"""
Year 2019, Day 3

Problem description: See https://adventofcode.com/2019/day/3

We use the following classes:
- Grid: This is a grid that stores only the points that are used by the wire (using a dict of dicts). Otherwise we
    would have to create a very large grid.
- Instruction: contains an instruction to extend the wire
- Wire: Represents the wire, containing instructions to extend the wire.

Part 1: Follow the instructions per wire and store an entry for the wire in the grid at each position where the wire
runs. A set is used to prevent the wires crossing themselves to be counted.

"""

# Imports
from pprint import pprint


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes
class Grid(dict):
    '''This class represents the grid, but it will only contain the the points where the wires are running.
    There is no use in creating a full blown 2D grid.
    The Grid class is a dict class. It contains an entry for each y value. Each y-key will contain a new
    dict for each x value. Each x-key value will contain a set of wire index which are crossing that point'''

    def add_point(self, x, y , index):
        '''Add a wire point in the grid'''

        # If no y value is found, create a new dict with key y
        if y not in self.keys():
            self[y] = {}

        # If no x value is found, create a new empty set on this location
        if x not in self[y].keys():
            self[y][x] = set()

        # Add the index value of the wire to the set
        self[y][x].add(index)


    def get_distance(self, x, y) -> int:
        # The distance to 0,0 is the sum of the absolute values
        return abs(x) + abs(y)


    def get_closest_cross(self) -> int:
        '''Determine the closest point to 0,0 on the grid where there are two wires'''

        # This will contain the closest distance
        min_dist = None

        # For each existing point on the grid
        for y in self.keys():
            for x in self[y].keys():
                # print(x, y, self[y][x])

                # Ignore this point if 0,0
                if x == 0 and y == 0:
                    continue

                # If the set contains more than 1 wire index
                if len(self[y][x]) > 1:
                    # Determine the distance
                    this_dist = self.get_distance(x, y)

                    # If this one is smaller than the min_dist (or it is the first one found)
                    if min_dist == None or min_dist > this_dist:
                        min_dist = this_dist

        return min_dist


class Instruction():
    '''Represents an instruction to extend the wire'''
    def __init__(self, line: str) -> None:
        # Direction of the instruction
        self.dir = line[0]
        # amount of steps
        self.amount = int(line[1:])


class Wire():
    '''Represents a wire, starting at position 0,0'''
    def __init__(self, index: int, line: str) -> None:
        # Number of the wire (1 or 2)
        self.index = index
        # Creat all the instructions
        self.instrs = [Instruction(line_part) for line_part in line.split(',')]
        # The ptrs represent the current position of the wire end
        self.ptr_x = 0
        self.ptr_y = 0


    def run_instr(self, instr: Instruction, grid: Grid):
        '''Run a single instruction.
        Depending on the direction, the function is redirected'''
        if instr.dir == "U":
            self.follow_up(instr.amount, grid)
        elif instr.dir == "D":
            self.follow_down(instr.amount, grid)
        elif instr.dir == "R":
            self.follow_right(instr.amount, grid)
        elif instr.dir == "L":
            self.follow_left(instr.amount, grid)
        else:
            raise RuntimeError("Unkown direction: '{}'.".format(instr.dir))


    def follow_up(self, y_amount: int, grid: Grid):
        '''For each point in the proper direction add a grid point'''
        for y in range(self.ptr_y + 1, self.ptr_y + y_amount + 1):
            grid.add_point(self.ptr_x, y, self.index)

        # Update the wire end point
        self.ptr_y += y_amount


    def follow_down(self, y_amount: int, grid: Grid):
        '''For each point in the proper direction add a grid point'''
        for y in range(self.ptr_y - 1, self.ptr_y - y_amount - 1, -1):
            grid.add_point(self.ptr_x, y, self.index)

        # Update the wire end point
        self.ptr_y -= y_amount


    def follow_right(self, x_amount: int, grid: Grid):
        '''For each point in the proper direction add a grid point'''
        for x in range(self.ptr_x + 1, self.ptr_x + x_amount + 1):
            grid.add_point(x, self.ptr_y, self.index)

        # Update the wire end point
        self.ptr_x += x_amount


    def follow_left(self, x_amount: int, grid: Grid):
        '''For each point in the proper direction add a grid point'''
        for x in range(self.ptr_x - 1, self.ptr_x - x_amount - 1, -1):
            grid.add_point(x, self.ptr_y, self.index)

        # Update the wire end point
        self.ptr_x -= x_amount


    def run_instrs(self, grid: Grid):
        '''Run all instructions for this wire'''
        for instr in self.instrs:
            self.run_instr(instr, grid)


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    grid = Grid()
    wires= []

    for i, line in enumerate(lines):
        # Creat the Wire objects
        wires.append(Wire(i, line))
        # Run all the instructions and update the grid along the way
        wires[i].run_instrs(grid)

    return grid.get_closest_cross()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
