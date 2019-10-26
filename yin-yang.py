import random

n = int(input())

n_y = random.randint(1, n//1.5)
n_Y = n - n_y

output = list("y" * n_y + "Y" * n_Y)

random.shuffle(output)
print("".join(output))
