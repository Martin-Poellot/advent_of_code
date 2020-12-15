import time
data = []
with open("05_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.split('\n')[0])

data1 = ['BFFFBBFRRR',
         'FFFBBBFRRR',
         'BBFFBBFRLL']
# part 1
start_1 = time.time()
seat_ids = []
for boarding_pass in data:
    row = 0
    for i, char in enumerate(reversed(boarding_pass[:-3])):
        if char == 'B':
            row += 2**i
    seat = 0
    for j, char in enumerate(reversed(boarding_pass[-3:])):
        if char == 'R':
            seat += 2**j
    seat_id = 8 * row + seat
    seat_ids.append(seat_id)

elapsed1 = time.time() - start_1
print(f'Result 1: {max(seat_ids)}')
print(f'Elapsed Time: {elapsed1:.6f}s')
# part 2
start_2 = time.time()
seats = list(range(9, 960))
sorted_seats = sorted(seat_ids)
for i, seat_id in enumerate(sorted_seats):
    if 8 < seat_id < 960:
        seats.pop(seats.index(seat_id))
elapsed2 = time.time() - start_2
print(f'Result 2: {seats[0]}')
print(f'Elapsed Time: {elapsed2:.6f}s')
