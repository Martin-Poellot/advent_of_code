import time

# puzzle 2


class CupRing:
    def __init__(self, value):
        self.value = value
        self.connection_left = None
        self.connection_right = None


start_2 = time.time()
my_input = '942387615'
input_list = [int(x) for x in my_input]

for x in range(10, 1000001):
    input_list.append(x)

cups = {}
last_cup = None

for i in input_list:
    curr_cup = CupRing(i)
    cups[i] = curr_cup

    if last_cup is not None:
        last_cup.connection_right = curr_cup
        curr_cup.connection_left = last_cup
    last_cup = curr_cup

pointer = cups[input_list[0]]
last_cup.connection_right = pointer
pointer.connection_left = last_cup

pointer = cups[input_list[0]]

for i in range(10000000):
    current_cup_value = pointer.value
    cup1 = pointer.connection_right
    cup2 = cup1.connection_right
    cup3 = cup2.connection_right

    pointer.connection_right = cup3.connection_right
    pointer.connection_right.connection_left = pointer

    dest_cup_value = current_cup_value - 1 or 1000000
    while dest_cup_value in (cup1.value, cup2.value, cup3.value):
        dest_cup_value = dest_cup_value - 1 or 1000000

    dest_cup = cups[dest_cup_value]

    cup3.connection_right = dest_cup.connection_right
    cup3.connection_right.connection_left = cup3
    dest_cup.connection_right = cup1
    cup1.connection_left = dest_cup

    pointer = pointer.connection_right

while pointer.value != 1:
    pointer = pointer.connection_right

result = pointer.connection_right.value * pointer.connection_right.connection_right.value
elapsed2 = time.time() - start_2
print(f'Result 2: {result}')
print(f'Elapsed Time: {elapsed2:.6f}s')
