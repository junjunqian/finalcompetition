#!/usr/bin/env python
#authors: Junjun Qian, Xiaoqin Zhou, Alan Ng

"""
input:  feature&value , click
output: feature&value , Pr(feature=value|click) , Pr(feature=value|no-click)
        totaltotal    , Pr(click)               , Pr(noclick)
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
#                current_impression += 1
            else:
                current_feature = feature
                unique_ad_identifier += 1
#                current_impression = 1
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
        total_impression = total_click + total_nonclick

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

    elif 'device_conn_type' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_device_conn_type += 1
        except ValueError:
            continue

    elif 'C14' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_ C14 += 1
        except ValueError:
            continue

    elif 'C15' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_ C15 += 1
        except ValueError:
            continue

    elif 'C16' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_ C16 += 1
        except ValueError:
            continue

    elif 'C17' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_ C17 += 1
        except ValueError:
            continue

    elif 'C18' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_ C18 += 1
        except ValueError:
            continue

    elif 'C19' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_ C19 += 1
        except ValueError:
            continue

    elif 'C20' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_ C20 += 1
        except ValueError:
            continue

    elif 'C21' in feature:
        current_feature = None
        current_impression = 0
        try:
            if current_feature == feature:
            else:
                current_feature = feature
                unique_ C21 += 1
        except ValueError:
            continue

"""
    if 'ad_identifier' in feature:
        current_feature = None
        current_impression = 0
        try:
            clicknonclick = int(clicknonclick)
            if current_feature == feature:
                if clicknonclick != 0:
                    ad_identifier_click += 1
                current_impression += 1
            else:
                ad_identifier_click = clicknonclick
                current_impression = 1
                current_feature = feature
                unique_ad_identifier += 1
        except ValueError:
            continue
        ad_identifier_nonclick = current_impression - ad_identifier_click

    elif 'hour' in feature:
        current_feature = None
        current_impression = 0
        try:
            clicknonclick = int(clicknonclick)
            if current_feature == feature:
                if clicknonclick != 0:
                    hour_click += 1
                current_impression += 1
            else:
                ad_identifier_click = clicknonclick
                current_impression = 1
                current_feature = feature
                unique_hour += 1
        except ValueError:
            continue
        ad_identifier_nonclick = current_impression - ad_identifier_click
"""


for line in sys.stdin:
    line = line.strip()
    feature, clicknonclick = line.split(',')
        # for feature = value, calculate Pr(feature=value|click) and Pr(feature=value|no-click)
    if 'ad identifier' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_ad_identifier)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_ad_identifier)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)
    elif 'hour' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_hour)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_hour)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'C1' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_C1)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_C1)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'banner_pos' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_banner_pos)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_banner_pos)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'site_id' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_site_id)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_site_id)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'site_domain' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_site_domain)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_site_domain)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'site_category' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_site_category)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_site_category)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'app_id' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_app_id)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_app_id)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'app_domian' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_app_domian)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_app_domian)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'app_category' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_app_category)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_app_category)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'device_id' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_device_id)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_device_id)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'device_ip' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_device_ip)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_device_ip)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'device_model' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_device_model)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_device_model)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'device_type' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_device_type)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_device_type)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'device_conn_type' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_device_conn_type)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_device_conn_type)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'C14' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_C14)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_C14)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'C15' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_C15)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_C15)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'C16' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_C16)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_C16)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'C17' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_C17)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_C17)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'C18' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_C18)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_C18)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'C19' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_C19)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_C19)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

    elif 'C20' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_C20)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_C20)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)
    elif 'C21' in item[0]:
        p1 = float(total_click) + 1) / (total_click + unique_C21)
        p2 = float(total_nonclick) + 1) / (total_nonclick + unique_C21)
        print '%s\t%.9f\t%.9f' % (item[0], p1, p2)

"""
#calculate Pr(feature=unk|click) and Pr(feature=unk|no-click)
p1 = float(1 + unk_ad_id_click) / (total_click + unique_ad_id + 1)
p2 = float(1 + unk_ad_id_imp - unk_ad_id_click) / (total_impression - total_click + unique_ad_id + 1)
print '%s\t%.9f\t%.9f' % ('ad_id_unk', p1, p2)
p1 = float(1 + unk_advertiser_id_click) / (total_click + unique_advertiser_id + 1)
p2 = float(1 + unk_advertiser_id_imp - unk_advertiser_id_click) / (total_impression - total_click + unique_advertiser_id + 1)
print '%s\t%.9f\t%.9f' % ('advertiser_id_unk',p1, p2)
p1 = float(1 + unk_depth_click) / (total_click + unique_depth + 1)
p2 = float(1 + unk_depth_imp - unk_depth_click) / (total_impression - total_click + unique_depth + 1)
print '%s\t%.9f\t%.9f' % ('depth_unk', p1, p2)
p1 = float(1 + unk_position_click) / (total_click + unique_position+ 1)
p2 = float(1 + unk_position_imp - unk_position_click) / (total_impression - total_click + unique_position + 1)
print '%s\t%.9f\t%.9f' % ('position_unk', p1, p2)
p1 = float(1 + unk_query_id_click) / (total_click + unique_query_id + 1)
p2 = float(1 + unk_query_id_imp - unk_query_id_click) / (total_impression - total_click + unique_query_id + 1)
print '%s\t%.9f\t%.9f' % ('query_id_unk', p1, p2)
p1 = float(1 + unk_keyword_id_click) / (total_click + unique_keyword_id + 1)
p2 = float(1 + unk_keyword_id_imp - unk_keyword_id_click) / (total_impression - total_click + unique_keyword_id + 1)
print '%s\t%.9f\t%.9f' % ('keyword_id_unk', p1, p2)
p1 = float(1 + unk_title_id_click) / (total_click + unique_title_id + 1)
p2 = float(1 + unk_title_id_imp - unk_title_id_click) / (total_impression - total_click + unique_title_id + 1)
print '%s\t%.9f\t%.9f' % ('title_id_unk', p1, p2)
p1 = float(1 + unk_description_id_click) / (total_click + unique_description_id + 1)
p2 = float(1 + unk_description_id_imp - unk_description_id_click) / (total_impression - total_click + unique_description_id + 1)
print '%s\t%.9f\t%.9f' % ('description_id_unk', p1, p2)
p1 = float(1 + unk_user_id_click) / (total_click + unique_user_id + 1)
p2 = float(1 + unk_user_id_imp - unk_user_id_click) / (total_impression - total_click + unique_user_id + 1)
print '%s\t%.9f\t%.9f' % ('user_id_unk', p1, p2)
"""

#calculate Pr(click) and Pr(noclick)
p1 = float(total_click) / (total_impression)
p2 = float(total_nonclick) / (total_impression)
print '%s\t%.9f\t%.9f' % ('totaltotal', p1, p2)
