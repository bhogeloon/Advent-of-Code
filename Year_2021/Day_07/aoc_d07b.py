


with open('input.txt') as f:
    data = f.read()

lines = data.splitlines()

# Fill Crab positions
crabs = []
for line in lines:
    elements = line.split(',')
    for element in elements:
        crabs.append(int(element))

# Make result matrix
fuel = [ 0 for n in range(max(crabs)+1) ]

for i in range(len(fuel)):
    for crab in crabs:
        steps = abs(crab-i)
        for j in range(steps):
            fuel[i] += 1 + j

    print(i)

print("Minimum amount of fuel:", min(fuel))