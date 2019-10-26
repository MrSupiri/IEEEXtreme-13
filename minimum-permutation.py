list_size, set_size = list(map(int, "3 2".split(' ')))
list_ = list(map(int, "3 1 5".split(' ')))
set_ = sorted(list(map(int, "4 2".split(' '))))

# list_size, set_size = list(map(int, input().split(' ')))
# list_ = list(map(int, input().split(' ')))
# set_ = sorted(list(map(int, input().split(' '))))

for i in range(len(list_)+1):
    for y in set_:
        if list_[i] > y:
            list_.insert(i, y)
            set_.remove(y)

print(' '.join(map(str, list_)))
