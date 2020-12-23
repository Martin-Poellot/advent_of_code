import time

example = '389125467'
my_input = '942387615'


def put_current_cup_as_first(current_cup_value, input_list):
    current_cup_index = input_list.index(current_cup_value)
    while current_cup_index != 0:
        removed_cup = input_list.pop(0)
        input_list.append(removed_cup)
        current_cup_index = input_list.index(current_cup_value)
    return input_list, current_cup_index


def find_destination_cup(current_cup_value, input_list):
    destination_cup_value = current_cup_value - 1
    if destination_cup_value in input_list:
        return input_list.index(destination_cup_value)
    else:
        if destination_cup_value < 2:
            return find_destination_cup(max(input_list) + 1, input_list)
        else:
            return find_destination_cup(destination_cup_value, input_list)


def remove_3(input_list, current_cup_index):
    removed_3_cups = []
    for i in range(3):
        removed_3_cups.append(input_list.pop(current_cup_index + 1))
    return removed_3_cups, input_list


def remove_3_ext(input_list, current_cup_index):
    removed_3_cups = []
    if current_cup_index < len(input_list) - 3:
        for i in range(3):
            removed_3_cups.append(input_list.pop(current_cup_index + 1))
    else:
        for i in range(3):
            q = input_list.pop(0)
            input_list.append(q)
        for i in range(3):
            removed_3_cups.append(input_list.pop(current_cup_index - 2))
    return removed_3_cups, input_list


# puzzle 1
start_1 = time.time()

input_list = [int(x) for x in my_input]
current_cup_value = input_list[0]

for i in range(100):
    input_list, current_cup_index = put_current_cup_as_first(current_cup_value, input_list)

    removed_3_cups, input_list = remove_3(input_list, current_cup_index)

    dest_cup_idx = find_destination_cup(current_cup_value, input_list)

    input_list[dest_cup_idx + 1:dest_cup_idx + 1] = removed_3_cups

    current_cup_value = input_list[int((current_cup_index + 1) % len(input_list))]


result = put_current_cup_as_first(1, input_list)[0][1:]
result_str = ""
for x in result:
    result_str += str(x)

elapsed1 = time.time() - start_1
print(f'Result 1: {result_str}')
print(f'Elapsed Time: {elapsed1:.6f}s')


# puzzle 2
start_2 = time.time()

input_list = [int(x) for x in my_input]
for x in range(10, 1000001):
    input_list.append(x)

current_cup_index = 0
current_cup_value = input_list[current_cup_index]

for i in range(10000000):
    removed_3_cups, input_list = remove_3_ext(input_list, current_cup_index)

    dest_cup_idx = find_destination_cup(current_cup_value, input_list)

    input_list[dest_cup_idx + 1:dest_cup_idx + 1] = removed_3_cups

    current_cup_value = input_list[int((current_cup_index + 1) % len(input_list))]

    current_cup_index = input_list.index(current_cup_value)

    if not i % 1000:
        print(f'\rSteps Done: {((i + 1) / 10000000) * 100:.4f} %')
    if i > 9999998:
        print(f'{i}: {put_current_cup_as_first(1, input_list)[0][1:3]}')

print(input_list)
star_cups = put_current_cup_as_first(1, input_list)[0][1:3]
print(star_cups)
result = star_cups[0] * star_cups[1]

elapsed2 = time.time() - start_2
print(f'Result 2: {result}')
print(f'Elapsed Time: {elapsed2:.6f}s')
