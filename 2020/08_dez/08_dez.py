import time

def load_data():
    data = []
    with open("08_dez_input.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            [operation, arg] = line.split(' ')
            data.append([operation, int(arg)])
    return data

# First puzzle
import numpy as np
start_1 = time.time()
data = load_data()
acc = 0
double_counter = np.zeros(len(data))
pointer = 0
while pointer < len(data):
    current_operation, argument = data[pointer]
    if current_operation == 'nop':
        double_counter[pointer] += 1
        if double_counter[pointer] == 2:
            elapsed1 = time.time() - start_1
            print(f"Result 1: breaks with Acc at {acc}")
            print(f'Elapsed Time: {elapsed1:.6f}s')
            break
        pointer += 1
    elif current_operation == 'acc':
        double_counter[pointer] += 1
        if double_counter[pointer] == 2:
            elapsed1 = time.time() - start_1
            print(f"Result 1: breaks with Acc at {acc}")
            print(f'Elapsed Time: {elapsed1:.6f}s')
            break
        pointer += 1
        acc += argument
    elif current_operation == 'jmp':
        double_counter[pointer] += 1
        if double_counter[pointer] == 2:
            elapsed1 = time.time() - start_1
            print(f"Result 1: breaks with Acc at {acc}")
            print(f'Elapsed Time: {elapsed1:.6f}s')
            break
        pointer += argument

# Second puzzle
start_2 = time.time()
for change_to, change_from in [['nop', 'jmp'], ['jmp', 'nop']]:
    change_pos = 0
    for i, action in enumerate(data):
        data = load_data()
        acc = 0
        double_counter = np.zeros(len(data))
        pointer = 0
        if action[0] == change_to and i >= change_pos:
            data[i][0] = change_from
        while pointer < len(data):
            current_operation, argument = data[pointer]
            if current_operation == 'nop':
                double_counter[pointer] += 1
                if double_counter[pointer] == 2:
                    break
                pointer += 1
            elif current_operation == 'acc':
                double_counter[pointer] += 1
                if double_counter[pointer] == 2:
                    break
                pointer += 1
                acc += argument
            elif current_operation == 'jmp':
                double_counter[pointer] += 1
                if double_counter[pointer] == 2:
                    break
                pointer += argument
        if pointer >= len(data):
            elapsed2 = time.time() - start_2
            print(f"Result 2: Reached final line, Acc: {acc}")
            print(f'Elapsed Time: {elapsed2:.6f}s')
            break
