"""
Day 12, Part 1

Problem description: See https://adventofcode.com/2021/day/12

My solution:
First we store all known paths in a dict, with the starting point as 
the key. The value is the list of possible end-points.
Note that the start point can be the A end or the B end (because you
can also travel the other way).

Then we start iterating over each possible destination, calling the same
function recursively. In the mean time
we keep track of the current path in a list. If we see the end as the
destination, we found a proper path. If we see a small cave, which is
already in the list, we have found a dead end and we are not going to
proceed.

"""


# Global values
current_path = []
connections = {}


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def calculate_path(start_point: str) -> int:
    '''Recursive function to calculate the path'''
    # If this point is a small cage we already visited, don't bother
    if start_point.islower() and start_point in current_path:
        return 0

    # If the current start_point is 'end', then we have a valid path
    if start_point == 'end':
        return 1

    # Then add this point to the path
    current_path.append(start_point)
    paths_found = 0

    for end_point in connections[start_point]:
        paths_found += calculate_path(end_point)
    
    # Now remove the current point before returning
    current_path.pop()

    return paths_found


def get_paths_found(lines):
    '''Main function to get the number of paths'''
    # Read the lines in the dict
    for line in lines:
        (a_point, b_point) = line.split('-')

        if a_point not in connections.keys():
            connections[a_point] = []
        connections[a_point].append(b_point)

        # Reverse path
        if b_point not in connections.keys():
            connections[b_point] = []
        connections[b_point].append(a_point)

    # Now start the recursive function from start
    paths_found = calculate_path('start')

    return paths_found


if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Number of paths found:", get_paths_found(lines))
