from math import *
from sys import *

n = 1
while 1:
    try:
        if float(argv[n]) > 0:
            print("ln(%g)" % float(argv[n]), " = ", log(float(argv[n])))
        else:
            print("ln(%g)" % float(argv[n]), " is illegal")
        n += 1
    except:
        break
