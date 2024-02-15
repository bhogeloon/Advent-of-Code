"""
Year 2019, Day 1, Part 1

Problem description: See https://adventofcode.com/2019/day/1

"""

# Imports
from pprint import pprint

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Spacecraft():
    def __init__(self, line:str) -> None:
        self.mass = int(line)


    def get_fuel(self) -> None:
        self.fuel = (self.mass // 3) - 2


class Spacecrafts(list[Spacecraft]):
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Spacecraft(line))


    def get_fuel(self):
        for spacecraft in self:
            spacecraft.get_fuel()

    def get_sum_of_fuel(self) -> int:
        sum_of_fuel = 0
        for spacecraft in self:
            sum_of_fuel += spacecraft.fuel

        return sum_of_fuel


# Functions




# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    spacecrafts = Spacecrafts(lines)

    spacecrafts.get_fuel()

    return spacecrafts.get_sum_of_fuel()

    return __name__


if __name__ == '__main__':
    pass