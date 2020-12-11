import numpy as np

data = []
with open("10_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(int(line))

# puzzle 1
current_jolt = 0
count_1_jolt = 0
count_3_jolt = 0
for adapter in sorted(data):
    if current_jolt + 1 == adapter:
        current_jolt += 1
        count_1_jolt += 1
    elif current_jolt + 2 == adapter:
        current_jolt += 2
    elif current_jolt + 3 == adapter:
        current_jolt += 3
        count_3_jolt += 1
count_3_jolt += 1
print(f'{count_1_jolt} + {count_3_jolt} = {count_1_jolt * count_3_jolt}')

# puzzle 2
adapters = sorted(data).copy()
adapters.append(max(adapters) + 3)  # add output
possibilities = {0: 1}
for adapter in adapters:
    possibilities[adapter] = 0
    if adapter - 1 in possibilities:
        possibilities[adapter] += possibilities[adapter - 1]
    if adapter - 2 in possibilities:
        possibilities[adapter] += possibilities[adapter - 2]
    if adapter - 3 in possibilities:
        possibilities[adapter] += possibilities[adapter - 3]
print(f'Maximum possibilities to reach the end: {possibilities[max(adapters)]}')

