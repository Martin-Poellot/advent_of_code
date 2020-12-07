data = []
with open("03_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.split('\n')[0])

def do_calc(move):
    current_x = 0
    current_y = 0
    line_len = len(data[0])
    tree_counter = 0
    free_counter = 0
    for i, line in enumerate(data[1:]):
        if (i + 1) % move[1] == 1:
            continue
        current_x += move[0]
        current_y += move[1]
        query_pos = current_x % line_len
        if line[query_pos] == '.':
            free_counter += 1
        elif line[query_pos] == "#":
            tree_counter += 1
    return tree_counter

if __name__ == '__main__':
    moves = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    tree_counters = []
    for move in moves:
        tree_counter = do_calc(move)
        print(f'Final Tree Encounter Counter for {move}: {tree_counter}')
        tree_counters.append(tree_counter)
    result_2 = tree_counters[0]
    print(f'Result for [3, 1]: {tree_counters[1]}')
    for p in tree_counters[1:]:
        print(f"{result_2} * {p}")
        result_2 *= p
    print(f'Multiple of trees hit: {result_2}')
