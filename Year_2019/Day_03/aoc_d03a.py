"""
Year 2019, Day 3, Part 1

Problem description: See https://adventofcode.com/2019/day/3

"""

# Imports
from lib2to3.refactor import MultiprocessRefactoringTool
from pprint import pprint

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Grid(dict):
    def add_point(self, x, y , index):
        if y not in self.keys():
            self[y] = {}

        if x not in self[y].keys():
            self[y][x] = set()

        self[y][x].add(index)


    def get_distance(self, x, y) -> int:
        return abs(x) + abs(y)


    def get_closest_cross(self) -> int:
        min_dist = None

        for y in self.keys():
            for x in self[y].keys():
                # print(x, y, self[y][x])
                if x == 0 and y == 0:
                    continue
                if len(self[y][x]) > 1:
                    this_dist = self.get_distance(x, y)
                    if min_dist == None or min_dist > this_dist:
                        min_dist = this_dist

        return min_dist


class Instruction():
    def __init__(self, line: str) -> None:
        self.dir = line[0]
        self.amount = int(line[1:])


class Wire():
    def __init__(self, index: int, line: str) -> None:
        self.index = index
        self.instrs = [Instruction(line_part) for line_part in line.split(',')]
        self.ptr_x = 0
        self.ptr_y = 0


    def run_instr(self, instr: Instruction, grid: Grid):
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
        for y in range(self.ptr_y + 1, self.ptr_y + y_amount + 1):
            grid.add_point(self.ptr_x, y, self.index)

        self.ptr_y += y_amount


    def follow_down(self, y_amount: int, grid: Grid):
        for y in range(self.ptr_y - 1, self.ptr_y - y_amount - 1, -1):
            grid.add_point(self.ptr_x, y, self.index)

        self.ptr_y -= y_amount


    def follow_right(self, x_amount: int, grid: Grid):
        for x in range(self.ptr_x + 1, self.ptr_x + x_amount + 1):
            grid.add_point(x, self.ptr_y, self.index)

        self.ptr_x += x_amount


    def follow_left(self, x_amount: int, grid: Grid):
        for x in range(self.ptr_x - 1, self.ptr_x - x_amount - 1, -1):
            grid.add_point(x, self.ptr_y, self.index)

        self.ptr_x -= x_amount


    def run_instrs(self, grid: Grid):
        for instr in self.instrs:
            self.run_instr(instr, grid)


# Functions




# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    grid = Grid()
    wires= []

    for i, line in enumerate(lines):
        wires.append(Wire(i, line))
        wires[i].run_instrs(grid)

    return grid.get_closest_cross()

    return __name__


if __name__ == '__main__':
    pass