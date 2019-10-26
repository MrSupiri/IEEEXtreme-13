import string

queries = list(map(int, input().split(' ')))

for _ in queries:
    size, index = list(map(int, input().split(' ')))
    s = string.ascii_uppercase[:size]
    prepend = ""
    for _ in range(index):
        s

