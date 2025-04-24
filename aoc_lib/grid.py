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
                self.grid[x].x = x


class Grid2D(Grid):
    '''Grid class for two dimensional grids'''

    def __init__(self, **kwargs) -> None:
        '''
        Class for a two-dimensional grid. It requires the following attributes:
            - sizes: list or tuple containing exactly two values.
            - default_value: The default value with which the cells are 
                initially filled (or None if not specified.)
            - cell_class: The class in which each cell is created in. The class
                must support a default initialisation (without any arguments).
                If this argument is not specified, all cells remain with content
                None.
            - func: Function to be used to fill the initial values of the cels.
                This preceedes the cell_class argument. func needs to support
                non-positional arguments only. All arguments needed need to 
                be provided as non-positional arguments to this function (they 
                will be transferred to func using **kwargs), except for x and y,
                which will be provided by this function.
            - input_lines: List of strings (generally the puzzle input). When
                this is specified, all cells are allocated the value of
                input_lines[y][x]. When int_value=True is provided, the int 
                value is used, rather than the str value. When cell_class is 
                also specified, the cells are initialised with 
                cell_class(input_lines[y][x]).
        '''
        super().__init__(**kwargs)

        if len(self.sizes) != 2:
            raise RuntimeError("Not a Two Dimensional grid.")

        cell_class = kwargs.get('cell_class', None)
        func = kwargs.get('func', None)
        input_lines = kwargs.get('input_lines', None)
        int_value = kwargs.get('int_value', False)

        if func != None:
            # Remove all arguments not relevant to the function call
            kwargs.pop('sizes', None)
            kwargs.pop('cell_class', None)
            kwargs.pop('default_value', None)
            kwargs.pop('input_lines', None)
            kwargs.pop('input_value', None)
            self.func_all_cells(**kwargs)
        elif input_lines != None:
            self.use_input_lines(
                input_lines=input_lines,
                cell_class=cell_class,
                int_value=int_value,
            )
        elif cell_class != None:
            for y in range(self.sizes[1]):
                for x in range(self.sizes[0]):
                    self.grid[x,y] = cell_class()
                    self.grid[x,y].x = x
                    self.grid[x,y].y = y


    def use_input_lines(self, input_lines, cell_class, int_value=False) -> None:
        '''Use input lines to initialise cells'''

        def _no_cell_no_int(x=None,y=None,lines=input_lines):
            return lines[y][x]
        
        def _no_cell_int(x=None,y=None,lines=input_lines):
            return int(lines[y][x])

        def _cell_no_int(x=None,y=None,lines=input_lines):
            obj = cell_class(lines[y][x])
            obj.x = x
            obj.y = y
            return obj

        def _cell_int(x=None,y=None,lines=input_lines):
            obj = cell_class(int(lines[y][x]))
            obj.x = x
            obj.y = y
            return obj

        if cell_class is None:
            if int_value:
                func=_no_cell_int
            else:
                func=_no_cell_no_int
        else:
            if int_value:
                func=_cell_int
            else:
                func=_cell_no_int

        self.func_all_cells(func=func)


    def func_all_cells(self, func=None, **kwargs):
        '''
        This function will execute the function func on all cells. func needs to support
        non-positional arguments only. All arguments needed need to be provided as
        non-positional arguments to this function (they will be transferred to func using
        **kwargs), except for x and y, which will be provided by this function
        '''

        if func != None:
            for y in range(self.sizes[1]):
                for x in range(self.sizes[0]):
                    self.grid[x,y] = func(x=x, y=y, **kwargs)
                    self.grid[x,y].x = x
                    self.grid[x,y].y = y


    def print(self, seperator = '') -> None:
        '''Print the values of all cells. Each cell in a row is seperated by
        the seporator (default is '')'''
        for y in range(self.sizes[1]):
            line = ''

            for x in range(self.sizes[0]):
                line += str(self.grid[x,y]) + seperator

            print(line)

        print()


    def __str__(self) -> str:
        '''String representation'''
        result = '\n'

        for y in range(self.sizes[1]):
            for x in range(self.sizes[0]):
                result += str(self.grid[x,y])
            result += '\n'

        return result


class Grid3D(Grid):
    '''Grid class for 3 dimensional grids'''

    def __init__(self, **kwargs) -> None:
        '''
        Class for a 3-dimensional grid. It requires the following attributes:
            - sizes: list or tuple containing exactly 3 values.
            - default_value: The default value with which the cells are initially filled (or
                None if not specified.)
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
                        self.grid[x,y,z] = cell_class()
                        self.grid[x,y,z].x = x
                        self.grid[x,y,z].y = y
                        self.grid[x,y,z].z = z


if __name__ == '__main__':
    # grid = Grid3D(sizes=[3,2,2], cell_class = TestLib)
    # grid = Grid1D(sizes=3, default_value = 69)
    grid = Grid2D(
        sizes=[3,3],
        func=lambda x=None,y=None : x+y,
    )
    # grid.func_all_cells(func=lambda x=None,y=None : x+y)

    print(grid.__class__)

    for cell in grid.grid.flat:
        print(cell)
