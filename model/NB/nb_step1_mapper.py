#!/usr/bin/env python

#authors: Junjun Qian, Xiaoqin Zhou, Alan Ng

"""
inout:     
    ad identifier, click, hour, C1, banner_pos, site_id, site_domain, site_category, app_id, app_domian, app_category, device_id, device_ip, device_model, device_type, device_conn_type, C14-C21 
output: feature&value \t click \t impression
"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into a list of strings
    line = line.split(',')
    
    #print the value we need
    print '%s,%s' % ('ad identifier'+   line[0], line[1])
    print '%s,%s' % ('hour'+ line[2], line[1])
    print '%s,%s' % ('C1'+         line[3], line[1])
    print '%s,%s' % ('banner_pos'+     line[4], line[1])
    print '%s,%s' % ('site_id'+     line[5], line[1])
    print '%s,%s' % ('site_domain'+    line[6], line[1])
    print '%s,%s' % ('site_category'+      line[7], line[1])
    print '%s,%s' % ('app_id'+line[8], line[1])
    print '%s,%s' % ('app_domian'+       line[9], line[1])
    print '%s,%s' % ('app_category'+   line[10], line[1])
    print '%s,%s' % ('device_id'+   line[11], line[1])
    print '%s,%s' % ('device_ip'+   line[12], line[1])
    print '%s,%s' % ('device_model'+   line[13], line[1])
    print '%s,%s' % ('device_type'+   line[14], line[1])
    print '%s,%s' % ('device_conn_type'+   line[15], line[1])
    print '%s,%s' % ('C14'+   line[16], line[1])
    print '%s,%s' % ('C15'+   line[17], line[1])
    print '%s,%s' % ('C16'+   line[18], line[1])
    print '%s,%s' % ('C17'+   line[19], line[1])
    print '%s,%s' % ('C18'+   line[20], line[1])
    print '%s,%s' % ('C19'+   line[21], line[1])
    print '%s,%s' % ('C20'+   line[22], line[1])
    print '%s,%s' % ('C21'+   line[23], line[1])
