"""
Year 2019, Day 1

Problem description: See https://adventofcode.com/2019/day/1

I created a Spacecraft class, which has a mass and an amount of fuel,
which can be calculated from the mass.
Also there is Spacecraft container class, which collects all fuels

For part 1, just calculate the fuel for each Spacecraft and add them up.

For part 2, an extended fuel calculation has been added. This keeps on
adding the fuel to them mass, until the additional fuel is zero.

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

class Spacecraft():
    '''Spacecraft has a mass and an amount of fuel'''
    def __init__(self, line:str) -> None:
        self.mass = int(line)


    def get_fuel(self) -> None:
        '''Calculate fuel'''
        self.fuel = (self.mass // 3) - 2


    def get_fuel_extended(self) -> None:
        '''Calculate fuel as in part 2'''
        self.fuel = (self.mass // 3) - 2

        # Keep track of the fuel, to see if it changes
        last_fuel = self.fuel

        while True:
            # Calculate the extra fuel required
            extra_fuel = (last_fuel // 3) - 2

            # Add the extra fuel if there is any
            if extra_fuel > 0:
                self.fuel += extra_fuel
                last_fuel = extra_fuel
            # And otherwise quit
            else:
                break



class Spacecrafts(list[Spacecraft]):
    '''Container class of Spacecraft ojects'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Spacecraft(line))


    def get_fuel(self):
        '''Calculate fuel for all Spacecrafts'''
        for spacecraft in self:
            spacecraft.get_fuel()


    def get_fuel_extended(self):
        '''Extended fuel calculation for part 2'''
        for spacecraft in self:
            spacecraft.get_fuel_extended()


    def get_sum_of_fuel(self) -> int:
        '''Get the sum of all fuels'''
        sum_of_fuel = 0
        for spacecraft in self:
            sum_of_fuel += spacecraft.fuel

        return sum_of_fuel


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    spacecrafts = Spacecrafts(lines)

    spacecrafts.get_fuel()

    return spacecrafts.get_sum_of_fuel()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    spacecrafts = Spacecrafts(lines)

    spacecrafts.get_fuel_extended()

    return spacecrafts.get_sum_of_fuel()


    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
