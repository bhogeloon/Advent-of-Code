"""
Day 16, Part 2

Problem description: See https://adventofcode.com/2021/day/16

My solution:

Part 1:
Read in all the hexadecimal numbers and convert them into binary values.
Store the binary characters in a deque object to be able to treat them
as a queue rather than a stack.
Then write functions to process the different sort of packets.

I also defined a class Gv to store the version_cnt variable, so I can
easily alter that in all functions.

Part2:
Add functions for all the different operators in process packets.
"""

# Imports
from collections import deque

# Global variables

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
    # For part 2 we can ignore the version
    bin2int(read_bits(bin_q, 3))

    return


def read_type(bin_q: deque) -> int:
    '''Reads 3 bits and returns the type'''

    return bin2int((read_bits(bin_q, 3)))


def process_literal(bin_q: deque):
    '''Processes a literal packet. Return the values as a list'''
    result_str = ''
    
    # Process literal values until first bit is 0
    last_value_reached = False
    while not last_value_reached: 
        first_bit = read_bits(bin_q, 1)
        if first_bit == '0':
            last_value_reached = True

        # Read 4 bits and add them to the list
        result_str += read_bits(bin_q, 4)

    return bin2int(result_str)


def process_operator(bin_q:deque):
    '''Processes an operator packet. Return the calculated results in a list'''
    results = []

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
            results.append(process_packet(sub_pack))

    # If fixed amount of packets
    else:
        # Read nr of packets
        nr_of_packs = bin2int(read_bits(bin_q, 11))

        # Read the packets
        for i in range(nr_of_packs):
            results.append(process_packet(bin_q))

    return results


def process_packet(bin_q:deque) -> int:
    '''Processes a packet and return result'''

    # Start with reading the version
    read_ver(bin_q)

    # Then read the type
    packet_type = read_type(bin_q)

    # If literal, process literal
    if packet_type == 4:
        # Process literal
        return process_literal(bin_q)

    # process operator
    results = process_operator(bin_q)

    if packet_type == 0:
        result = sum(results)
        print("summarising {} = {}".format(results, result))
    elif packet_type == 1:
        result = 1
        for sub_result in results:
            result *= sub_result
        print("multiplying {} = {}".format(results, result))
    elif packet_type == 2:
        result = min(results)
        print("minimum of {} = {}".format(results, result))
    elif packet_type == 3:
        result = max(results)
        print("maximum of {} = {}".format(results, result))
    elif packet_type == 5:
        if results[0] > results[1]:
            result = 1
        else:
            result = 0
        print("greater than {} = {}".format(results, result))
    elif packet_type == 6:
        if results[0] < results[1]:
            result = 1
        else:
            result = 0
        print("smaller than {} = {}".format(results, result))
    elif packet_type == 7:
        if results[0] == results[1]:
            result = 1
        else:
            result = 0
        print("equal to {} = {}".format(results, result))
    else:
        raise RuntimeError("Unexpected packet type: {}".format(packet_type))

    return result


def get_bits_result(lines):
    '''Main function to get the sum of the versions'''
    bin_q = deque()

    # Read all hexadecimal values, convert them to binary and store in a deque
    for line in lines:
        for char in line:
            hex_value = int(char, 16)
            bin_str = format(hex_value, '04b')
            bin_q.extend(list(bin_str))

    return process_packet(bin_q)


if __name__ == '__main__':
    lines = read_input('input.txt')
    # lines = read_input('example8.txt')
    print("End result:", get_bits_result(lines))
