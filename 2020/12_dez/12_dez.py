data = []
with open("12_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.strip('\n'))


def get_heading(heading):
    true_heading = heading % 360
    if true_heading < 45 or true_heading > 315:
        return 'N'
    elif 45 <= true_heading < 135:
        return 'E'
    elif 135 <= true_heading < 225:
        return 'S'
    elif 225 <= true_heading < 315:
        return 'W'

# puzzle 1

heading = 90
# east = +  |  west = -
# north = + | south = -
position = [0, 0]

for instruction in data:
    action, value = instruction[0], int(instruction[1:])
    if action == 'N':
        position[1] += value
    elif action == 'S':
        position[1] -= value
    elif action == 'E':
        position[0] += value
    elif action == 'W':
        position[0] -= value
    elif action == 'F':
        action = get_heading(heading)
        if action == 'N':
            position[1] += value
        elif action == 'S':
            position[1] -= value
        elif action == 'E':
            position[0] += value
        elif action == 'W':
            position[0] -= value
    elif action == 'R':
        heading += value
    elif action == 'L':
        heading -= value

print(position)
print(abs(position[0]) + abs(position[1]))

# puzzle 2

waypoint = [10, 1]
position = [0, 0]

for instruction in data:
    action, value = instruction[0], int(instruction[1:])
    if action == 'N':
        waypoint[1] += value
    elif action == 'S':
        waypoint[1] -= value
    elif action == 'E':
        waypoint[0] += value
    elif action == 'W':
        waypoint[0] -= value
    elif action == 'R':
        times = int(value / 90)
        for time in range(times):
            waypoint = waypoint[::-1]
            waypoint[1] *= -1
    elif action == 'L':
        times = int(value / 90)
        for time in range(times):
            waypoint = waypoint[::-1]
            waypoint[0] *= -1
    elif action == 'F':
        position[0] += waypoint[0] * value
        position[1] += waypoint[1] * value

print(position)
print(abs(position[0]) + abs(position[1]))
