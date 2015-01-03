# quantifying hour

import sys

for line in sys.stdin:

    line = line.strip()
    line = line.split("\t")
    if sys.argv[1] == 'day':
    	print '%s,%s' % (line[0][4:6], line[1])
    elif sys.argv[1] == 'hour':
        print '%s,%s' % (((float(line[0][6:])+0.5)/24), line[1])
    else:
    	print '%s,%s,%s' % (line[0][4:6], ((float(line[0][6:])+0.5)/24), line[1])

