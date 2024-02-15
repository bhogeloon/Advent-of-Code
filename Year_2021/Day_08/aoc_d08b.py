"""
Day 8, Part 2

Problem description: See https://adventofcode.com/2021/day/8

My solution:

This one was a little trickier.
I started by processing the easy records, the one with unique length.
These I could easily correlate with a value.
Then I tried to figure out how to recognise the others and came up
with a solution to count the overlapping segments (or characters) with a
known value. For that reason I chose to use sets to store the character
as I could more easily calculate the overlap.
Then I stored all mappings in a dict, using a string with sorted letters
as not all letters were in the same order in the output section.
Then it was just a question of sorting the characters on the output section
and reading the mappings.

"""


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def decipher_input(input_strs):
    '''
    This function returns a mapping (dict) from digit_string 
    to digit decimal value (0 - 9).
    '''
    # This will be the mapping from set to value
    digit_value = {}
    # This one will be the reverse mapping (used in this function only)
    digit_set = {}

    # In the firs cycle, we only look at the 'easy' values, which
    # are recogonisable by length
    for input_str in input_strs:
        input_set = set(input_str)
        input_sort = ''.join(sorted(input_set))
        if len(input_set) == 2:
            digit_value[input_sort] = 1
            digit_set[1] = input_set
        elif len(input_set) == 3:
            digit_value[input_sort] = 7
            digit_set[7] = input_set
        elif len(input_set) == 4:
            digit_value[input_sort] = 4
            digit_set[4] = input_set
        elif len(input_set) == 7:
            digit_value[input_sort] = 8
            digit_set[8] = input_set

    # In the next cycle, we only look at length 6 and 5
    for input_str in input_strs:
        input_set = set(input_str)
        input_sort = ''.join(sorted(input_set))
        # This one can be eiter 0, 6 or 9
        if len(input_set) == 6:
            # if both letters of digit 1 appear, it 0 or 9
            # otherwise it must be 6
            if len(input_set & digit_set[1]) < 2:
                digit_value[input_sort] = 6
                digit_set[6] = input_set
            # if all letters of digit 4 overlap, it must be 9
            elif len(input_set & digit_set[4]) == 4:
                digit_value[input_sort] = 9
                digit_set[9] = input_set
            # and if not, it must be 0
            else:
                digit_value[input_sort] = 0
                digit_set[0] = input_set

        # This one is either 2, 3 or 5:
        elif len(input_set) == 5:
            # if it overlaps with digit 1, it must be 3
            if len(input_set & digit_set[1]) == 2:
                digit_value[input_sort] = 3
                digit_set[3] = input_set
            # if the overlap with digit 4 is only 2, it must be 2
            elif len(input_set & digit_set[4]) == 2:
                digit_value[input_sort] = 2
                digit_set[2] = input_set
            # and what remains is 5
            else:
                digit_value[input_sort] = 5
                digit_set[5] = input_set

    return digit_value


def get_total(lines):
    total = 0

    for line in lines:
        (input_part, output_part) = line.split(' | ')
        input_strs = input_part.split()
        output_strs = output_part.split()

        digit_value = decipher_input(input_strs)

        output_digits_str = ''

        for output_str in output_strs:
            output_set = set(output_str)
            output_sort = ''.join(sorted(output_set))
            output_digits_str += str((digit_value[output_sort]))

        number = int(output_digits_str)

        total += number

    return total


if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Total:", get_total(lines))
