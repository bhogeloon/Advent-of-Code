"""
Year 2021, Day 6

Problem description: See https://adventofcode.com/2021/day/6

The following classes are used:
- Fish: Represents a fish with days_left attribute (days left to reproduce)
- Fishes: List container class of Fish objects

Part 1: For every day, decrease days left of every fish. But if days_left is
already 0:
- Reset value to 6
- Create new Fish with days_left set to 8

Part 2: It looks easy: just change the number of days to 256. However this
proves to take a very long time.
So to improve: we just calculate the scenario for single fish and then use
this data on each individual fish.
Still: 256 days on a single fish also takes a very long time.
So, to further improve, we only calculate the scenario for 128 days and
then calculate the scenario of the last few days by looking at each individual
fish in the 128 days calculation.
This way, it took less than half a second to get the answer, so I stopped there.
Theoratically though, you could repeat this scenario for 64 and 32, and 16
days, so you really only need the scenario for 16 days (8 days is too short as 
you have to take into account that it can take 9 days before an offspring is
created). This way you could even further improve the run time.
"""

# Imports
from pprint import pprint


# Constants

TOTAL_DAYS = 80
DAYS_TO_REPRODUCE = 7
EXTRA_DAYS_NEW_FISH = 2

LONG_PERIOD = 256
HALF_TIME = LONG_PERIOD // 2


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Fish():
    '''Represents a fish with an attribute days_left (days left before it reproduces).'''
    def __init__(self, days_left: int) -> None:
        self.days_left = days_left


    def ready(self) -> bool:
        '''Returns True if Fish is ready to reproduce'''
        if self.days_left == 0:
            self.days_left = DAYS_TO_REPRODUCE - 1
            return True
        else:
            self.days_left -= 1
            return False


class Fishes(list[Fish]):
    '''List container class of Fish objects'''
    def __init__(self, line: str) -> None:
        nr_days = line.split(',')

        for nr_day in nr_days:
            self.append(Fish(int(nr_day)))


    def pass_day(self):
        '''Progress one day'''
        for i in range(len(self)):
            # If fish is ready to reproduce
            if self[i].ready():
                self.append(Fish(DAYS_TO_REPRODUCE + EXTRA_DAYS_NEW_FISH - 1))


# Functions

def get_nr_fishes_long_period(real_fishes: Fishes) -> int:
    '''Calulate the nr of fishes for a longer period'''
    # A 'bogus' input to create a scenario for a single fish
    bogus_fishes = Fishes('0')

    # A list contiaining the nr of offsprings after a certain amount of days
    nr_of_offspring = []

    # Fill the nr_of_offspring list for the bogus fish for 128 days
    for day in range(HALF_TIME):
        nr_of_fishes = len(bogus_fishes)

        if Gv.test:
            print("at te start of day {} there are {} fishes".format(day, nr_of_fishes))

        bogus_fishes.pass_day()

        nr_of_offspring.append(len(bogus_fishes))

    # Now calculate for the next xxx days
    # Then go through the current list and calculate the offspring based on the
    # 128 days calculation, without creating the actual list

    # This is the totals for last few days
    totals = {}
    for day in range(LONG_PERIOD - DAYS_TO_REPRODUCE, LONG_PERIOD):
        totals[day] = 0
        for fish in bogus_fishes:
            # The total number of offspring depends on the day in which it has
            # The first offspring. On that day, the total number can be retrieved from
            # the 128 day list.
            totals[day] += nr_of_offspring[day - HALF_TIME - fish.days_left]

        if Gv.test:
            print("Total after {} days: {}".format(day + 1, totals[day]))

    # Now calculate the total amount in the 'real_fishes' list, depending on the current
    # state
    total = 0
    for fish in real_fishes:
        total += totals[LONG_PERIOD - 1 - fish.days_left]

    return total


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    fishes = Fishes(lines[0])

    for day in range(TOTAL_DAYS):
        fishes.pass_day()

    return len(fishes)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    fishes = Fishes(lines[0])

    return get_nr_fishes_long_period(fishes)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
