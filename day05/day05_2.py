import sys


def find_in_maps(curr_r, maps, i=0):
    if i >= len(maps):
        return min([x.start for x in curr_r])

    next_r = []
    remaining_r = curr_r

    for m in maps[i]:
        if not remaining_r:
            break

        source_r = range(m[1], m[1] + m[2])
        dest_r = range(m[0], m[0] + m[2])

        new_remaining_r = []

        for xr in remaining_r:
            # if overlapping
            if xr.start <= source_r.stop and xr.stop >= source_r.start:
                overlap = range(
                    max(xr.start, source_r.start), min(xr.stop, source_r.stop)
                )
                next_r.append(
                    range(
                        overlap.start + dest_r.start - source_r.start,
                        overlap.stop + dest_r.stop - source_r.stop,
                    )
                )

                # get above range
                if overlap.stop < xr.stop:
                    above_range = range(overlap.stop, xr.stop)
                    new_remaining_r.append(above_range)

                # get under range
                if overlap.start > xr.start:
                    below_range = range(xr.start, overlap.start)
                    new_remaining_r.append(below_range)

            else:
                new_remaining_r.append(xr)

        remaining_r = new_remaining_r

    next_r += remaining_r
    return find_in_maps(next_r, maps, i + 1)


with open(sys.argv[1]) as f:
    data = f.read().split("\n\n")

    initial_seeds = [int(s) for s in data[0].split(": ")[1].split()]

    seed_ranges = []
    for i in range(0, len(initial_seeds), 2):
        seed_ranges.append(
            range(initial_seeds[i], initial_seeds[i] + initial_seeds[i + 1])
        )

    maps = []
    for d in data[1:]:
        maps.append(
            [[int(x) for x in y.split()] for y in d.split(":\n")[1].splitlines()]
        )

    results = []
    for sr in seed_ranges:
        results.append(find_in_maps([sr], maps))

    print(min(results))
