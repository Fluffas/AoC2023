import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    cards = [([int(x) for x in z[0].split(': ')[1].split()], [int(x) for x in z[1].split()]) for z in [y.split(' | ') for y in data]]
    ids = range(1, len(cards) + 1)
    d = dict(zip(ids, cards))

    bonus = dict.fromkeys(ids, 1)

    for i, (winners, numbers) in d.items():
        points = 0

        for n in numbers:
            if n in winners:
                points += 1

        for p in range(1, points + 1):
            if i + p <= len(d):
                bonus[i + p] += 1 * bonus[i]

    print(sum(bonus.values()))
