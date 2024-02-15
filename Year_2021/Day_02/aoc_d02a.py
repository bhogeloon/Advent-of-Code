

with open('input.txt') as f:
    data = f.read()

lines = data.splitlines()

hor_pos = 0
depth = 0

for line in lines:
    (instruction, amount_str) = line.split()
    amount = int(amount_str)

    if instruction == 'forward':
        hor_pos += amount
    elif instruction == 'up':
        depth -= amount
    elif instruction == 'down':
        depth += amount
    else:
        raise RuntimeError("no valid instruction {}".format(instruction))

print("Horizontal postion:", hor_pos)
print("Depth:", depth)
print("Product:", hor_pos * depth)

