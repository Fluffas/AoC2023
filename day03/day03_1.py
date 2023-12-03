import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

    total = 0

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

                adj = []
                for i in range(max(0, y - 1), min(len(data) - 1, y + 1) + 1):
                    for j in range(
                        max(0, startpos - 1), min(len(data[y]) - 1, endpos + 1) + 1
                    ):
                        if not data[i][j].isnumeric() and data[i][j] != ".":
                            adj.append(data[i][j])

                if adj:
                    total += int(num)

                startpos = 0
                endpos = 0
                num = ""

            elif data[y][x].isnumeric():
                num += data[y][x]
                endpos = x
                if startpos == 0:
                    startpos = x

    print(total)
