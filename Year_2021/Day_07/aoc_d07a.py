


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
        fuel[i] += abs(crab-i)

print("Minimum amount of fuel:", min(fuel))