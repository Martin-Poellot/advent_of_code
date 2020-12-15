import time
data = []
with open("09_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(int(line))

# Puzzle 1
start_1 = time.time()
preamble_length = 25
for i in range(preamble_length, len(data) - preamble_length - 1, 1):
    cutout = data[i:i + preamble_length]
    target = data[i + preamble_length]
    check_if_valid = False
    for j, n1 in enumerate(cutout):
        for n2 in cutout[j:]:
            if n1 + n2 == target:
                if n1 is not n2:
                    check_if_valid = True
    if not check_if_valid:
        elapsed1 = time.time() - start_1
        print(f'Result 1: {target}')
        print(f'Elapsed Time: {elapsed1:.6f}s')
        break

# Puzzle 2
start_2 = time.time()
for i in range(len(data)):
    contiguous = data[i]
    j = i
    while contiguous < target:
        j += 1
        contiguous += data[j]
    if contiguous == target and j is not i:
        cont_part = data[i:j]
        k = cont_part.index(min(cont_part))
        l = cont_part.index(max(cont_part))
        elapsed2 = time.time() - start_2
        print(f"{cont_part[k]} + {cont_part[l]} = {cont_part[k] + cont_part[l]}")
        print(f'Elapsed Time: {elapsed2:.6f}s')
