import sys

with open(sys.argv[1]) as f:
    data = f.read().split("\n")
    times = [int(x) for x in data[0].split(":")[1].strip().split()]
    distances = [int(x) for x in data[1].split(":")[1].strip().split()]
    t_d = zip(times, distances)

    total = 1
    for t, d in t_d:
        count = 0
        for i in range(int(t / 2), 0, -1):
            if i * (t - i) <= d:
                break
            count += 1
        total *= (count * 2) - int(not (t % 2))

    print(total)
