data = [2, 0, 1, 9, 5, 19]
#data = [0, 3, 6]  # 436
#data = [1, 3, 2]  # 1
#data = [2, 1, 3]  # 10

numbers_spoken = {}
last_number_spoken = data[-1]
all_spoken_numbers = data.copy()

for i in range(0, 30000000):
    if i < len(data):
        numbers_spoken[all_spoken_numbers[i]] = [i]
    else:
        current_number = all_spoken_numbers[-1]
        if current_number in numbers_spoken.keys():
            if len(numbers_spoken[current_number]) < 2:
                if 0 in numbers_spoken.keys():
                    numbers_spoken[0].append(i)
                else:
                    numbers_spoken[0] = [i]
                all_spoken_numbers.append(0)
            else:
                last_call = numbers_spoken[current_number][-1]
                the_call_before = numbers_spoken[current_number][-2]
                diff = last_call - the_call_before
                all_spoken_numbers.append(diff)
                if diff in numbers_spoken.keys():
                    numbers_spoken[diff].append(i)
                    numbers_spoken[diff] = numbers_spoken[diff][-2:]
                else:
                    numbers_spoken[diff] = [i]
        else:
            numbers_spoken[all_spoken_numbers[i]] = [i]
    if i == 2019:
        print(f'Puzzle 1 answer after 2020: {all_spoken_numbers[i]}')
    if i % 1000000 == 0:
        print(f'Progress: {float((i + 1) / 30000000) * 100:.2f}%')

print(f'Puzzle 2 answer after 2020: {all_spoken_numbers[i]}')
