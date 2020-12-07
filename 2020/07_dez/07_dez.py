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

print(bags)

possible_bags = []
for bag in bags:
    for root in bag['roots']:
        if 'shiny gold' in root:
            print(bag)
            possible_bags.append(bag['target_color'])

print(possible_bags)
