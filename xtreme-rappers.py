import itertools
import numpy as np
std_in = list(map(int, "4 3".split(' ')))

a, b = std_in
a_1 = list(range(1, (a//3)+1))
a_2 = list(range((a//3)+1, (a//3) + (a//3) + 1))
a_3 = list(range((a//3)+1 + (a//3), a+1))
b_1 = list(range(1, (b//3)+1))
b_2 = list(range((b//3)+1, (b//3) + (b//3) + 1))
b_3 = list(range((b//3)+1 + (b//3), b+1))
if a == 0 or b == 0:
    print(0)
else:
    dsf = np.array(list(itertools.product(a_1, a_2, a_3, b_1, b_2, b_3)))
    print(len(dsf))
