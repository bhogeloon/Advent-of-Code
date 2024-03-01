"""
Year 2022, Day 1, Part 1

Problem description: See https://adventofcode.com/2022/day/1

<Include solution description>

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

class Elf():
    '''An elf can contain a certain amount of food'''
    def __init__(self) -> None:
        '''foods contains the list of food items'''
        self.foods = []


    def get_cals(self) -> int:
        '''Calculate total amount of calories'''
        tot_cal = 0

        for food in self.foods:
            tot_cal += food.cal

        return tot_cal


class Food():
    '''A Food item can contain a certain amount of calories'''
    def __init__(self, cal_str:str) -> None:
        self.cal = int(cal_str)


# Functions
def process_input(lines: list[str]) -> list:
    '''Returns a list of Elfs'''

    all_elfs = []
    elf = Elf()

    for line in lines:
        # If new line
        if line == '':
            if len(elf.foods) > 0:
                all_elfs.append(elf)
                elf = Elf()
        else:
            elf.foods.append(Food(line))

    if len(elf.foods) > 0:
        all_elfs.append(elf)

    return all_elfs


def get_fattest_elf(all_elfs: list[Elf]) -> int:
    '''Return the largest amount of calories on one Elf'''

    max_cal = 0

    for elf in all_elfs:
        cals = elf.get_cals()
        #pprint(cals)

        if cals > max_cal:
            max_cal = cals

    return max_cal


def get_fattest3_elfs(all_elfs: list[Elf]) -> int:
    '''Return total calories of the three fattest elfs'''

    max_cals = [0, 0, 0]

    for elf in all_elfs:
        cals = elf.get_cals()
        #pprint(cals)

        if cals > min(max_cals):
            max_cals[max_cals.index(min(max_cals))] = cals

    return sum(max_cals)


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    all_elfs = process_input(lines)

    return get_fattest_elf(all_elfs)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    all_elfs = process_input(lines)

    return get_fattest3_elfs(all_elfs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
