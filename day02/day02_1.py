import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

    ids = [int(x.split()[1]) for x in [y.split(': ')[0] for y in data]]
    cubes = [[z.split(', ') for z in x.split('; ')] for x in [y.split(': ')[1] for y in data]]
    games = dict(zip(ids, cubes))

    total = 0
    lim_blue = 14
    lim_green = 13
    lim_red = 12

    for key, val in games.items():
        impossible = False
        for x in val:
            for y in x:
                num, col = y.split()
                if col == 'blue' and int(num) > lim_blue:
                    impossible = True
                elif col == 'green' and int(num) > lim_green:
                    impossible = True
                elif col == 'red' and int(num) > lim_red:
                    impossible = True
        if not impossible:
            total += key
    print(total)
