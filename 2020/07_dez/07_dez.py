import time
bags = []
with open("07_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        bag = {}
        target, roooots = line.split('contain')[0], line.split('contain')[1:]
        color_target = target.split('bags')[0][:-1]
        roots = roooots[0].split(' bag')
        prefix = []
        for root in roots:
            res = root.split(',')
            for r in res:
                if len(r) > 5:
                    if not 'no other' in r:
                        nr, c1, c2 = r.split(' ')[1], r.split(' ')[2], r.split(' ')[3]
                        prefix.append([int(nr), f'{c1} {c2}'])
        bag['target_color'] = color_target
        bag['roots'] = prefix
        bags.append(bag)

# Puzzle 1: counting up from the root to the target
start_1 = time.time()
possible_bags = []
for bag in bags:
    for root in bag['roots']:
        if 'shiny gold' in root:
            possible_bags.append(bag['target_color'])

for possible_bag in possible_bags:
    for bag in bags:
        for root in bag['roots']:
            if possible_bag in root:
                possible_bags.append(bag['target_color'])

elapsed1 = time.time() - start_1
print(f'Result 1: {len(set(possible_bags))}')
print(f'Elapsed Time: {elapsed1:.6f}s')

# Puzzle 2: counting down the roots
start_2 = time.time()
counter = 0
for bag in bags:
    if bag['target_color'] == 'shiny gold':
        bags_included = bag['roots']
        while len(bags_included) > 0:
            processed_bag = bags_included.pop()
            [nr_of_bags, color] = processed_bag
            processed = False
            for bag in bags:
                if bag['target_color'] == color:
                    bag_2 = []
                    for [b_nr, c] in bag['roots']:
                        bag_2.append([b_nr * nr_of_bags, c])
                    bags_included += bag_2
                    processed = True
                if processed:
                    counter += nr_of_bags
                    break
elapsed2 = time.time() - start_2
print(f'Result 2: {counter}')
print(f'Elapsed Time: {elapsed2:.6f}s')
