import time
data = []
with open("14_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.strip('\n'))

# Puzzle 1
start_1 = time.time()
memory = {}
masks = []
curr_mask = None
curr_value = None
curr_address = None

for line in data:
    identifier, value = line.split(" = ")
    if identifier == "mask":
        masks.append(value)
        curr_mask = value
    else:
        curr_address = int(identifier[4:-1])  # decimal address
        curr_value = int(value)  # decimal value

        binary_value = list(bin(curr_value)[2:].zfill(36))  # cvt to 36 bit list
        new_value = [0] * 36  # empty value with 36 zeros

        for i, (current_mask_bit, bin_value) in enumerate(zip(curr_mask, binary_value)):
            if current_mask_bit == "X":
                new_value[i] = bin_value
            else:
                new_value[i] = current_mask_bit

        memory[curr_address] = int("".join(new_value), 2)

elapsed1 = time.time() - start_1
print(f'Sum of all Values in Memory: {sum(memory.values())}')
print(f'Elapsed Time: {elapsed1:.6f}s')

# Puzzle 2

start_2 = time.time()
memory = {}
masks = []
curr_mask = None
curr_value = None
curr_address = None

for line in data:
    identifier, value = line.split(" = ")
    if identifier == "mask":
        masks.append(value)
        curr_mask = value
    else:
        curr_address = int(identifier[4:-1])  # decimal address
        curr_value = int(value)  # decimal value

        binary_address = list(bin(curr_address)[2:].zfill(36))  # cvt to 36 bit list
        new_address = ["0"] * 36

        for i, (current_mask_bit, value) in enumerate(zip(curr_mask, binary_address)):
            if current_mask_bit == "X":
                new_address[i] = "X"
            elif current_mask_bit == "0":
                new_address[i] = value
            elif current_mask_bit == "1":
                new_address[i] = "1"
        new_address = "".join(new_address)
        number_of_floats = new_address.count("X")

        floatings = []
        for i in range(2**number_of_floats):
            floatings.append(list(bin(i)[2:].zfill(number_of_floats)))

        for float_ in floatings:
            bit_runner = 0
            float_address = ""
            for x in new_address:
                if x == "X":
                    float_address += str(float_[bit_runner])
                    bit_runner += 1
                else:
                    float_address += str(x)
            memory[int(float_address, 2)] = curr_value

elapsed2 = time.time() - start_2
print(f'Sum of all Values in Memory: {sum(memory.values())}')
print(f'Elapsed Time: {elapsed2:.6f}s')
