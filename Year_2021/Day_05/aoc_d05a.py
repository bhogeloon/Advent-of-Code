


with open('input.txt') as f:
    data = f.read()

lines = data.splitlines()

# Create matrix
location = []

for x in range(1000):
    ys = []
    for y in range(1000):
        ys.append(0)
    location.append(ys)

# Update matrix
for line in lines:
    xy_str = line.split(' -> ')
    (x1_str, y1_str) = xy_str[0].split(',')
    x1 = int(x1_str)
    y1 = int(y1_str)
    (x2_str, y2_str) = xy_str[1].split(',')
    x2 = int(x2_str)
    y2 = int(y2_str)

    # if x coordinates are the same:
    if x1 == x2:
        # Put them in the right order
        (y_small, y_big) = sorted([y1, y2])
        for y in range(y_small, y_big + 1):
            location[x1][y] += 1


    # if y coordinates are the same:
    if y1 == y2:
        # Put them in the right order
        (x_small, x_big) = sorted([x1, x2])
        for x in range(x_small, x_big + 1):
            location[x][y1] += 1


# Count entries larger than 1
total = 0
for x in location:
    for y in x:
        if y > 1:
            total +=1

print("Total:", total)
