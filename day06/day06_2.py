import sys

with open(sys.argv[1]) as f:
    data = f.read().split("\n")
    t = int("".join([x for x in data[0].split(":")[1].strip().split()]))
    d = int("".join([x for x in data[1].split(":")[1].strip().split()]))

    count = 0
    for i in range(int(t / 2), 0, -1):
        if i * (t - i) <= d:
            break
        count += 1

    count = (count * 2) - int(not (t % 2))
    print(count)
