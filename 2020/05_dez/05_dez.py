data = []
with open("05_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.split('\n')[0])

data1 = ['BFFFBBFRRR',
         'FFFBBBFRRR',
         'BBFFBBFRLL']
# part 1
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

print(f'Result 1: {max(seat_ids)}')

# part 2
seats = list(range(9, 960))
sorted_seats = sorted(seat_ids)
for i, seat_id in enumerate(sorted_seats):
    if 8 < seat_id < 960:
        seats.pop(seats.index(seat_id))

print(f'Result 2: {seats}')
