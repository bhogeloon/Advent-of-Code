"""
Year 2018, Day 5

Problem description: See https://adventofcode.com/2018/day/5

The following class is being used:
- Polymer: List class containing all characters of the string

Part 1: Go through the list. If the next character is the lower or uppercase reverse
then delete both current and next character from the list. Then go back one position 
and start the cycle again.
At first, I started all over again from the start of the string after a match. Then
it took 37 seconds to find the solution. After I changed the code, it took 0.16 seconds.


"""

# Imports
from pprint import pprint
import string


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Polymer(list[str]):
    '''Represents a polymer. It is a list class containing characters'''
    def __init__(self, line: str) -> None:
        self.extend(list(line))


    def process(self) -> None:
        '''Go through the polymer and remove all opposing parts with different
        polarisation'''
        # Start with index 0
        i = 0
        if Gv.test:
            self.print()

        # Keep processing until i = length - 1
        while i < len(self) - 1:
            # Consider current and next character
            if (
                    self[i].upper() == self[i+1].upper() and (
                        (
                            self[i] in string.ascii_lowercase and
                            self[i+1] in string.ascii_uppercase
                        ) or (
                            self[i] in string.ascii_uppercase and
                            self[i+1] in string.ascii_lowercase
                        )
                    )
                ):
                del self[i:i+2]

                if Gv.test:
                    self.print()

                # Then go back a few places to see if you have a new match
                i -= 2

                # If at the start, just start over
                if i < -1:
                    i = -1

            i += 1


    def print(self) -> None:
        '''Print the list as a string'''
        print(''.join(self))
    

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    polymer = Polymer(lines[0])
    polymer.process()

    return len(polymer)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
