import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    cards = [([int(x) for x in z[0].split(': ')[1].split()], [int(x) for x in z[1].split()]) for z in [y.split(' | ') for y in data]]

    total = 0

    for winners, numbers in cards:
        points = 0
        for n in numbers:
            if n in winners:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        total += points

    print(total)
