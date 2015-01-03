# quantifying hour

import sys

for line in sys.stdin:

    line = line.strip()
    line = line.split("\t")
    print '%s,%s' % (line[1], (float(line[0][6:])+0.5)/24)