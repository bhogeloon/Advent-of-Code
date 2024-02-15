


with open('input.txt') as f:
    data = f.read()

lines = data.splitlines()

real_fishes= [ int(nr) for nr in lines[0].split(',') ]
fishes = [0]

nr_of_offspring = []

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
totals = {}
for day in range(248, 256):
    totals[day] = 0
    for fish in fishes:
        totals[day] += nr_of_offspring[day - 128 - fish]

    print("Total after {} days: {}".format(day + 1, totals[day]))


# Now calculate the total amount
total = 0
for fish in real_fishes:
    total += totals[255 - fish]


print("Total amount of fishes:", total)