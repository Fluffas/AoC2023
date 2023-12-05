import sys


def find_in_maps(x, maps, i):
    if i >= len(maps):
        return x

    for m in maps[i]:
        if x in range(m[1], m[1] + m[2]):
            x = x + m[0] - m[1]
            break

    return find_in_maps(x, maps, i + 1)


with open(sys.argv[1]) as f:
    data = f.read().split("\n\n")

    initial_seeds = [int(s) for s in data[0].split(": ")[1].split()]

    maps = []
    for d in data[1:]:
        maps.append(
            [[int(x) for x in y.split()] for y in d.split(":\n")[1].splitlines()]
        )

    results = []
    for s in initial_seeds:
        results.append(find_in_maps(s, maps, 0))

    print(min(results))
