#!/usr/bin/env python

#authors: Junjun Qian, Xiaoqin Zhou, Alan Ng
"""
output: feature, AVGclick(float)
"""

from operator import itemgetter
import sys

current_feature = None
current_click = 0
current_impression = 0
feature = None

for line in sys.stdin:
    line = line.strip()
    feature, click = line.split('\t')
    try:
        click = int(click)
        if current_feature == feature:
            if click != 0:
                current_click += click
            current_impression += click 
        else:
            if current_feature:
                if sys.argv[1] == "AVGctr":
                    AVGctr = float(current_click) / (current_impression)
                    print '%s\t%s' % (current_feature, AVGctr)
            current_click = click
            current_impression = 1
            current_feature = feature
    except ValueError:
        continue

if current_feature == feature:
    #collect last time
    if sys.argv[1] == "AVGctr":
        AVGctr = float(current_click + 0.05 * 75) / (current_impression + 75)
        print '%s\t%s' % (current_feature, AVGctr)
