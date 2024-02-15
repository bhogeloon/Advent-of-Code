

with open('depth_measurements.txt') as f:
    data = f.read()

lines = data.splitlines()

depths = []

for line in lines:
    depths.append(int(line))

nr_of_increases = 0

for i in range(1, len(depths)):
    if depths[i] > depths [i-1]:
        nr_of_increases += 1

print("Nr of increases is:", nr_of_increases)
