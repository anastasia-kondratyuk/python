import sys, math

try:
    outfilename = sys.argv[1]
except:
    print('Usage: ', sys.argv[0], ' outfile')
    sys.exit(1)

ofile = open(outfilename, 'w')


def myfunc(y):
    if y >= 0.0:
        return y ** 5 * math.exp(-y)
    else:
        return 0.0

n = 2
while n <= len(sys.argv) - 1:
    x = float(sys.argv[n])
    y = float(sys.argv[n+1])
    fy = myfunc(y)
    ofile.write('%g %12.5e\n' % (x, fy))
    n += 2
ofile.close()
