

with open('input.txt') as f:
    data = f.read()

lines = data.splitlines()
bin_length = len(lines[0])

oxygen_list = lines[:]

for i in range(bin_length):
    zeros = 0
    ones = 0

    for oxygen_entry in oxygen_list:
        if oxygen_entry[i] == '0':
            zeros += 1
        elif oxygen_entry[i] == '1':
            ones += 1
        else:
            raise RuntimeError("Invalid bit: {}".format(oxygen_entry[i]))

    if zeros > ones:
        oxygen_bit = '0'
    elif ones > zeros:
        oxygen_bit = '1'
    else:
        oxygen_bit = '1'

    j = 0
    while j < len(oxygen_list):
        if oxygen_list[j][i] == oxygen_bit:
            j += 1
        else:
            del(oxygen_list[j])

    if len(oxygen_list) == 0:
        raise RuntimeError("Oxygen list is empty")
    elif len(oxygen_list) == 1:
        oxygen_bin_string = oxygen_list[0]
        break

if len(oxygen_list) > 1:
    raise RuntimeError("No unique value for Oxygen found")

oxygen_value = int(oxygen_bin_string, base=2)
print("Oxygen value is:", oxygen_value)

co2_list = lines[:]

for i in range(bin_length):
    zeros = 0
    ones = 0

    for co2_entry in co2_list:
        if co2_entry[i] == '0':
            zeros += 1
        elif co2_entry[i] == '1':
            ones += 1
        else:
            raise RuntimeError("Invalid bit: {}".format(co2_entry[i]))

    # if (zeros[i] == 0) or (ones[i] == 0):
    #    continue
    if zeros > ones:
        co2_bit = '1'
    elif ones > zeros:
        co2_bit = '0'
    else:
        co2_bit = '0'

    j = 0
    while j < len(co2_list):
        if co2_list[j][i] == co2_bit:
            j += 1
        else:
            del(co2_list[j])

    if len(co2_list) == 0:
        raise RuntimeError("Co2 list is empty at bit {}".format(i))
    elif len(co2_list) == 1:
        co2_bin_string = co2_list[0]
        break

if len(co2_list) > 1:
    raise RuntimeError("No unique value for Co2 found")

co2_value = int(co2_bin_string, base=2)

print("Co2 value is:", co2_value)
print("Product is:", oxygen_value * co2_value)

