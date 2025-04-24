"""
Year 2019, Day 8

Problem description: See https://adventofcode.com/2019/day/8

The following classes are used:
- Layer: A grid class containing all the digits
- Image: List container class of Layer objects

Part 1: Read all the data and fill each image sequentially. Then create a
counter object for the image data. Find the one with the least amount of zeroes
and report the amount of 1's multiplied by the amount of 2's.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from grid import Grid2D
from collections import deque, Counter


# Constants

IMG_SIZE = (25,6)
IMG_SIZE_TEST = (3,2)


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

class Layer(Grid2D):
    '''Layer of an image'''
    def __init__(self, layer_data: deque, layer_size: tuple[int]):
        super().__init__(sizes = layer_size)

        for y in range(self.sizes[1]):
            for x in range(self.sizes[0]):
                self.grid[x,y] = int(layer_data.popleft())

        # Create Counter object
        self.cnt = Counter(self.grid.flat)


    def get_1_times_2(self) -> int:
        '''Return the number of 1 digits multiplied by the number of 2
        digits'''
        # If no 1 or no 2 digits, result will always be 0
        if 1 not in self.cnt.keys() or 2 not in self.cnt.keys():
            return 0
        
        return self.cnt[1] * self.cnt[2]


class Image(list[Layer]):
    '''List class containing several Layer objects'''
    def __init__(self, img_data: deque):
        if Gv.test:
            layer_size = IMG_SIZE_TEST
        else:
            layer_size = IMG_SIZE

        while len(img_data) > 0:
            # Pop all data
            layer_data = deque()
            for i in range(layer_size[0]*layer_size[1]):
                layer_data.append(img_data.popleft())

            self.append(Layer(layer_data, layer_size))


    def get_lowest_0_layer(self) -> Layer:
        '''Return the Layer with the fewest 0 digits'''
        # Start with large value for zeroes
        min_zeroes = 999999999

        for layer in self:
            Gv.log.debug(f"zeroes: {layer.cnt[0]}")
            if 0 not in layer.cnt.keys():
                min_zeroes = 0
                zero_layer = layer
            elif layer.cnt[0] < min_zeroes:
                min_zeroes = layer.cnt[0]
                zero_layer = layer
                Gv.log.debug(f"Setting min_zeroes to {min_zeroes}")
            elif layer.cnt[0] == min_zeroes:
                Gv.log("Found duplicate:")
                Gv.log(str(self))
                raise Exception("Found duplicate")

        return zero_layer
    

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    img_data = deque(lines[0])
    img = Image(img_data)

    for layer in img:
        Gv.log.debug(str(layer))

    zero_layer = img.get_lowest_0_layer()

    Gv.log.debug(f"Selected layer with {zero_layer.cnt[0]} zeroes"
                 f", {zero_layer.cnt[1]} 1's and {zero_layer.cnt[2]} 2's")
    Gv.log.debug(str(zero_layer))

    return zero_layer.get_1_times_2()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
