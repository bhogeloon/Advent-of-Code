


with open('input.txt') as f:
    data = f.read()

lines = data.splitlines()

# Create matrix
location = [[0 for y in range(1000)] for x in range(1000)]


# Update matrix
for line in lines:
    xy_str = line.split(' -> ')

    (x1, y1) = [ int(nr) for nr in xy_str[0].split(',') ]
    (x2, y2) = [ int(nr) for nr in xy_str[1].split(',') ]

    # if x coordinates are the same:
    if x1 == x2:
        # Put them in the right order
        (y_small, y_big) = sorted([y1, y2])
        for y in range(y_small, y_big + 1):
            location[x1][y] += 1

    # if y coordinates are the same:
    elif y1 == y2:
        # Put them in the right order
        (x_small, x_big) = sorted([x1, x2])
        for x in range(x_small, x_big + 1):
            location[x][y1] += 1

    # If both are different:
    else:
        # Determine  absolute range
        abs_range = range(abs(x2-x1)+1)
        # Determine x step
        if x1 < x2:
            x_step = 1
        else:
            x_step = -1

        # Determine y-range
        if y1 < y2:
            y_step = 1
        else:
            y_step = -1

        # Update matrix
        for i in abs_range:
            location[x1+i*x_step][y1+i*y_step] += 1

# Count entries larger than 1
total = 0
for x in location:
    for y in x:
        if y > 1:
            total +=1

print("Total:", total)
