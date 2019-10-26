import numpy as np
from collections import Counter

n = int(input())

valid = [0] * n


def check_all_chars(line):
    if len(np.unique(np.array(list(line)))) == 1:
        return True
    return False


def check_lexicographically(line):
    return line == "".join(sorted(line))

def dfsgs(line):
    temp = line.copy()
    line = sorted(line)
    return temp[0] == line[0]


for i in range(n):
    std_in = input()
    if check_all_chars(std_in):
        valid[i] = 1
        continue

    for k in range(1, len(std_in)):
        if check_lexicographically(std_in[:k]) and check_lexicographically(std_in[k:]) and dfsgs([std_in[:k], std_in[k:]]):
            # print(std_in[:k], std_in[k:])
            valid[i] = 1
            continue

    # if std_in[:len(std_in) // 2] == std_in[len(std_in) // 2:]:
    #     letters = dict(Counter(std_in[:len(std_in) // 2]))
    #     l = 0
    #     for letter in sorted(letters):
    #         if l <= letters[letter]:
    #             l = letters[letter]
    #             valid[i] = 1
    #         else:
    #             valid[i] = 0
    #             break

print("".join(map(str, valid)))
