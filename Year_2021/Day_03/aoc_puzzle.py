"""
Year 2021, Day 3

Problem description: See https://adventofcode.com/2021/day/3

I created a single class DiagReport, which contains a numpy grid containing
all binary digits.

For part 1, look at each x bit and determine the most common. Glue them together to get
the number. Do the same for the least common bits and multiply them.

For part 2: For both the oxygen and co2 level, create a set of line numbers and then
looking at the x bits one by one, remove all line numbers from the set that do not
match the criteria. Keep doing this until only one is left.

"""

# Imports
from pprint import pprint
from collections import Counter
# Use function in aoc_lib
from grid import Grid2D


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class DiagReport(Grid2D):
    '''Diagnostic report, which contains all binary numbers in a numpy grid'''

    def __init__(self, lines: list[str]) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)

        super().__init__(
            sizes=(self.x_size,self.y_size),
            input_lines=lines,
        )

        self.bins = self.grid


    def get_power_consumption(self) -> int:
        '''Calculate gamma and epsilon rate and return product'''
        gamma_str = ''
        epsilon_str = ''

        for x in range(self.x_size):
            c = Counter(self.bins[x,:])
            zeros = c['0']
            ones = c['1']

            if zeros > ones:
                gamma_str += '0'
                epsilon_str += '1'
            elif ones > zeros:
                gamma_str += '1'
                epsilon_str += '0'
            else:
                raise RuntimeError("Equal values for 0 and 1 in pos {}.".format(x))

            gamma_value = int(gamma_str, base=2)
            epsilon_value = int(epsilon_str, base=2)

        return gamma_value * epsilon_value


    def get_oxygen(self) -> int:
        '''Get the oxygen level'''

        # This set contains all y values still valid

        valid_bins = set([v for v in range(self.y_size)])

        # Start at column 0
        x = 0

        while len(valid_bins) > 1:
            # First determine most common bit
            zeros = 0
            ones = 0

            for y in range(self.y_size):
                if y not in valid_bins:
                    continue
                if self.bins[x,y] == '0':
                    zeros += 1
                elif self.bins[x,y] == '1':
                    ones += 1

            if zeros > ones:
                oxygen_bit = '0'
            else:
                oxygen_bit = '1'

            # Then go through the list and remove all invalid bins
            for y in range(self.y_size):
                if self.bins[x,y] != oxygen_bit:
                    valid_bins -= {y}

            # Increase x
            x += 1

        oxygen_bin_str = ''.join(self.bins[:,valid_bins.pop()])

        return int(oxygen_bin_str, base=2)


    def get_co2_scrubber(self) -> int:
        '''Get the co2 scrubber level'''

        # This set contains all y values still valid

        valid_bins = set([v for v in range(self.y_size)])

        # Start at column 0
        x = 0

        while len(valid_bins) > 1:
            # First determine most common bit
            zeros = 0
            ones = 0

            for y in range(self.y_size):
                if y not in valid_bins:
                    continue
                if self.bins[x,y] == '0':
                    zeros += 1
                elif self.bins[x,y] == '1':
                    ones += 1

            if zeros > ones:
                co2_bit = '1'
            else:
                co2_bit = '0'

            # Then go through the list and remove all invalid bins
            for y in range(self.y_size):
                if self.bins[x,y] != co2_bit:
                    valid_bins -= {y}

            # Increase x
            x += 1

        co2_bin_str = ''.join(self.bins[:,valid_bins.pop()])

        return int(co2_bin_str, base=2)


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    diagrep = DiagReport(lines)

    return diagrep.get_power_consumption()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    diagrep = DiagReport(lines)

    return diagrep.get_oxygen() * diagrep.get_co2_scrubber()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
