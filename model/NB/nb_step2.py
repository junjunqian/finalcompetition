#!/usr/bin/env python
#authors: Junjun Qian, Xiaoqin Zhou, Shirui Ouyang, Yanan Wang

"""
input:  feature&value , click
output: feature&value , Pr(feature=value|click) , Pr(feature=value|no-click)
"""

import re
import sys
from os import listdir
from os.path import isfile, join
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
        except ValueError:
            continue
        if clicknonclick == 0:
            current_nonclick += 1
        elif clicknonclick == 1:
            current_click += 1
        ad_identifier_click = current_click
        ad_identifier_nonclick = current_nonclick

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
        if clicknonclick == 0:
            current_nonclick += 1
        elif clicknonclick == 1:
            current_click += 1
        hour_click = current_click
        hour_nonclick = current_nonclick

#    ad identifier, click, hour, C1, banner_pos, site_id, site_domain, site_category, app_id, app_domian, app_category, device_id, device_ip, device_model, device_type, device_conn_type, C14-C21 



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



#read the file
for parts in filenames:
    if not re.match("^part-.....$$",parts) is None:
        filename  = sys.argv[1] + re.match("^part-.....$$",parts).group(0)
        file = open(filename)
        items = [line.strip() for line in file]
        for item in items:
            item = item.split('\t')
            try:
                click = int(item[1])
                impression = int(item[2])
            except ValueError:
                continue
            
            # for feature = value, calculate Pr(feature=value|click) and Pr(feature=value|no-click)
            if 'ad_id' in item[0] and impression > 5:
                p1 = float(int(item[1]) + 1) / (total_click + unique_ad_id)
                p2 = float(int(item[2]) - int(item[1]) + 1) / (total_impression - total_click + unique_ad_id)
                print '%s\t%.9f\t%.9f' % (item[0], p1, p2)
            elif 'advertiser_id' in item[0] and impression > 5:
                p1 = float(int(item[1]) + 1) / (total_click + unique_advertiser_id)
                p2 = float(int(item[2]) - int(item[1]) + 1) / (total_impression - total_click + unique_advertiser_id)
                print '%s\t%.9f\t%.9f' % (item[0], p1, p2)
            elif 'depth' in item[0] and impression > 5:
                p1 = float(int(item[1]) + 1) / (total_click + unique_depth)
                p2 = float(int(item[2]) - int(item[1]) + 1) / (total_impression - total_click + unique_depth)
                print '%s\t%.9f\t%.9f' % (item[0], p1, p2)
            elif 'position' in item[0] and impression > 5:
                p1 = float(int(item[1]) + 1) / (total_click + unique_position)
                p2 = float(int(item[2]) - int(item[1]) + 1) / (total_impression - total_click + unique_position)
                print '%s\t%.9f\t%.9f' % (item[0], p1, p2)
            elif 'query_id' in item[0] and impression > 5:
                p1 = float(int(item[1]) + 1) / (total_click + unique_query_id)
                p2 = float(int(item[2]) - int(item[1]) + 1) / (total_impression - total_click + unique_query_id)
                print '%s\t%.9f\t%.9f' % (item[0], p1, p2)
            elif 'keyword_id' in item[0] and impression > 5:
                p1 = float(int(item[1]) + 1) / (total_click + unique_keyword_id)
                p2 = float(int(item[2]) - int(item[1]) + 1) / (total_impression - total_click + unique_keyword_id)
                print '%s\t%.9f\t%.9f' % (item[0], p1, p2)
            elif 'title_id' in item[0] and impression > 5:
                p1 = float(int(item[1]) + 1) / (total_click + unique_title_id)
                p2 = float(int(item[2]) - int(item[1]) + 1) / (total_impression - total_click + unique_title_id)
                print '%s\t%.9f\t%.9f' % (item[0], p1, p2)
            elif 'description_id' in item[0] and impression > 5:
                p1 = float(int(item[1]) + 1) / (total_click + unique_description_id)
                p2 = float(int(item[2]) - int(item[1]) + 1) / (total_impression - total_click + unique_description_id)
                print '%s\t%.9f\t%.9f' % (item[0], p1, p2)
            elif 'user_id' in item[0] and impression > 5:
                p1 = float(int(item[1]) + 1) / (total_click + unique_user_id)
                p2 = float(int(item[2]) - int(item[1]) + 1) / (total_impression - total_click + unique_user_id)
                print '%s\t%.9f\t%.9f' % (item[0], p1, p2)
        file.close()

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

#calculate Pr(click) and Pr(noclick)
p1 = float(total_click) / (total_impression)
p2 = float(total_impression - total_click) / (total_impression)
print '%s\t%.9f\t%.9f' % ('totaltotal', p1, p2)
