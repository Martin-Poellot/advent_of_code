import time

rules = []
to_rules = True
other_tickets = []
to_other_tickets = False
my_ticket = []
to_my_ticket = False

with open("16_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line == '\n' and to_rules:
            to_my_ticket = True
            to_rules = False
            continue
        elif line == '\n' and to_my_ticket:
            to_my_ticket = False
            to_other_tickets = True
            continue
        if to_rules:
            rules.append(line.strip('\n'))
        elif to_my_ticket:
            my_ticket.append(line.strip('\n'))
        elif to_other_tickets:
            other_tickets.append(line.strip('\n'))

my_ticket = list(map(int, my_ticket[1].split(',')))
other_tickets = other_tickets[1:]

# Puzzle 1:
start_1 = time.time()
ticket_scanning_error_rate = 0
allowed_nrs = []
# gather rulez
for rule in rules:
    name, rest = rule.split(': ')
    first_r, second_r = rest.split(' or ')
    first_lower, first_upper = first_r.split('-')
    second_lower, second_upper = second_r.split('-')
    allowed_nrs += list(range(int(first_lower), int(first_upper) + 1))
    allowed_nrs += list(range(int(second_lower), int(second_upper) + 1))

other_tickets = [list(map(int, t.split(','))) for t in other_tickets]

# check nearby tickets:
valid_tickets = []
for ticket in other_tickets:
    if not set(ticket).issubset(allowed_nrs):
        for nr in ticket:
            if nr not in allowed_nrs:
                ticket_scanning_error_rate += nr
    else:
        valid_tickets.append(ticket)
elapsed1 = time.time() - start_1
print(f"Result 1: {ticket_scanning_error_rate}")
print(f'Elapsed Time: {elapsed1:.6f}s')

# Puzzle 2:
start_2 = time.time()
# rearrange rules
ticket_rules = {}
for rule in rules:
    name, rest = rule.split(': ')
    first_r, second_r = rest.split(' or ')
    first_lower, first_upper = first_r.split('-')
    second_lower, second_upper = second_r.split('-')
    ticket_rules[name] = list(range(int(first_lower), int(first_upper) + 1))
    ticket_rules[name] += list(range(int(second_lower), int(second_upper) + 1))

possible_fields = {}
for pos in range(len(my_ticket)):
    field_order = []
    values = [entry[pos] for entry in valid_tickets]
    values.append(my_ticket[pos])
    for rule in ticket_rules.items():
        valid_numbers = rule[1]
        rule_name = rule[0]
        if set(values).issubset(valid_numbers):
            field_order.append(rule_name)
    possible_fields[pos] = field_order

correct_fields = []
while len(correct_fields) < 20:
    possibilities = []
    for x in possible_fields.items():
        possibilities.append(len(x[1]))
    q = possibilities.index(1)
    correct_fields.append([q, possible_fields[q].copy()])
    for x in possible_fields.items():
        if correct_fields[-1][1][0] in x[1]:
            possible_fields[x[0]].remove(correct_fields[-1][1][0])

mults = []
for correct_pos, field in correct_fields:
    if 'departure' in field[0]:
        mults.append(my_ticket[correct_pos])

# thx numpy...
prod = mults[0]
for p in mults[1:]:
    prod *= p

elapsed2 = time.time() - start_2
print(f"Result 2: {prod}")
print(f'Elapsed Time: {elapsed2:.6f}s')