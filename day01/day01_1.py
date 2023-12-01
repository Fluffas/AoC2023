import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    sum = 0

    for line in data:
        digits = [x for x in list(line) if x.isdigit()]
        if digits:
            sum += int(digits[0] + digits[-1])

    print(sum)
