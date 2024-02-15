"""
Day 10, Part 2

Problem description: See https://adventofcode.com/2021/day/10

My solution:

So now we keep the same code to check for corrupte lines, but instead
of keeping the score, we just ignore them.

For the ones that make it to the end, we will investigate the remaining 
characters in the stack and calculate all the score for those.
]"""


# Global values
corrupt_score_table = {
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

compl_score_table = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def check_line_corrupt(bracket_stack: list, char: str) -> int:
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
            return corrupt_score_table[char]
        # else if the character matches the current opening bracket
        elif char == match_table[bracket_stack.pop()]:
            return 0
        # else return score
        else:
            return corrupt_score_table[char]

    # If any other character was found, raise exception
    else:
        raise RuntimeError("Unkown char found: {}".format(char))

    # This should never be reached
    return


def middle_score(my_list: list) -> int:
    '''This function determines the middle score of a list
    of integers'''
    list_len = len(my_list)

    # Raise exception if not on odd number
    if (list_len % 2) == 0:
        raise RuntimeError("Even number of scores: {}".format(list_len))

    # Sort the list
    my_list.sort()

    # Determine the middle entry
    middle = list_len // 2

    print(list_len, middle)

    for my_value in my_list:
        print(my_value)

    return my_list[middle]


def get_score(lines):
    '''Main function to get the final score'''
    line_scores = []

    for line in lines:
        # Create stack
        bracket_stack = []
        line_is_corrupt = False

        for char in line:
            char_score = check_line_corrupt(bracket_stack, char)
            if char_score > 0:
                line_is_corrupt = True
                break

        if not line_is_corrupt:
            line_score = 0
            for i in range(len(bracket_stack)):
                line_score *= 5
                line_score += compl_score_table[bracket_stack.pop()]

            line_scores.append(line_score)

    return middle_score(line_scores)


if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Middle Score is:", get_score(lines))
