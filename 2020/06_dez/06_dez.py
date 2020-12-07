data = []
with open("06_dez_input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append(line)


people_vote = ''
all_vote = []
counts = 0
alphabet = sorted('abcdefghijklmnopqrstuvwxyz')
for vote in data:
    if vote == '\n':
        all_choices = alphabet.copy()
        for v in all_vote:
            for c in alphabet:
                if c not in v:
                    if c in all_choices:
                        all_choices.remove(c)
        all_vote = []
        counts += len(all_choices)
    else:
        for choice in vote.split('\n')[0]:
            people_vote += choice
        all_vote.append(people_vote)
        people_vote = ''
all_choices = alphabet.copy()
for v in all_vote:
    for c in alphabet:
        if c not in v:
            if c in all_choices:
                all_choices.remove(c)
counts += len(all_choices)
print(counts)
