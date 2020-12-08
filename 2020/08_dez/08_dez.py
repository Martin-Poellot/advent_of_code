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
data = load_data()
acc = 0
double_counter = np.zeros(len(data))
pointer = 0
while pointer < len(data):
    current_operation, argument = data[pointer]
    if current_operation == 'nop':
        double_counter[pointer] += 1
        if double_counter[pointer] == 2:
            print(f"Result 1: breaks with Acc at {acc}")
            break
        pointer += 1
    elif current_operation == 'acc':
        double_counter[pointer] += 1
        if double_counter[pointer] == 2:
            print(f"Result 1: breaks with Acc at {acc}")
            break
        pointer += 1
        acc += argument
    elif current_operation == 'jmp':
        double_counter[pointer] += 1
        if double_counter[pointer] == 2:
            print(f"Result 1: breaks with Acc at {acc}")
            break
        pointer += argument

# Second puzzle
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
            print(f"Result 2: Reached final line, Acc: {acc}")
            break
