"""
Year 2020, Day 17, Part 2

Problem description: See https://adventofcode.com/2020/day/17

"""

# Imports
from pprint import pprint
from collections import deque

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Cube():
    def __init__(self, char: str) -> None:
        self.active = (char == '#')


class Cubes(deque[Cube]):
    def __init__(self, lines: list[str] = []) -> None:
        if len(lines) == 0:
            return

        z_values = deque()

        y_values = deque()

        for line in lines:
            x_values = deque()

            for char in line:
                x_values.append(Cube(char))

            y_values.append(x_values)

        z_values.append(y_values)
        self.append(z_values)

        self.expand()


    def print(self) -> None:
        for (w, z_values) in enumerate(self):
            for (z, y_values) in enumerate(z_values):
                print('z = {}, w = {}'.format(z,w))
                for x_values in y_values:
                    pline = ''
                    for x in x_values:
                        if x.active:
                            pline += '#'
                        else:
                            pline += '.'
                    print(pline)
                print()


    def expand(self) -> None:
        new_z_len = len(self[0]) + 2
        new_y_len = len(self[0][0]) + 2
        new_x_len = len(self[0][0][0]) + 2
        empty_x_values = deque( Cube('.') for i in range(new_x_len) )
        empty_y_values = deque( empty_x_values for i in range(new_y_len) )
        empty_z_values = deque( empty_y_values for i in range(new_z_len) )

        for z_values in self:

            for y_values in z_values:

                for x_values in y_values:
                    x_values.appendleft(Cube('.'))
                    x_values.append(Cube('.'))

                y_values.appendleft(empty_x_values)
                y_values.append(empty_x_values)

            z_values.appendleft(empty_y_values)
            z_values.append(empty_y_values)

        self.appendleft(empty_z_values)
        self.append(empty_z_values)


    def get_neighbors(self, x: int, y: int, z:int, w: int) -> list[Cube]:
        nb_cubes = []

        w_min = max(0, w-1)
        w_max = min(len(self)-1, w+1)

        for w_nb in range(w_min, w_max+1):
            z_min = max(0, z-1)
            z_max = min(len(self[w])-1, z+1)

            for z_nb in range(z_min, z_max+1):
                y_min = max(0, y-1)
                y_max = min(len(self[w][z])-1, y+1)
                
                for y_nb in range(y_min, y_max+1):
                    x_min = max(0, x-1)
                    x_max = min(len(self[w][z][y])-1, x+1)

                    for x_nb in range(x_min, x_max+1):
                        if x_nb == x and y_nb == y and z_nb ==z and w_nb == w:
                            continue
                        nb_cubes.append(self[w_nb][z_nb][y_nb][x_nb])

        return nb_cubes


    def cycle(self):
        new_cubes = Cubes()

        for (w, z_values) in enumerate(self):
            new_z_values = deque()

            for (z, y_values) in enumerate(z_values):
                new_y_values = deque()

                for (y, x_values) in enumerate(y_values):
                    new_x_values = deque()

                    for (x, cube) in enumerate(x_values):
                        active_nbs = 0
                        for nb in self.get_neighbors(x,y,z,w):
                            if nb.active:
                                active_nbs += 1

                        if cube.active:
                            if active_nbs == 2 or active_nbs == 3:
                                new_x_values.append(Cube('#'))
                            else:
                                new_x_values.append(Cube('.'))

                        else:
                            if active_nbs == 3:
                                new_x_values.append(Cube('#'))
                            else:
                                new_x_values.append(Cube('.'))

                    new_y_values.append(new_x_values)

                new_z_values.append(new_y_values)

            new_cubes.append(new_z_values)

        new_cubes.expand()

        return new_cubes


    def count(self) -> int:
        active_cubes = 0

        for z_values in self:
            for y_values in z_values:
                for x_values in y_values:
                    for cube in x_values:
                        if cube.active:
                            active_cubes += 1

        return active_cubes


# Functions



# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    cubes = Cubes(lines)

    for i in range(6):
        cubes = cubes.cycle()
 
    # cubes.print()

    return cubes.count()

    return __name__


if __name__ == '__main__':
    pass