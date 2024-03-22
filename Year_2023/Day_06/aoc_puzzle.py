"""
Year 2023, Day 6

Problem description: See https://adventofcode.com/2023/day/6

This puzzle could be done on simple calculator once you have the
formula right, using the abc formula.

T = total time
R = record distance
Formula for calculating distance:
s(ht) = v_start * (T - ht)
v_start is equal to ht, so:
s(ht) = -ht^2 + T*ht

So to calculate min and max ht, we have to solve:
-ht^2 + T*ht - R = 0
According to the abc formula:
ht_min = (-T + SQRT(T^2 - 4*R))/-2
ht_max = (-T - SQRT(T^2 - 4*R))/-2

But Ok, let's do it in Python :-)
So I create the following classes:
- Race: Each race has a max duration and a given record.
- Races: container class (list)

So, for part 1, calculate the formula to get the min and max value and
see which integer values are within that range for each race.

For part 2, glue all numbers together and then do the formula for a
single race.

"""

# Imports
from pprint import pprint
from math import sqrt

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''



# Classes
class Race():
    ''''''

    def __init__(self, time: int, record: int) -> None:
        self.dur = time
        self.rec = record


    def nr_of_wins(self) -> int:
        '''Calculate the number of integer values that causes the
        record to break, using the formula on top'''
        ht_min = (-self.dur + sqrt(self.dur**2 - 4*self.rec)) / -2
        ht_max = (-self.dur - sqrt(self.dur**2 - 4*self.rec)) / -2

        # The minimum integer is the first integer which is bigger
        # (as equal to the record is not breaking it)
        ht_min_int = int(ht_min) + 1

        # The maximum is last integer which is smaller.
        if ht_max == int(ht_max):
            ht_max_int = int(ht_max) - 1
        else:
            ht_max_int = int(ht_max)

        # Then calculate the amount of integers in the range
        return ht_max_int - ht_min_int + 1


class Races(list):
    def __init__(self, lines: list[str]) -> None:
        # Extract the time values
        times_line = lines[0]
        times_str, rest = times_line.split(':')
        times = [ int(t) for t in rest.split()]

        # Extract the records values
        records_line = lines[1]
        record_str, rest = records_line.split(':')
        records = [ int(t) for t in rest.split()]

        # Then create the Race objects
        for i in range(len(times)):
            self.append(Race(times[i], records[i]))

    
    def get_wins(self) -> list:
        '''Get the wins of each race and put them in a list'''
        wins = []
        for race in self:
            wins.append(race.nr_of_wins())

        return wins


def get_single_race(lines: list[str]) -> Race:
        '''Get the data for a single race'''
        # Extract the time by glueing the numbers together
        time_line = lines[0]
        time_str, rest = time_line.split(':')
        time = int(''.join(rest.split()))

        # Do the same for record
        record_line = lines[1]
        record_str, rest = record_line.split(':')
        record = int(''.join(rest.split()))

        # Then use the same formula
        return Race(time, record)


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    races = Races(lines)
    wins = races.get_wins()

    result = 1

    # Calculate the product of all wins
    for win in wins:
        result *= win

    return result

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    race = get_single_race(lines)
    
    return race.nr_of_wins()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass