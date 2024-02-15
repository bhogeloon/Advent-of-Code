

with open('input.txt') as f:
    data = f.read()

lines = data.splitlines()
bin_length = len(lines[0])
ones = []
zeros = []

for i in range(bin_length):
    ones.append(0)
    zeros.append(0)

for line in lines:
    for i in range(bin_length):
        if line[i] == '0':
            zeros[i] += 1
        elif line[i] == '1':
            ones[i] += 1
        else:
            raise RuntimeError("Invalid bit: {}".format(line[i]))

gamma_string = ''
epsilon_string = ''

for i in range(bin_length):
    if zeros[i] > ones[i]:
        gamma_string += '0'
        epsilon_string += '1'
    elif ones[i] > zeros[i]:
        gamma_string += '1'
        epsilon_string += '0'
    else:
        raise RuntimeError("Equal values for 0 and 1 in pos {}.".format(i))

gamma_value = int(gamma_string, base=2)
epsilon_value = int(epsilon_string, base=2)

print("Gamma is:", gamma_value)
print("Epsilon is:", epsilon_value)
print("Product is:", gamma_value * epsilon_value)

