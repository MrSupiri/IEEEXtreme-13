import numpy as np

cases = int(input())


def rearrange_list(data):
    changes = 0
    print(data)
    for i in np.unique(np.array(data)):
        ii = np.where(np.array(data) == i)[0]
        # print(i, ii)
        if len(ii) > 1:
            try:
                for y in range(len(ii)):
                    if ii[y] + 1 != ii[y + 1]:
                        temp = row[int(ii[y])]
                        del row[y]
                        row.insert(int(ii[y + 1]), temp)
                        changes += 1
                        break
            except IndexError:
                continue
    print(data)
    return changes, data


for _ in range(cases):
    c = 0
    row = list(input())
    if row[0] == row[-1]:
        k = 0
        while row[k] == row[k + 1]:
            k += 1
        temp_list = row[:k + 1]
        del row[:k + 1]
        row += temp_list
    coms = []
    for i in np.unique(np.array(row)):
        coms.append(len(np.where(np.array(row) == i)[0]))
    for _ in range(max(coms)):
        c_, row = rearrange_list(row)
        c += c_
    print(c)

# for _ in range(cases):
#     changes = 0
#     row = list(input())
#     if row[0] != row[1] and row[0] == row[-1]:
#         row.append(row.pop(0))
#     print(row)
#
#     while True:
#         for i in range(len(row)):
#             ii = np.where(np.array(row) == row[i])[0]
#             if len(ii) > 1:
#                     if row[i] != row[y]:
#                         row[i], row[y] = row[y], row[i]
#                         changes += 1
#     print(row)
#     print(changes)

"""
5
CBBACC
DBCA
CCACACC
ABCABCABC
ABCDABCDABCDABCD

1
ABCABCABC

"""
