

with open('depth_measurements.txt') as f:
    data = f.read()

lines = data.splitlines()

depths = []

for line in lines:
    depths.append(int(line))

depth_sums = []

for i in range(2, len(depths)):
    depth_sums.append(sum(depths[i-2:i+1]))

nr_of_increases = 0

for i in range(1, len(depth_sums)):
    if depth_sums[i] > depth_sums[i-1]:
        nr_of_increases += 1

print("Nr of increases is:", nr_of_increases)
