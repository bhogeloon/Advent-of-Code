


with open('input.txt') as f:
    data = f.read()

lines = data.splitlines()

# The real input
real_fishes= [ int(nr) for nr in lines[0].split(',') ]

# A 'bogus' input to create a scenario for a single fish
fishes = [0]

# A list contiaining the nr of offsprings after a certain amount of days
nr_of_offspring = []

# Fill the nr_of_offspring list for the bogus fish for 128 days
for day in range(128):
    nr_of_fishes = len(fishes)
    print("at te start of day {} there are {} fishes".format(day, nr_of_fishes))

    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1

    nr_of_offspring.append(len(fishes))

# Now calculate for the next xxx days
# Then go through the current list and calculate the offspring based on the
# 128 days calculation, without creating the actual list

# This is the totals for last few days
totals = {}
for day in range(248, 256):
    totals[day] = 0
    for fish in fishes:
        # The total number of offspring depends on the day in which it has
        # The first offspring. On that day, the total number can be retrieved from
        # the 128 day list.
        totals[day] += nr_of_offspring[day - 128 - fish]

    print("Total after {} days: {}".format(day + 1, totals[day]))


# Now calculate the total amount in the 'real_fishes' list, depending on the current
# state
total = 0
for fish in real_fishes:
    total += totals[255 - fish]


print("Total amount of fishes:", total)