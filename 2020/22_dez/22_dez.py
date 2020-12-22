import time

player1 = True
deck1 = []
deck2 = []

#with open("22_dez_input.txt", 'r') as f:
with open("Markus_Input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines[1:]:
        if "Player" in line:
            player1 = False
            continue
        elif line == "\n":
            continue
        else:
            if player1:
                deck1.append(int(line))
            else:
                deck2.append(int(line))

# puzzle 1
start_1 = time.time()
while (len(deck1) > 0) and (len(deck2) > 0):
    p1, p2 = deck1.pop(0), deck2.pop(0)
    if p1 > p2:
        deck1 += [p1, p2]
    else:
        deck2 += [p2, p1]

winner_deck = deck1 or deck2
score = 0
for i, card_value in enumerate(reversed(winner_deck)):
    score += (i + 1) * card_value
elapsed1 = time.time() - start_1
print(f'Result1: {score}')
print(f'Elapsed Time: {elapsed1:.6f}s')

# puzzle 2
player1 = True
deck1 = []
deck2 = []

with open("22_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines[1:]:
        if "Player" in line:
            player1 = False
            continue
        elif line == "\n":
            continue
        else:
            if player1:
                deck1.append(int(line))
            else:
                deck2.append(int(line))

# recursion, so we need a function :D
start_2 = time.time()


def recursive_combat(depth, deck1, deck2):
    played_hands1 = {}
    played_hands2 = {}
    turn = 1
    while 1:
        if len(deck1) < 1:
            if depth == 1:
                return deck2
            else:
                return 2
        if len(deck2) < 1:
            if depth == 1:
                return deck1
            else:
                return 1
        p1, p2 = deck1[0], deck2[0]
        deck1 = deck1[1:]
        deck2 = deck2[1:]
        if (len(deck1) >= p1) and (len(deck2) >= p2):
            winner = recursive_combat(depth + 1, deck1[:p1], deck2[:p2])
        else:
            winner = 1 if p1 > p2 else 2
        if winner == 1:
            deck1 += [p1, p2]
        else:
            deck2 += [p2, p1]
        for i in range(1, turn):
            if (played_hands1[i] == deck1) or (played_hands2[i] == deck2):
                return 1
        played_hands1[turn] = deck1
        played_hands2[turn] = deck2
        turn += 1


winner_deck = recursive_combat(1, deck1, deck2)

score = 0
for i, card_value in enumerate(reversed(winner_deck)):
    score += (i + 1) * card_value
elapsed2 = time.time() - start_2
print(f'Result2: {score}')
print(f'Elapsed Time: {elapsed2:.6f}s')
