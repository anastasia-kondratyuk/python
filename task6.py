import sys, numpy

try:
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
except:
    print('Usage: ', sys.argv[0], " infile outfile")
    sys.exit(1)

ifile = open(infilename, 'r')
ofile = open(outfilename, 'w')

for line in ifile:
    arr = numpy.array(line.split())
    arr = arr.astype(float)
    for n in arr:
        ofile.write('%12.6f ' % n)
    ofile.write(' %12.6f\n' % numpy.mean(arr))

ifile.close()
ofile.close()