"""
Year 2021, Day 7

Problem description: See https://adventofcode.com/2021/day/7

The following classes are used:
- Crabs: A list class containing all starting positions of each crab
- Positions: A list class containing all possible ending positions. The value
    contains the amount of fuel required for that.

Part 1: Calculate the Fuel required for each position and report the minimum
(Takes 1.5 seconds)

Part 2: First make a list of all the fuel consumption by the amount of steps
(so that we don't have to calculate that for each crab for each position).
Then go through the same function as in part 1, adding the amount in the list
along the way.

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

class Crabs(list[int]):
    '''List container class of crab submarine. The integer value 
    represents the starting position'''
    def __init__(self, line:str) -> None:
        self.extend([int(p) for p in line.split(',')])


class Positions(list[int]):
    '''List class of all possible positions. The values indicates the fuel
    necessarry to align all crabs to that position'''
    def __init__(self, crabs: Crabs) -> None:
        # Create list of possible postions
        self.extend([0 for n in range(max(crabs)+1)])
        self.crabs = crabs


    def calculate_fuel(self) -> None:
        '''Fill the list with the fuel that is required to align the crabs
        to this position'''
        for i in range(len(self)):
            for crab in self.crabs:
                self[i] += abs(crab-i)


    def calculate_fuel_increasing(self) -> None:
        '''Fill the list with the fuel that is required to align the crabs
        to this position using the increasing fuel consumption in part 2'''
        # Create a fuel consumption list for each amount of steps
        fuel_cons = {}
        fuel = 0
        for i in range(len(self)+1):
            fuel += i
            fuel_cons[i] = fuel

        if Gv.test:
            print(fuel_cons)
            print(self)
            print(self.crabs)
            
        for i in range(len(self)):
            for crab in self.crabs:
                steps = abs(crab-i)
                self[i] += fuel_cons[steps]
        if Gv.test:
            print(self)



# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    crabs = Crabs(lines[0])
    positions = Positions(crabs)
    positions.calculate_fuel()

    return min(positions)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    crabs = Crabs(lines[0])
    positions = Positions(crabs)
    positions.calculate_fuel_increasing()

    return min(positions)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
