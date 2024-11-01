"""
Year 2015, Day 7

Problem description: See https://adventofcode.com/2015/day/7

The following classes are used:
- Wire: Represents a wire with an id and a signal value. Initially, the signal
    value will None.
- Wires: A dict class with as key the wire id and as value the Wire object.
- Gate: A gate consists of the following attributes:
    - target: a link to the Wire that will be used to store the result
    - operator: the bitwise operator that is specified. A new one is added
        (ASSIGN) for a simple assignment operation.
    - operands: A tuple of one or two operands. Each operand can hold either:
        - An integer value
        - A Wire object
- Gates: A list container class of Gate objects

Part 1: Go through the list of Gates and try to evaluate the bitwise operation.
This can only be done when all the operands or known, i.e. either an integer
value or a Wire object with a signal value that is not None. If it is not 
possible, just skip it.
Store the calculated value in the target Wire object.
Keep repeating this process until eventually the signal value of Wire 'a' is
known.

Part 2: Reset all signals to None after preserving the signal on wire a. Then
store that on wire b and redo the evaluation part.
"""

# Imports
from __future__ import annotations
from pprint import pprint
import re


# Constants

TARGET = 'a'
TARGET2 = 'b'
TARGET_TEST = 'defghixy'

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Wire:
    '''Represents a wire with a id and signal attribute'''
    
    def __init__(self, id, signal=None) -> None:
        self.id=id
        self.signal=signal


    def print(self) -> None:
        '''Print function for debugging'''
        print(f'Wire {self.id} gets value {self.signal}')
        

class Wires(dict[str,Wire]):
    '''Dict class with as key the wire identifier and as value a Wire object'''

    def add_wire(self, id, signal=None):
        '''Add the wire if it doesn't exist or otherwise assign value if not
        None'''
        if signal != None or id not in self.keys():
            self[id] = Wire(id, signal)

        return self[id]


class Gate:
    '''Represents a gate. It has an operator as attribute. This can be one
    of the following:
    - AND
    - OR
    - LSHIFT
    - RSHIFT
    - NOT
    - ASSIGN (this means the value is assigned directly)
    It also has a tuple of operands, which is either length 2 or 1 (for NOT
    and ASSIGN). The operands can refer to a wire or contain an integer
    Finally, it has a target, which is always a referal to a wire'''

    # Class variables

    wires = Wires()

    def __init__(self, line: str) -> None:
        (line_part1, target_str) = line.split(' -> ')
        
        # Set target
        self.target = self.wires.add_wire(target_str)

        # Determine operator part
        ops_parts = line_part1.split()
        # If only on word then it is an assignment
        if len(ops_parts) == 1:
            self.operator = 'ASSIGN'
            self.operands = (self.get_operand(ops_parts[0]),)
        # When two words, first part is operator and second operand
        elif len(ops_parts) == 2:
            self.operator = ops_parts[0]
            self.operands = (self.get_operand(ops_parts[1]),)
        # In all other cases, second part is operator
        else:
            self.operator = ops_parts[1]
            self.operands = (
                self.get_operand(ops_parts[0]),
                self.get_operand(ops_parts[2]),
            )

        if self.target.id == 'b':
            print(self.target.id, self.operator, self.operands, type(self.operands[0]))


    def get_operand(self, word: str):
        '''Return either an int value or a Wire object'''
        if re.fullmatch(r'\d+', word):
            return int(word)
        else:
            return self.wires.add_wire(word)
        

    def evaluate(self) -> None:
        '''Try to evaluate this gate'''
        # if target already has a value, then don't bother
        if self.target.signal != None:
            return
        
        # Values used for the operands
        op_vals = []

        for operand in self.operands:
            if type(operand) == int:
                op_vals.append(operand)
            else:
                # If one of the operands does not have a value, don't bother
                if operand.signal == None:
                    return
                else:
                    op_vals.append(operand.signal)
            
        # Then calculate the target value
        if self.operator == 'ASSIGN':
            self.target.signal = op_vals[0]
        elif self.operator == 'NOT':
            self.target.signal = ~op_vals[0]
        elif self.operator == 'AND':
            self.target.signal = op_vals[0] & op_vals[1]
        elif self.operator == 'OR':
            self.target.signal = op_vals[0] | op_vals[1]
        elif self.operator == 'LSHIFT':
            self.target.signal = op_vals[0] << op_vals[1]
        elif self.operator == 'RSHIFT':
            self.target.signal = op_vals[0] >> op_vals[1]
        else:
            raise RuntimeError(f'Unkown operator {self.operator}')
        
        self.target.print()


class Gates(dict[str, Gate]):
    '''Dict container class of Gate objects. The key is the wire id of the
    target wire'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            new_gate = Gate(line)
            self[new_gate.target.id] = new_gate


    def evaluate(self) -> None:
        '''Keep evaluating all values until a target has been found'''
        if Gv.test:
            solution_target = TARGET_TEST[5]
        else:
            solution_target = TARGET

        while Gate.wires[solution_target].signal == None:
            for gate in self.values():
                gate.evaluate()
            
            if Gv.test:
                pprint([Gate.wires[w].signal for w in TARGET_TEST])

    def reset(self) -> None:
        '''Resets all the gates after preserving the state of wire a and then
        store that in wire b'''
        # Preserve value of wire a
        orig_signal = self[TARGET].target.signal

        # Reset all signals to none
        for wire in Gate.wires.values():
            wire.signal = None

        # Store original a value in b
        self[TARGET2].target.signal = orig_signal


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    gates = Gates(lines)
    gates.evaluate()

    if Gv.test:
        return [Gate.wires[w].signal for w in TARGET_TEST]
    else:
        return Gate.wires[TARGET].signal

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    # This solution does not work on the test data, so no use using the
    # -t option
    # Gv.test = kwargs.get('test', False)

    gates = Gates(lines)
    gates.evaluate()
    gates.reset()
    gates.evaluate()

    return Gate.wires[TARGET].signal

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
