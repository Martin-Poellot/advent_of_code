import time
data = []
valid = 0
v = 0

with open("02_dez_input.txt", 'r') as f:
    lines = f.readlines()
    start_1 = time.time()
    for line in lines:
        part1, pw = line.split(':')
        freq, letter = part1.split(' ')
        min_freq, max_freq = freq.split('-')
        data.append([min_freq, max_freq, letter, pw])
        c = pw.count(letter)
        if int(min_freq) <= c <= int(max_freq):
            valid += 1
elapsed1 = time.time() - start_1
print(f'Result 1: {valid}')
print(f'Elapsed Time: {elapsed1:.6f}s')

with open("02_dez_input.txt", 'r') as f:
    lines = f.readlines()
    start_2 = time.time()
    for line in lines:
        part1, pw = line.split(':')
        freq, letter = part1.split(' ')
        min_freq, max_freq = freq.split('-')
        data.append([min_freq, max_freq, letter, pw])
        c = pw.count(letter)
        l1 = pw[int(min_freq)]
        l2 = pw[int(max_freq)]
        if l1 is letter or l2 is letter:
            if l1 is not l2:
                if l1 is letter:
                    v += 1
                elif l2 is letter:
                    v += 1
elapsed2 = time.time() - start_2
print(f'Result 2: {v}')
print(f'Elapsed Time: {elapsed2:.6f}s')
