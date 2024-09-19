"""
Year 2015, Day 6

Problem description: See https://adventofcode.com/2015/day/6

The following classes are used:
- Instruction: Contains a single instruction (one input line)
- Instructions: List container class of Instruction objects
- Lights: 2D grid object, containing the light states (True = on, False = off)

Part 1: Simply follow each instruction. It takes 6.5 seconds to complete them
all.

"""

# Imports
from pprint import pprint
import re
from grid import Grid2D


# Constants

GRID_SIZE = 1000

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Instruction():
    '''Instruction to turn on or off or toggle a light'''
    def __init__(self, line: str) -> None:
        m = re.fullmatch(r'(.*) (\d+),(\d+) through (\d+),(\d+)', line)
        self.action = m.group(1)
        xs = sorted([ int(m.group(2)), int(m.group(4))])
        ys = sorted([ int(m.group(3)), int(m.group(5))])
        self.x1 = xs[0]
        self.x2 = xs[1]
        self.y1 = ys[0]
        self.y2 = ys[1]

        if Gv.test:
            print(f'{self.action} {self.x1},{self.x2}'
                  f' through {self.y1},{self.y2}')



class Instructions(list[Instruction]):
    '''List container class of Instruction objects'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Instruction(line))


class Lights(Grid2D):
    '''Grid class containing the lights, which are booleans (True = on)
    and False=off'''
    def __init__(self) -> None:
        super().__init__(
            sizes=(GRID_SIZE,GRID_SIZE),
            default_value = False,
        )


    def nr_of_lights_on(self) -> int:
        '''Returns the number of lights being on'''
        result = 0

        for light in self.grid.flat:
            if light:
                result += 1

        return result
    

    def process_instructions(self, instrs: Instructions) -> None:
        '''Process all the instructions'''
        for instr in instrs:
            self.process_instruction(instr)


    def process_instruction(self, instr: Instruction) -> None:
        '''Process a single instruction'''
        for y in range(instr.y1,instr.y2+1):
            for x in range(instr.x1,instr.x2+1):
                if instr.action == 'turn on':
                    self.grid[x,y] = True
                elif instr.action == 'turn off':
                    self.grid[x,y] = False
                elif instr.action == 'toggle':
                    self.grid[x,y] = not(self.grid[x,y])
                else:
                    raise RuntimeError(f'Unkown action {instr.action}')


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    lights = Lights()
    instrs = Instructions(lines)
    lights.process_instructions(instrs)

    return lights.nr_of_lights_on()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
