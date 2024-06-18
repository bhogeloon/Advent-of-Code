"""
Module for Grid class and subclasses.
These classes define a numpy multidimensional grid.
Client classes can inherit from the main class or subclasses.
"""

# Imports
from test_lib import TestLib
import numpy as np


class Grid():
    '''Main Grid class to inherit from'''

    def __init__(self, **kwargs) -> None:
        '''
        This class has the following argument:
            - sizes: a list or tuple that contains the sizes per dimension. The length of this
                list/tuple also defines the dimensions that are created for the grid
            - default_value: The default value with which the cells are initially filled (or
                None if not specified.)
        '''
        self.sizes = kwargs['sizes']
        default_value = kwargs.get('default_value', None)

        self.grid = np.full(self.sizes, default_value)


class Grid1D(Grid):
    '''Grid class for one dimensional grids (so a simple array really)'''

    def __init__(self, **kwargs) -> None:
        '''
        Class for a one-dimensional grid. It requires the following attributes:
            - sizes: int or list or tuple containing only one value.
            - default_value: The default value with which the cells are initially filled (or
                None if not specified.)
            - cell_class: The class in which each cell is created in. The class must
                support a default initialisation (without any arguments).
                If this argument is not specified, all cells remain with content None.
        '''
        super().__init__(**kwargs)

        if type(self.sizes) != int:
            if len(self.sizes) != 1:
                raise RuntimeError("Not a One Dimensional grid.")
            else:
                self.sizes = self.sizes[0]

        cell_class = kwargs.get('cell_class', None)

        if cell_class != None:
            for x in range(self.sizes):
                self.grid[x] = cell_class()


class Grid2D(Grid):
    '''Grid class for two dimensional grids'''

    def __init__(self, **kwargs) -> None:
        '''
        Class for a two-dimensional grid. It requires the following attributes:
            - sizes: list or tuple containing exactly two values.
            - cell_class: The class in which each cell is created in. The class must
                support a default initialisation (without any arguments).
                If this argument is not specified, all cells remain with content None.
        '''
        super().__init__(**kwargs)

        if len(self.sizes) != 2:
            raise RuntimeError("Not a Two Dimensional grid.")

        cell_class = kwargs.get('cell_class', None)

        if cell_class != None:
            for y in range(self.sizes[1]):
                for x in range(self.sizes[0]):
                    self.grid[x,y] = cell_class()


class Grid3D(Grid):
    '''Grid class for 3 dimensional grids'''

    def __init__(self, **kwargs) -> None:
        '''
        Class for a 3-dimensional grid. It requires the following attributes:
            - sizes: list or tuple containing exactly 3 values.
            - cell_class: The class in which each cell is created in. The class must
                support a default initialisation (without any arguments).
                If this argument is not specified, all cells remain with content None.
        '''
        super().__init__(**kwargs)

        if len(self.sizes) != 3:
            raise RuntimeError("Not a 3 Dimensional grid.")

        cell_class = kwargs.get('cell_class', None)

        if cell_class != None:
            for z in range(self.sizes[2]):
                for y in range(self.sizes[1]):
                    for x in range(self.sizes[0]):
                        self.grid[x,y] = cell_class()


if __name__ == '__main__':
    # grid = Grid3D(sizes=[3,2,2], cell_class = TestLib)
    grid = Grid1D(sizes=3, default_value = 69)

    print(grid.__class__)

    for cell in grid.grid.flat:
        print(type(cell))
