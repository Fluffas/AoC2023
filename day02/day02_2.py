import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

    ids = [int(x.split()[1]) for x in [y.split(': ')[0] for y in data]]
    cubes = [[z.split(', ') for z in x.split('; ')] for x in [y.split(': ')[1] for y in data]]
    games = dict(zip(ids, cubes))

    total = 0

    for key, val in games.items():
        max_blue = 0
        max_green = 0
        max_red = 0
        for x in val:
            for y in x:
                num, col = y.split()
                if col == 'blue' and int(num) > max_blue:
                    max_blue = int(num)
                elif col == 'green' and int(num) > max_green:
                    max_green = int(num)
                elif col == 'red' and int(num) > max_red:
                    max_red = int(num)
        total += max_blue * max_green * max_red
    print(total)
