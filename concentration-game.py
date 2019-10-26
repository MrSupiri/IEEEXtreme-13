from collections import defaultdict
from random import sample, choice

N = int(input())

sample_space = list(range(1, (N * 2)+1))
known_cards = {}

moves = []

c1, c2 = sample(sample_space, k=2)
sample_space.remove(c1)
sample_space.remove(c2)


for i in range((N * 2)):
    try:
        print("{} {}".format(c1, c2), flush=True)
        isMatched = False
        std_in = input()
        if std_in == "MATCH":
            if c1 in known_cards:
                del known_cards[c1]
            if c2 in known_cards:
                del known_cards[c2]
            if c1 in sample_space:
                sample_space.remove(c1)
            if c2 in sample_space:
                sample_space.remove(c2)
            if c1 in moves:
                moves.remove(c1)
            if c2 in moves:
                moves.remove(c2)
        elif std_in == "-1":
            break
        else:
            moves.append(c1)
            moves.append(c2)
            values = list(map(int, std_in.split(" ")))
            known_cards[c1] = values[0]
            known_cards[c2] = values[1]

        v = defaultdict(list)

        for key, value in sorted(known_cards.items()):
            v[value].append(key)
        for l in v:
            if len(v[l]) >= 2:
                c1 = v[l][0]
                c2 = v[l][1]
                isMatched = True
                break
        if not isMatched:
            if len(sample_space) == 1:
                try:
                    c1 = moves[-1]
                except IndexError:
                    c1 = choice(sample_space)
                    sample_space.remove(c1)
                c2 = choice(sample_space)
                sample_space.remove(c2)
            elif len(sample_space) >= 2:
                c1 = choice(sample_space)
                sample_space.remove(c1)
                c2 = choice(sample_space)
                sample_space.remove(c2)
            else:
                c1 = choice(moves)
                moves.remove(c1)
                c2 = choice(moves)
                moves.remove(c2)
    except:
        break

print("-1")
