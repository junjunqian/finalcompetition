#!/usr/bin/env python
#authors: Junjun Qian, Xiaoqin Zhou, Alan Ng

"""
input:  feature&value , click
output: feature&value , Pr(feature=value|click) , Pr(feature=value|no-click)
"""

import re
import sys
#from os import listdir
#from os.path import isfile, join
#filenames = [ f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1],f))]

#the following is all the numbers we need to count in the first loop

total_click = 0
total_nonclick = 0

unique_ad_identifier = 0
unique_hour = 0
unique_C1 = 0
unique_banner_pos = 0
unique_site_id = 0
unique_site_domain = 0
unique_site_category = 0
unique_app_id = 0
unique_app_domain = 0
unique_app_category = 0
unique_device_id = 0
unique_device_ip = 0
unique_device_model = 0
unique_device_type = 0
unique_device_conn_type = 0
unique_C14 = 0
unique_C15 = 0
unique_C16 = 0
unique_C17 = 0
unique_C18 = 0
unique_C19 = 0
unique_C20 = 0
unique_C21 = 0

ad_identifier_click = 0
hour_click = 0
C1_click = 0
banner_pos_click = 0
site_id_click = 0
site_domain_click = 0
site_category_click = 0
app_id_click = 0
app_domain_click = 0
app_category_click = 0
device_id_click = 0
device_ip_click = 0
device_model_click = 0
device_type_click = 0
device_conn_type_click = 0
C14_click = 0
C15_click = 0
C16_click = 0
C17_click = 0
C18_click = 0
C19_click = 0
C20_click = 0
C21_click = 0

ad_identifier_nonclick = 0
hour_nonclick = 0
C1_nonclick = 0
banner_pos_nonclick = 0
site_id_nonclick = 0
site_domain_nonclick = 0
site_category_nonclick = 0
app_id_nonclick = 0
app_domain_nonclick = 0
app_category_nonclick = 0
device_id_nonclick = 0
device_ip_nonclick = 0
device_model_nonclick = 0
device_type_nonclick = 0
device_conn_type_nonclick = 0
C14_nonclick = 0
C15_nonclick = 0
C16_nonclick = 0
C17_nonclick = 0
C18_nonclick = 0
C19_nonclick = 0
C20_nonclick = 0
C21_nonclick = 0

#read the input file
for line in sys.stdin:
    line = line.strip()
    feature, clicknonclick = line.split(',')
    
    if 'ad identifier' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
                current_impression += 1
            else:
                current_feature = feature
                unique_ad_identifier += 1
                current_impression = 1
        except ValueError:
            continue
        if clicknonclick == 0:
            current_nonclick += 1
        elif clicknonclick == 1:
            current_click += 1
        ad_identifier_click = current_click
        ad_identifier_nonclick = current_nonclick
        total_click = current_click
        total_nonclick = current_nonclick

    elif 'hour' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_hour += 1
        except ValueError:
            continue

    elif 'C1' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_C1 += 1
        except ValueError:
            continue

    elif 'banner_pos' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_banner_pos += 1
        except ValueError:
            continue

    elif 'site_id' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_site_id += 1
        except ValueError:
            continue

    elif 'site_domain' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_site_domain += 1
        except ValueError:
            continue

    elif 'site_category' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_site_category += 1
        except ValueError:
            continue

    elif 'app_id' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_app_id += 1
        except ValueError:
            continue

    elif 'app_domain' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_app_domain += 1
        except ValueError:
            continue

    elif 'app_category' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_app_category += 1
        except ValueError:
            continue

    elif 'device_id' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_device_id += 1
        except ValueError:
            continue

    elif 'device_ip' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_device_ip += 1
        except ValueError:
            continue

    elif 'device_model' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_device_model += 1
        except ValueError:
            continue

    elif 'device_type' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_device_type += 1
        except ValueError:
            continue
