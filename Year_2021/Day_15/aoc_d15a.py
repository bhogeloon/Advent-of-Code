"""
Day 15, Part 1

Problem description: See https://adventofcode.com/2021/day/15

My solution:
Time for another recursice function. The function find_path does the following:
- Check if this point is already in the current_path. If so, return
- Increase current risk
- Check if current risk level is bigger or equal than the minimal value found to
  this point so far. If so, decrease risk level and return. If not, update this risk level
  and continue
- Check if end point has been reached. If so, update min risk level, decrease current
  risk level and return.
- Add current point to current_path
- Call itself for all neighbors.
- Remove last value of current_path
- Decrease current risk level
- Return

This approach results in the total risk which includes the starting point, so in the
end we have to extract that value.
"""

# Imports


# Global values
min_risk = [-1]
current_path = []
current_risk = [0]
risk_levels = []
cost_to_point = []
end_point = []
end_point_reached = [0]


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def find_path(current_point: tuple):
    '''Recursive function to start off finding the next hop
    in the path'''
    # If current point is already in the path, immediately return
    if current_point in current_path:
        return
    x, y = current_point
    # Increase current risk level
    current_risk[0] += risk_levels[y][x]

    # Check if current risk is already too big
    if current_risk[0] >= cost_to_point[y][x]:
        current_risk[0] -= risk_levels[y][x]
        return

    # Change cost to this point
    cost_to_point[y][x] = current_risk[0]

    # Check if current point is endpoint
    if current_point == end_point[0]:
        min_risk[0] = current_risk[0]
        current_risk[0] -= risk_levels[y][x]
        end_point_reached[0] += 1
        print(end_point_reached[0], min_risk[0], current_risk[0])
        return

    # Add current point to path
    current_path.append(current_point)

    # Call for all neighbors
    if x > 0:
        find_path((x-1,y))
    if x < len(risk_levels[y]) - 1:
        find_path((x+1,y))
    if y > 0:
        find_path((x,y-1))
    if y < len(risk_levels) - 1:
        find_path((x,y+1))

    # Remove current point from list
    current_path.pop()

    # Decrease risk level
    current_risk[0] -= risk_levels[y][x]

    return


def get_min_risk(lines):
    '''Main function to get the Minimal Risk'''
    # Set min risk_level
    min_risk[0] = 2000

    # Read in matrix
    for line in lines:
        risk_levels.append([int(char) for char in line])
        cost_to_point.append([2000 for char in line])

    # Set end_point
    end_point.append((len(risk_levels[0])-1, len(risk_levels) - 1))
    print(end_point)

    # Call find_path for starting point
    find_path((0,0))
        
    # Extract the value of the first field
    return min_risk[0] - risk_levels[0][0]


if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Minimal risk", get_min_risk(lines))
