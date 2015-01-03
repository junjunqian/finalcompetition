#!/usr/bin/env python

#authors: Junjun Qian, Xiaoqin Zhou, Alan Ng
"""
inout:     
    ad identifier, click, hour, C1, banner_pos, site_id, site_domain, site_category, app_id, app_domian, app_category, device_id, device_ip, device_model, device_type, device_conn_type, C14-C21 
output: 
    feature, click
"""

import sys

for line in sys.stdin:
    
    line = line.strip()
    line = line.split(",")
    #depend on your chose
    if sys.argv[1] == 'ad identifier':
        print '%s\t%s' % (line[0], line[1])
    elif sys.argv[1] == 'hour':
        print '%s\t%s' % (line[2], line[1])
    elif sys.argv[1] == 'C1':
        print '%s\t%s' % (line[3], line[1])
    elif sys.argv[1] == 'banner_pos':
        print '%s\t%s' % (line[4], line[1])
    elif sys.argv[1] == 'site_id':
        print '%s\t%s' % (line[5], line[1])
    elif sys.argv[1] == 'site_domain':
        print '%s\t%s' % (line[6], line[1])
    elif sys.argv[1] == 'site_category':
        print '%s\t%s' % (line[7], line[1])
    elif sys.argv[1] == 'app_id':
        print '%s\t%s' % (line[8], line[1])
    elif sys.argv[1] == 'app_domian':
        print '%s\t%s' % (line[9], line[1])
    elif sys.argv[1] == 'app_category':
        print '%s\t%s' % (line[10], line[1])
    elif sys.argv[1] == 'device_id':
        print '%s\t%s' % (line[11], line[1])
    elif sys.argv[1] == 'device_ip':
        print '%s\t%s' % (line[12], line[1])
    elif sys.argv[1] == 'device_model':
        print '%s\t%s' % (line[13], line[1])
    elif sys.argv[1] == 'device_type':
        print '%s\t%s' % (line[14], line[1])
    elif sys.argv[1] == 'device_conn_type':
        print '%s\t%s' % (line[15], line[1])
    elif sys.argv[1] == 'C14':
        print '%s\t%s' % (line[16], line[1])
    elif sys.argv[1] == 'C15':
        print '%s\t%s' % (line[17], line[1])
    elif sys.argv[1] == 'C16':
        print '%s\t%s' % (line[18], line[1])
    elif sys.argv[1] == 'C17':
        print '%s\t%s' % (line[19], line[1])
    elif sys.argv[1] == 'C18':
        print '%s\t%s' % (line[20], line[1])
    elif sys.argv[1] == 'C19':
        print '%s\t%s' % (line[21], line[1])
    elif sys.argv[1] == 'C20':
        print '%s\t%s' % (line[22], line[1])
    elif sys.argv[1] == 'C21':
        print '%s\t%s' % (line[23], line[1])
