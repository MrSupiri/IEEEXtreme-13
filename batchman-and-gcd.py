# import math
#
# size, max_size = list(map(int, input().split(' ')))
# data = list(map(int, input().split(' ')))
#
# gces = {}
#
# for i in range(size + 1):
#     for j in range(i + 1, size + 1):
#         if j - i > max_size:
#             break
#         sub = data[i:j]
#         # print(sub)
#         gces[math.gcd(sub[0], sub[-1])] = None
# print(len(gces.keys()))

import math

size, max_size = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

gces = {}

for i in range(size + 1):
    for j in range(i + 1, size + 1):
        if j - i > max_size:
            break
        sub = data[i:j]
        print(sub)
        gces[math.gcd(sub[0], sub[-1])] = None
print(len(gces.keys()))















import math
import numpy as np

size, max_size = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

# gces = []
# mid_value = (size // 2)
# even = size % 2 == 0
# for i in range(size):
#     gces.append(math.gcd(data[i], data[i]))
#     # if not even and i == mid_value:
#     #     gces.append(math.gcd(data[i], data[-1]))
#     # else:
#     gces.append(math.gcd(data[i], data[-i - 1]))
#
# print(len(np.unique(np.array(gces))))
