import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

    total = 0
    gears = {}

    for y in range(len(data)):
        num = ""
        startpos = 0
        endpos = 0
        for x in range(len(data[y])):
            if (not data[y][x].isnumeric() and num != "") or (
                x == len(data[y]) - 1 and data[y][x].isnumeric()
            ):
                if data[y][x].isnumeric():
                    num += data[y][x]
                    endpos = x

                for i in range(max(0, y - 1), min(len(data) - 1, y + 1) + 1):
                    for j in range(
                        max(0, startpos - 1), min(len(data[y]) - 1, endpos + 1) + 1
                    ):
                        if data[i][j] == "*":
                            if (i, j) in gears:
                                gears[(i, j)].append(int(num))
                            else:
                                gears[(i, j)] = [int(num)]

                startpos = 0
                endpos = 0
                num = ""

            elif data[y][x].isnumeric():
                num += data[y][x]
                endpos = x
                if startpos == 0:
                    startpos = x

    for key, val in gears.items():
        if len(val) == 2:
            total += val[0] * val[1]

    print(total)
