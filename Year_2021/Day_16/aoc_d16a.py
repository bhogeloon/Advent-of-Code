"""
Day 16, Part 1

Problem description: See https://adventofcode.com/2021/day/16

My solution:
Read in all the hexadecimal numbers and convert them into binary values.
Store the binary characters in a deque object to be able to treat them
as a queue rather than a stack.
Then write functions to process the different sort of packets.

I also defined a class Gv to store the version_cnt variable, so I can
easily alter that in all functions.
"""

# Imports
from collections import deque

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''
    version_cnt = 0


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def bin2int(bin_str: str) -> int:
    '''Converts bin string to int'''

    return int(bin_str, 2)


def read_bits(bin_q: deque, n: int) -> str:
    '''Reads n bits form queue and returns the bin string'''
    bin_str = ''
    for i in range(n):
        bin_str += bin_q.popleft()

    return bin_str


def read_ver(bin_q: deque):
    '''Reads first three bits from bin_q and adds to version_cnt'''
    Gv.version_cnt += bin2int(read_bits(bin_q, 3))

    return


def read_type(bin_q: deque) -> int:
    '''Reads 3 bits and returns the type'''

    return bin2int((read_bits(bin_q, 3)))


def process_literal(bin_q: deque):
    '''Processes a literal packet.'''
    # Process literal values until first bit is 0
    last_value_reached = False
    while not last_value_reached: 
        first_bit = read_bits(bin_q, 1)
        if first_bit == '0':
            last_value_reached = True

        # Read 4 bits and ignore for now
        read_bits(bin_q, 4)
        # Add 5 to bin_cnt

    return


def process_operator(bin_q:deque):
    '''Processes an operator packet. '''
    # Get length type id
    length_type_id = read_bits(bin_q, 1)

    # If fixed length
    if length_type_id == '0':
        # Read length
        sub_pack_len = bin2int(read_bits(bin_q, 15))

        # Extract the bits in a subpacket
        sub_pack = deque()
        for i in range(sub_pack_len):
            sub_pack.append(bin_q.popleft())

        # Keep processing packets until all empty queue
        while len(sub_pack) > 0:
            process_packet(sub_pack)

    # If fixed amount of packets
    else:
        # Read nr of packets
        nr_of_packs = bin2int(read_bits(bin_q, 11))

        # Read the packets
        for i in range(nr_of_packs):
            process_packet(bin_q)

    return


def process_packet(bin_q:deque):
    '''Processes a packet'''
    # Start with reading the version
    read_ver(bin_q)

    # Then read the type
    packet_type = read_type(bin_q)

    # If literal, process literal
    if packet_type == 4:
        # Process literal
        process_literal(bin_q)
    else:
        # process operator
        process_operator(bin_q)

    return


def get_sum_of_ver(lines):
    '''Main function to get the sum of the versions'''
    bin_q = deque()

    # Read all hexadecimal values, convert them to binary and store in a deque
    for line in lines:
        for char in line:
            hex_value = int(char, 16)
            bin_str = format(hex_value, '04b')
            bin_q.extend(list(bin_str))

    process_packet(bin_q)

    return Gv.version_cnt


if __name__ == '__main__':
    lines = read_input('input.txt')
    # lines = read_input('example1.txt')
    print("Sum of the versions:", get_sum_of_ver(lines))
