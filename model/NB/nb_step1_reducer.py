#!/usr/bin/env python

#authors: Junjun Qian, Xiaoqin Zhou, Alan Ng

"""
input:  feature&value \t click 
output: feature&value \t click(sum) \t impression(sum)
"""

from operator import itemgetter
import sys

current_id = None
current_click = 0
current_impression = 0
id = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from nb_coubt_mapper.py
    id, click = line.split(',')
    
    # convert click (currently a string) to int
    try:
        click = int(click)
    except ValueError:
        continue
    

    #for each unique id (feature&value), output the sum of click and the sum of impression
    if current_id == id:
        current_click += click
        current_impression += 1
    else:
        if current_id:
            print '%s,%s,%s' % (current_id, current_click, current_impression)
        current_click = click
        current_impression = 1
        current_id = id

#output the last id
if current_id == id:
    print '%s,%s,%s' % (current_id, current_click, current_impression)
