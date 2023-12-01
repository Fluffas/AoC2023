import sys


def find_digit(line, sequence):
    for i in sequence:
        if line[i].isdigit():
            return line[i]
        else:
            for word, num in spelled_out.items():
                if line[i:].startswith(word):
                    return spelled_out[word]


with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    spelled_out = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    sum = 0

    for line in data:
        sum += int(find_digit(line, range(len(line))) + find_digit(line, reversed(range(len(line)))))

    print(sum)
