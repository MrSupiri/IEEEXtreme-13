import itertools

test_case = int(input())

for _ in range(test_case):
    budget = int(input())
    n_items = int(input())
    item_per_category = input()
    items = []

    for i in range(n_items):
        items.append(list(map(int, input().split(' '))))

    com = {}

    for i in itertools.product(*items):
        print(i)

    best_value = 0
    # for i in np.product(*items):
    #     sum_ = sum(i)
    #     if budget >= sum_ > best_value:
    #         best_value = sum_
    #         if sum_ == budget:
    #             break
    print(best_value)



"""
1
50
4
3 2 1 2
15 10 49
11 17
10
13 23



"""