bags = []
with open("07_dez_input2.txt", 'r') as f:
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

print(bags)

# Puzzle 1: counting up from the root to the target
possible_bags = []
for bag in bags:
    for root in bag['roots']:
        if 'shiny gold' in root:
            print(bag)
            possible_bags.append(bag['target_color'])

for possible_bag in possible_bags:
    for bag in bags:
        for root in bag['roots']:
            if possible_bag in root:
                possible_bags.append(bag['target_color'])

print(f'Result 1: {len(set(possible_bags))}')

# Puzzle 2: counting down the roots
counter = 0
for bag in bags:
    if bag['target_color'] == 'shiny gold':
        bags_included = bag['roots']
        print(bag['roots'])
        while len(bags_included) > 0:
            processed_bag = bags_included.pop()
            [nr_of_bags, color] = processed_bag
            processed = False
            for bag in bags:
                if bag['target_color'] == color:
                    for i, [b_nr, c] in enumerate(bag['roots']):
                        bag['roots'][i] = [b_nr * nr_of_bags, c]
                    bags_included += bag['roots']
                    processed = True
                if processed:
                    counter += nr_of_bags
                    print(f'Adding {nr_of_bags}')
                    break
print(f'Result 2: {counter}')
