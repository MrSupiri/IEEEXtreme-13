# std_in = list(map(int, "10 6 9".split(' ')))
std_in = list(map(int, "1243523 1325443234 1325443234".split(' ')))
# std_in = list(map(int, input().split(' ')))
n, a, b = std_in
max_ = max(a, b)
min_ = min(a, b)

from time import time

start_time = time()

try:
    seq = [max_] * ((n // max_) + 1)
except:
    print("NO")
    exit(0)

for y in range(len(seq)):
    seq[y] = 0
    sum__ = sum(seq)
    seq[y] = max(min_, n - sum__)
    if sum__ + seq[y] == n:
        print("YES")
        print(' '.join(map(str, seq)))
        print(time() - start_time)
        exit(0)
    if time() - start_time > 700:
        break
print("NO")
print(time() - start_time)
