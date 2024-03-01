"""
Year 2023, Day 6

Problem description: See https://adventofcode.com/2023/day/6

For part1:
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
        ht_min = (-self.dur + sqrt(self.dur**2 - 4*self.rec)) / -2
        ht_max = (-self.dur - sqrt(self.dur**2 - 4*self.rec)) / -2

        ht_min_int = int(ht_min) + 1

        if ht_max == int(ht_max):
            ht_max_int = int(ht_max) - 1
        else:
            ht_max_int = int(ht_max)

        return ht_max_int - ht_min_int + 1


class Races(list):
    def __init__(self, lines: list[str]) -> None:
        times_line = lines[0]
        times_str, rest = times_line.split(':')
        times = [ int(t) for t in rest.split()]

        records_line = lines[1]
        record_str, rest = records_line.split(':')
        records = [ int(t) for t in rest.split()]

        for i in range(len(times)):
            self.append(Race(times[i], records[i]))

    
    def get_wins(self) -> list:
        wins = []
        for race in self:
            wins.append(race.nr_of_wins())

        return wins


def get_single_race(lines: list[str]) -> Race:
        time_line = lines[0]
        time_str, rest = time_line.split(':')
        time = int(''.join(rest.split()))

        record_line = lines[1]
        record_str, rest = record_line.split(':')
        record = int(''.join(rest.split()))

        return Race(time, record)


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    races = Races(lines)
    wins = races.get_wins()

    result = 1

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