"""
Year 2019, Day 7

Problem description: See https://adventofcode.com/2019/day/7

The following classes are used:
- Intcode: Same class as in day 5, with a couple of small modifications: 
    - The input argument is now not a single number but a deque of numbers.
    - Also the output queue is a deque and the return value of the 
        run_program method is now the complete output queue instead of the
        latest value. This is a requirement of part 2.
- PhaseSequences: At initialisation, it creates all possible lists of Phase
    Sequences, using numbers 0 - 4.

Part 1: Loop through all possible PhaseSequences and register the output
after running the code for each amplifier. Then return the maximum.

Part 2:
The main challenge of this puzzle was to interpret the puzzle text. 
It was clear to me that I had to keep a seperate Intcode instance for each
amplifier, but the following points puzzled me:
- When do we pass control over to the next Amp?
- When do we break the loop? When all processes have halted or just Amp E?
- What do we pass on when the program halts?
- What happens if we pass on control to a program which is already halted?

In my first attempt I decided to pass on control immediately after an output
was detected, which was then the input for the next Amp (along with the Phase 
setting in the first run). When the program halts, just pass on the latest 
value in the output queue. I guess there it went wrong as it could be that that
value was already passed earlier.

Then I started to dig around a bit and found an alternative solution: Keep
running every process until you are out of input. I guess that more simulates
a multithreading approach. As soon as you're out of input or the program halts,
just pass on the entire output queue as input queue to the next process.
When the program has already been halted, just pass on the input queue as is 
(which is effectively the same as skipping the process entirely).
The feedback loop ends as soon as Amp E halts. This produced the right result.

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
    def __init__(self, seq_range:list[int] | None = None) -> None:
        if seq_range == None:
            self.seq_range = [0,1,2,3,4]
        else:
            self.seq_range = seq_range

        used_nrs = set()
        all_nrs = set(self.seq_range)

        for a in self.seq_range:
            used_nrs.add(a)
            for b in self.seq_range:
                if b in used_nrs:
                    continue
                used_nrs.add(b)
                for c in self.seq_range:
                    if c in used_nrs:
                        continue
                    used_nrs.add(c)
                    for d in self.seq_range:
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
                thrust = intcode.run_program()[-1]

            thrust_outputs.append(thrust)

        return max(thrust_outputs)
    

    def get_max_thrust_w_feedback(self, line: str) -> int:
        '''Get the maximum thrust level using the feedback loop'''
        thrust_outputs = []

        for phase_seq in self:
            # The amplifier processes
            amps = []

            # The I/O queue
            queue = deque([0])

            # For each phase, first start processes
            for phase in phase_seq:
                intcode = Intcode(line)
                amps.append(intcode)
                queue.appendleft(phase)
                queue = intcode.run_program(queue)

            # Now repeat until no more processes running
            while not amps[4].completed:
                for amp in amps:
                    queue = amp.run_program(queue)

            thrust_outputs.append(queue[-1])

        return max(thrust_outputs)


class Intcode():
    '''Intcode class from day 5. Uses the same logic. However the input
    is now mandatory and is a deque'''
    def __init__(self, line:str, input: deque | None = None) -> None:
        self.codes = [ int(nr) for nr in line.split(',') ]
        # Indicates where the program is
        self.ptr = 0

        self.input = input

        # Create output list
        self.output = deque()

        # Indicates that the code is completed, i.e. 99 has been detected
        self.completed = False


    def fix(self, val1 = 12, val2 = 2) -> None:
        '''Fix the initial values'''
        self.codes[1] = val1
        self.codes[2] = val2


    def run_program(self, input: deque | None = None) -> int:
        '''Run through the program and return the list of output codes.
        The program stops if the program halts or if the input queue
        is empty. In the latter case the program can be resumed in a later
        stage.'''
        # If the program has already stopped, just return the current input
        # queue
        if self.completed:
            return input
        
        # First, the input queue is replaced by a new one:
        if input != None:
            self.input = input

        # Now purge the output queue, in case the program is restarted
        self.output = deque()
        
        # Then start the loop
        while True:
            # If we detect value 99, end program
            if self.codes[self.ptr] == 99:
                self.completed = True
                # Return last code on the output queue
                return self.output

            # Determine opcode and modes
            opcode = self.codes[self.ptr] % 100
            modes = self.codes[self.ptr] // 100

            if opcode == 3:
                # If the input queue is empty, terminate
                if len(self.input) == 0:
                    return self.output
                
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

    phase_seqs = PhaseSequences([5,6,7,8,9])

    return phase_seqs.get_max_thrust_w_feedback(lines[0])

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
