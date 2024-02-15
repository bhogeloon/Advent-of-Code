


with open('input.txt') as f:
    data = f.read()

lines = data.splitlines()

fishes= [ int(nr) for nr in lines[0].split(',') ]

for day in range(80):
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1

print("Total amount of fishes:", len(fishes))