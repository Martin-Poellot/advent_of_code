data = []
with open("09_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(int(line))

# Puzzle 1
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
        print(f'Result 1: {target}')
        break

# Puzzle 2
for i in range(len(data)):
    contiguous = data[i]
    j = i
    while contiguous < target:
        j += 1
        contiguous += data[j]
    if contiguous == target and j is not i:
        cont_part = data[i:j]
        print(cont_part)
        k = cont_part.index(min(cont_part))
        l = cont_part.index(max(cont_part))
        print(f"{cont_part[k]} + {cont_part[l]} = {cont_part[k] + cont_part[l]}")
