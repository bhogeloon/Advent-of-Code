"""
Day 24, Part 1

Problem description: See https://adventofcode.com/2021/day/24

My solution:
Part 1:

"""

# Imports
import math

# Constants

BASE_MODEL_NR = '99999999999999'
# BASE_MODEL_NR = '11111111111111'

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes
class Nomad():
    '''NOMAD ALU'''

    # Class variables
    instructions = []

    def __init__(self, model_nr: list) -> None:
        '''model_nr is a list of nrs 1-9
        lines contains the instruction set'''
        self.reg = {
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0,
        }

        self.queue = model_nr.copy()
        self.queue.reverse()


    @classmethod
    def fill_instructions(cls, lines: list):
        '''Fill the instructions class variable'''

        for line in lines:
            words = line.split()
            instruction = {
                'operand': words[0],
                'args': words[1:]
            }
            Nomad.instructions.append(instruction)


    def process_model_nr(self) -> bool:
        '''Processes the model number and return True if successfull'''

        for instr in Nomad.instructions:
            if instr['operand'] == 'inp':
                self.inp(*instr['args'])
            elif instr['operand'] == 'add':
                self.add(*instr['args'])
            elif instr['operand'] == 'mul':
                self.mul(*instr['args'])
            elif instr['operand'] == 'div':
                self.div(*instr['args'])
            elif instr['operand'] == 'mod':
                self.mod(*instr['args'])
            elif instr['operand'] == 'eql':
                self.eql(*instr['args'])
            else:
                raise RuntimeError('Invalid operand: {}'.format(instr['operand']))

        if self.reg['z'] == 0:
            return True
        else:
            return False


    def inp(self, a: str):
        '''Store value from the queue in a'''
        self.reg[a] = self.queue.pop()

        
    def add(self, a: str, b:str):
        '''add a to b and store in a'''
        if b.isalpha():
            b_value = self.reg[b]
        else:
            b_value = int(b)

        self.reg[a] += b_value


    def mul(self, a: str, b:str):
        '''multiply a with b and store in a'''
        if b.isalpha():
            b_value = self.reg[b]
        else:
            b_value = int(b)

        self.reg[a] *= b_value


    def div(self, a: str, b:str):
        '''Divide a by b and store in a'''
        if b.isalpha():
            b_value = self.reg[b]
        else:
            b_value = int(b)

        if b_value == 0:
            raise RuntimeError("Division by zero")

        # print(a, self.reg[a])
        div_result = float(self.reg[a]) / b_value
        self.reg[a] = math.trunc(div_result)


    def mod(self, a: str, b:str):
        '''multiply a with b and store in a'''
        if b.isalpha():
            b_value = self.reg[b]
        else:
            b_value = int(b)

        if self.reg[a] < 0 or b_value < 0:
            raise RuntimeError("Mod operand not allowed with negative numbers")

        if b_value == 0:
            raise RuntimeError("Division by zero during mod operand")

        self.reg[a] %= b_value


    def eql(self, a: str, b:str):
        '''Store 1 in a if a==b, otherwise b'''
        if b.isalpha():
            b_value = self.reg[b]
        else:
            b_value = int(b)

        if self.reg[a] == b_value:
            self.reg[a] = 1
        else:
            self.reg[a] = 0



# Functions

def init_model_nr() -> list:
    '''Defines first model nr with all 9's'''
    model_nr = []
    for digit in BASE_MODEL_NR:
        model_nr.append(int(digit))

    return model_nr


def write_model_nr(model_nr: list) -> str:
    '''Writes a line with all model nrs'''
    return ''.join([str(model_dig) for model_dig in model_nr])


def decrease_model_nr(model_nr: list):
    '''Decreases the model_nr by 1'''
    i = 13

    while True:
        if i < 0:
            raise RuntimeError("We reached the lowest number possible")

        model_nr[i] -= 1

        if model_nr[i] == 0:
            model_nr[i] = 9
            i -= 1
        else:
            break


# Main function
def get_solution(lines: list) -> int:
    '''Main function'''
    model_nr = init_model_nr()

    Nomad.fill_instructions(lines)

    nomad = Nomad(model_nr)

    cycle = 0

    while not nomad.process_model_nr():
        cycle += 1

        if cycle % 100000 == 0:
            print(write_model_nr(model_nr))

        decrease_model_nr(model_nr)
        nomad = Nomad(model_nr)

    return write_model_nr(model_nr)


if __name__ == '__main__':
    pass