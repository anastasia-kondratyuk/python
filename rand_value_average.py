from random import *
from sys import *
import numpy

n = int(argv[1])
average = []
for _ in range(n):
    average.append(uniform(-1, 1))
    print('%.4f' % average[-1])
print("Average:", '%.4f' % numpy.mean(average))