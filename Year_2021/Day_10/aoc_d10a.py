"""
Day 10, Part 1

Problem description: See https://adventofcode.com/2021/day/10

My solution:

For each line, create a stack. The is filled with the open character and
the upper stack entry will be removed again if the closing character is
found. If a non-matching closing character is found, it means that the line
is corrupt. The score is then updated with the matching character and
then we move on to the next line.

At the end of each line, the stack should be empty, otherwise we have
an incomplete line. At this moment, we will ignore this though.
"""


# Global values
score_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

match_table = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def line_corrupt(bracket_stack: list, char: str) -> int:
    '''Updates the bracket_stack and return the score if a non-matching
    character is found. Otherwise, return 0'''
    # If opening character, store it and return False
    if char in match_table.keys():
        bracket_stack.append(char)
        return 0

    # Now investigate closing brackets one by one
    elif char in match_table.values():
        # If this is the first char, return the matching score
        if len(bracket_stack) == 0:
            return score_table[char]
        # else if the character matches the current opening bracket
        elif char == match_table[bracket_stack.pop()]:
            return 0
        # else return score
        else:
            return score_table[char]

    # If any other character was found, raise exception
    else:
        raise RuntimeError("Unkown char found: {}".format(char))

    # This should never be reached
    return


def get_score(lines):
    '''Main function to get the final score'''
    score = 0

    for line in lines:
        # Create stack
        bracket_stack = []

        for char in line:
            char_score = line_corrupt(bracket_stack, char)
            if char_score > 0:
                score += char_score
                break

    return score

if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Score is:", get_score(lines))
