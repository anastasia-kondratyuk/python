from math import *
from sys import *

for n in range(1, len(argv)):
    if float(argv[n]) > 0:
        print("ln(%g)" % float(argv[n]), " = ", log(float(argv[n])))
    else:
        print("ln(%g)" % float(argv[n]), " is illegal")
