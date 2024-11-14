"""
Year 2019, Day 7

Problem description: See https://adventofcode.com/2019/day/7

The following classes are used:
- Intcode: Same class as in day 5, with one small modification: the input
    argument is now not a single number but a deque of numbers.
- PhaseSequences: At initialisation, it creates all possible lists of Phase
    Sequences, using numbers 0 - 4.

Part 1: Loop through all possible PhaseSequences and register the output
after running the code for each amplifier. Then return the maximum.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from collections import deque


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class PhaseSequences(list[list[int]]):
    '''This class contains all Phase sequences possible. It is a list of lists
    of ints'''
    def __init__(self) -> None:
        used_nrs = set()
        all_nrs = {0,1,2,3,4}

        for a in range(5):
            used_nrs.add(a)
            for b in range(5):
                if b in used_nrs:
                    continue
                used_nrs.add(b)
                for c in range(5):
                    if c in used_nrs:
                        continue
                    used_nrs.add(c)
                    for d in range(5):
                        if d in used_nrs:
                            continue
                        used_nrs.add(d)
                        # e is the number not in the set
                        leftover = used_nrs ^ all_nrs
                        e = leftover.pop()
                        self.append([a,b,c,d,e])
                        used_nrs.remove(d)
                    used_nrs.remove(c)
                used_nrs.remove(b)
            used_nrs.remove(a)


    def get_max_thrust(self, line: str) -> int:
        '''Get the maximum number of thrust output'''
        thrust_outputs = []

        for phase_seq in self:
            thrust = 0

            # For each phase
            for phase in phase_seq:
                intcode = Intcode(line, deque([phase,thrust]))
                thrust = intcode.run_program()

            thrust_outputs.append(thrust)

        return max(thrust_outputs)


class Intcode():
    '''Intcode class from day 5. Uses the same logic. However the input
    is now mandatory and is a deque'''
    def __init__(self, line:str, input: deque) -> None:
        self.codes = [ int(nr) for nr in line.split(',') ]
        # Indicates where the program is
        self.ptr = 0

        self.input = input

        # Create output list
        self.output = []


    def fix(self, val1 = 12, val2 = 2) -> None:
        '''Fix the initial values'''
        self.codes[1] = val1
        self.codes[2] = val2


    def run_program(self) -> int:
        '''Run through the program and return diagnostic code'''
        while True:
            # If we detect value 99, end program
            if self.codes[self.ptr] == 99:
                # Return last code on the output queue
                return self.output[-1]

            # Determine opcode and modes
            opcode = self.codes[self.ptr] % 100
            modes = self.codes[self.ptr] // 100

            if opcode == 3:
                self.get_input()
            elif opcode == 4:
                self.store_output(modes)
            elif opcode in (1,2,7,8):
                self.operator(opcode, modes)
            elif opcode in (5,6):
                self.jump(opcode, modes)
            else:
                raise RuntimeError(f'Unkown opcode {opcode}')


    def operator(self, opcode: int, modes: int) -> None:
            '''Perform add or multiply operator'''
            # Determine mode per argument
            mode1 = modes % 10
            mode2 = (modes // 10) % 10

            # Get the arguments and the store location
            arg1 = self.get_value_by_mode(mode1, self.ptr+1)
            arg2 = self.get_value_by_mode(mode2, self.ptr+2)
            store_loc = self.codes[self.ptr+3]

            # If opcode = 1, add the args
            if opcode == 1:
                self.codes[store_loc] = arg1 + arg2
 
            # If opcode = 2, multiply the args
            elif opcode == 2:
                self.codes[store_loc] = arg1 * arg2

            # If opcode = 7
            elif opcode == 7:
                if arg1 < arg2:
                    self.codes[store_loc] = 1
                else:
                    self.codes[store_loc] = 0

            # If opcode = 8
            elif opcode == 8:
                if arg1 == arg2:
                    self.codes[store_loc] = 1
                else:
                    self.codes[store_loc] = 0

            else:
                raise RuntimeError(f"Unknown operator {opcode}.")

            # Jump ahead 4 positions
            self.ptr += 4


    def less_than(self, modes: int) -> None:
        '''Store 1 if less than, otherwise 0'''


    def equal_to(self, modes: int) -> None:
        '''Store 1 if equal, otherwise 0'''


    def get_input(self) -> None:
        '''Get input and store information'''
        store_loc = self.codes[self.ptr+1]
        self.codes[store_loc] = self.input.popleft()
        self.ptr += 2


    def store_output(self, modes: int) -> None:
        '''Store output in the output queue'''
        mode = modes % 10
        output = self.get_value_by_mode(mode, self.ptr+1)
        self.output.append(output)
        self.ptr += 2


    def jump(self, opcode: int, modes: int) -> None:
        '''Change the ptr'''
        # First check if you need to do something at all by checking first
        # parameter
        mode1 = modes % 10
        action = self.get_value_by_mode(mode1, self.ptr+1)

        # If no action required
        if (
                (opcode == 5 and action == 0) or
                (opcode == 6 and action != 0)
            ):
            self.ptr += 3
            return
        
        # Now determine the new ptr position
        mode2 = (modes // 10) % 10
        self.ptr = self.get_value_by_mode(mode2, self.ptr+2)


    def get_value_by_mode(self, mode: int, index: int) -> int:
        '''Return the positional or immediate value, depending on the mode'''
        if mode == 0:
            return self.codes[self.codes[index]]
        else:
            return self.codes[index]


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    phase_seqs = PhaseSequences()

    return phase_seqs.get_max_thrust(lines[0])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
