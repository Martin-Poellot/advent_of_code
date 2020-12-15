import time
data = []
with open("11_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.strip('\n'))

# rearrange Floor to an image
import numpy as np
floor_img = np.zeros((len(data), len(data[0])))
for y, line in enumerate(data):
    for x, l in enumerate(line):
        if l == '#':
            floor_img[y, x] = 255
        elif l == 'L':
            floor_img[y, x] = 127

start_1 = time.time()
floor_state = floor_img.copy()
while 1:
    new_seat_state = np.zeros_like(floor_state)
    changes = 0
    for y, line in enumerate(floor_state):
        for x, seat in enumerate(line):
            if seat != 0:
                adjacent_occupied_seats = 0
                for pos_y in range(max(y - 1, 0), min(y + 2, len(floor_state))):
                    for pos_x in range(max(x - 1, 0), min(x + 2, len(line))):
                        if (not pos_x == x) or (not pos_y == y):
                            if floor_state[pos_y, pos_x] == 255:  # occupied
                                adjacent_occupied_seats += 1

                if seat == 127 and not adjacent_occupied_seats:
                    new_seat_state[y, x] = 255
                    changes += 1
                elif seat == 255 and adjacent_occupied_seats >= 4:
                    new_seat_state[y, x] = 127
                    changes += 1
                elif seat == 127 and adjacent_occupied_seats:
                    new_seat_state[y, x] = 127
                elif seat == 255 and adjacent_occupied_seats < 4:
                    new_seat_state[y, x] = 255
    if (floor_state == new_seat_state).all():
        break
    else:
        floor_state = new_seat_state

unique, counts = np.unique(new_seat_state, return_counts=True)
res = dict(zip(unique, counts))
elapsed1 = time.time() - start_1
print(f'Res: {res[255]}')
print(f'Elapsed Time: {elapsed1:.6f}s')

# puzzle # 2
start_2 = time.time()
floor_state = floor_img.copy()
while 1:
    new_seat_state = np.zeros_like(floor_state)
    changes = 0
    for y, line in enumerate(floor_state):
        for x, seat in enumerate(line):
            if seat != 0:
                adjacent_occupied_seats = 0
                # check 8 directions, ugly but simple
                # would also work with a set of allow directional moves e.g. [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], ...]
                # check right
                pos_x = x
                while pos_x < len(line) - 1:
                    pos_x += 1
                    if floor_state[y, pos_x] == 255:
                        adjacent_occupied_seats += 1
                        break
                    elif floor_state[y, pos_x] == 127:
                        break
                # check left
                pos_x = x
                while pos_x > 0:
                    pos_x -= 1
                    if floor_state[y, pos_x] == 255:
                        adjacent_occupied_seats += 1
                        break
                    elif floor_state[y, pos_x] == 127:
                        break
                # check top
                pos_y = y
                while pos_y > 0:
                    pos_y -= 1
                    if floor_state[pos_y, x] == 255:
                        adjacent_occupied_seats += 1
                        break
                    elif floor_state[pos_y, x] == 127:
                        break
                # check bottom
                pos_y = y
                while pos_y < len(floor_state) - 1:
                    pos_y += 1
                    if floor_state[pos_y, x] == 255:
                        adjacent_occupied_seats += 1
                        break
                    elif floor_state[pos_y, x] == 127:
                        break
                # check top right bottom
                pos_y = y
                pos_x = x
                while pos_y > 0 and pos_x < len(line) - 1:
                    pos_y -= 1
                    pos_x += 1
                    if floor_state[pos_y, pos_x] == 255:
                        adjacent_occupied_seats += 1
                        break
                    elif floor_state[pos_y, pos_x] == 127:
                        break
                # check bottom right bottom
                pos_y = y
                pos_x = x
                while pos_y < len(floor_state) - 1 and pos_x < len(line) - 1:
                    pos_y += 1
                    pos_x += 1
                    if floor_state[pos_y, pos_x] == 255:
                        adjacent_occupied_seats += 1
                        break
                    elif floor_state[pos_y, pos_x] == 127:
                        break
                # check bottom left bottom
                pos_y = y
                pos_x = x
                while pos_y < len(floor_state) - 1 and pos_x > 0:
                    pos_y += 1
                    pos_x -= 1
                    if floor_state[pos_y, pos_x] == 255:
                        adjacent_occupied_seats += 1
                        break
                    elif floor_state[pos_y, pos_x] == 127:
                        break
                # check top left bottom
                pos_y = y
                pos_x = x
                while pos_y > 0 and pos_x > 0:
                    pos_y -= 1
                    pos_x -= 1
                    if floor_state[pos_y, pos_x] == 255:
                        adjacent_occupied_seats += 1
                        break
                    elif floor_state[pos_y, pos_x] == 127:
                        break

                if seat == 127 and not adjacent_occupied_seats:
                    new_seat_state[y, x] = 255
                    changes += 1
                elif seat == 255 and adjacent_occupied_seats >= 5:
                    new_seat_state[y, x] = 127
                    changes += 1
                elif seat == 127 and adjacent_occupied_seats:
                    new_seat_state[y, x] = 127
                elif seat == 255 and adjacent_occupied_seats < 5:
                    new_seat_state[y, x] = 255

    if (floor_state == new_seat_state).all():
        break
    else:
        floor_state = new_seat_state

unique, counts = np.unique(new_seat_state, return_counts=True)
res = dict(zip(unique, counts))
elapsed2 = time.time() - start_2
print(f'Res: {res[255]}')
print(f'Elapsed Time: {elapsed2:.6f}s')
