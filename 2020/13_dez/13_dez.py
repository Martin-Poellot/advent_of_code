import time
data = []
with open("13_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.strip('\n'))

# puzzle part 1
import numpy as np
start_1 = time.time()
earliest_departure_time = int(data[0])
bus_frequencies = data[1].split(',')
min_wait_time = np.Inf
min_wait_bus = 0
for bus in bus_frequencies:
    if bus != 'x':
        wait_time = -(earliest_departure_time % int(bus) - int(bus))
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            min_wait_bus = int(bus)

elapsed1 = time.time() - start_1
print(min_wait_time * min_wait_bus)
print(f'Elapsed Time: {elapsed1:.6f}s')

# puzzle part 2 (this works theoretically, but has too long run time...)
if 0:
    offsets = []
    busses = []
    #bus_frequencies = ['17', 'x', '13', '19']  # 3417
    #bus_frequencies = ['67', '7', '59', '61']  # 754018
    #bus_frequencies = ['67', 'x', '7', '59', '61']  # 779210

    for i, bus in enumerate(bus_frequencies):
        if bus != 'x':
            offsets.append(i)
            busses.append(int(bus))
    offset_bus_list = list(zip(offsets, busses))

    actual_offset = np.zeros(len(offsets))

    t = 99999999999998
    t = 0
    while not (np.array(actual_offset) == np.array(offsets)).all():
        t += busses[0]
        #t += max(busses)
        actual_offset = [bus - (t % bus) for bus in busses]
        #actual_offset[busses.index(max(busses))] = 0
        actual_offset[0] = 0
        break
    print(t)

# puzzle 2
start_2 = time.time()
t = 0
busses = ['x' if b == 'x' else int(b) for b in data[1].split(",")]
look_up = {bus: -i % bus for i, bus in enumerate(busses) if bus != 'x'}
differences = list(reversed(sorted(look_up)))
difference = look_up[differences[0]]
d = differences[0]
for bus in differences[1:]:
    while difference % bus != look_up[bus]:
        difference += d
    d *= bus
elapsed2 = time.time() - start_2
print(difference)
print(f'Elapsed Time: {elapsed2:.6f}s')
