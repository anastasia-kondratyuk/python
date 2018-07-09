from math import *
from sys import *

for n in argv[1:]:
    if float(n) > 0:
        print("ln(%d)" % float(n), " = ", log(float(n)))
    else:
        print("ln(%d)" % float(n), " is illegal")