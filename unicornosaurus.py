import numpy as np
import itertools

n_sections_broken, n_possible_fixes, IDK = list(map(int, input().split(' ')))
sections_broken = []
possible_fixes = []
power_construction = []

for _ in range(n_sections_broken):
    sections_broken.append(tuple(map(int, input().split(' '))))

for _ in range(n_possible_fixes):
    possible_fixes.append((list(map(int, input().split(' ')))))

within_range = []

for possible_fix in possible_fixes:
    for section in sections_broken:
        if possible_fix[0] <= section[0] or possible_fix[1] >= section[1]:
            within_range.append(possible_fix)

within_range = sorted(within_range)

for i in range(len(within_range)):
    for y in range(i, len(within_range)):
        try:
            if within_range[i][0] < within_range[y][0] and within_range[i][1] > within_range[y][1]:
                within_range.remove(within_range[y])
        except IndexError:
            continue

within_range = list(itertools.product(within_range, within_range))

within_range = list(dict.fromkeys(map(str, within_range)))
within_range = list(map(eval, within_range))

for i in range(len(within_range)):
    if within_range[i][0] == within_range[i][1]:
        within_range[i] = tuple(within_range[i][0])
    else:
        within_range[i] = min(within_range[i][0][0] , within_range[i][1][0]), max(within_range[i][0][1], within_range[i][1][1]), \
                           (within_range[i][0][2] + within_range[i][1][2])

within_range = sorted(within_range)
# print(within_range)


power_need = []
found_start = False
section_x = min(sections_broken)[0]
section_y = max(sections_broken)[1]

# print(section_x, section_y)

completed = False
for i in range(len(within_range)):
    if within_range[i][0] <= section_x and within_range[i][1] >= section_y:
        if found_start:
            power_need.pop()
        power_need.append(within_range[i][2])
        completed = True
        found_start = False
        break
    elif not found_start and within_range[i][0] <= section_x:
        power_need.append(within_range[i][2])
        found_start = True
    elif found_start and within_range[i][1] >= section_y:
        found_start = False
        completed = True
        break
if not completed:
    print(-1)
else:
    print(-1)
"""
1 3 15
5 10
3 7 2
6 12 5
2 11 6


2 4 15
3 7
9 10
2 6 10
3 9 15
5 12 13
8 10 30

"""
