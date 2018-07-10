from random import *
n = 10000
m = 0
for _ in range(n - 1):
    a = randint(1, 6)
    b = randint(1, 6)
    c = randint(1, 6)
    d = randint(1, 6)
    s = a + b + c + d
    if (s) < 9:
        m += 1
print(m/n)