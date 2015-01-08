#!/usr/bin/env python
#authors: Junjun Qian, Xiaoqin Zhou, Alan Ng

"""
input:  feature&value , click
output: feature&value , Pr(feature=value|click) , Pr(feature=value|no-click)
        totaltotal    , Pr(click)               , Pr(noclick)
"""

import sys
#from os import listdir
#from os.path import isfile, join
#filenames = [ f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1],f))]

#the following is all the numbers we need to count in the first loop

total_click = 0
total_impression = 0

unique_hour = 0
unique_C01 = 0
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
unique_time = 0
unique_day = 0

unk_hour_click = 0
unk_C01_click = 0
unk_banner_pos_click = 0
unk_site_id_click = 0
unk_site_domain_click = 0
unk_site_category_click = 0
unk_app_id_click = 0
unk_app_domain_click = 0
unk_app_category_click = 0
unk_device_id_click = 0
unk_device_ip_click = 0
unk_device_model_click = 0
unk_device_type_click = 0
unk_device_conn_type_click = 0
unk_C14_click = 0
unk_C15_click = 0
unk_C16_click = 0
unk_C17_click = 0
unk_C18_click = 0
unk_C19_click = 0
unk_C20_click = 0
unk_C21_click = 0
unk_time_click = 0
unk_day_click = 0

unk_hour_imp = 0
unk_C01_imp = 0
unk_banner_pos_imp = 0
unk_site_id_imp = 0
unk_site_domain_imp = 0
unk_site_category_imp = 0
unk_app_id_imp = 0
unk_app_domain_imp = 0
unk_app_category_imp = 0
unk_device_id_imp = 0
unk_device_ip_imp = 0
unk_device_model_imp = 0
unk_device_type_imp = 0
unk_device_conn_type_imp = 0
unk_C14_imp = 0
unk_C15_imp = 0
unk_C16_imp = 0
unk_C17_imp = 0
unk_C18_imp = 0
unk_C19_imp = 0
unk_C20_imp = 0
unk_C21_imp = 0
unk_time_imp = 0
unk_day_imp = 0

#read the input file
for line in sys.stdin:
    line = line.strip()
    feature, click, impression = line.split(',')
    try:
        click = int(click)
        impression = int(impression)
    except ValueError:
        continue

    if 'hour' in feature:
        if impression > int(sys.argv[1]):
            unique_hour += 1
        else:
            unk_hour_click += click
            unk_hour_imp += imp
        total_click += click
        total_impression += impression


    elif 'time' in feature:
        if impression > int(sys.argv[1]):
            unique_time += 1
        else:
            unk_time_click += 1
            unk_time_imp += 1

    elif 'day' in feature:
        if impression > int(sys.argv[1]):
            unique_day += 1
        else:
            unk_day_click += 1
            unk_day_imp += 1


    elif 'C01' in feature[0:3]:
        if impression > int(sys.argv[1]):
            unique_C01 += 1
        else:
            unk_C01_click += 1
            unk_C01_imp += 1

    elif 'banner_pos' in feature:
        if impression > int(sys.argv[1]):
            unique_banner_pos += 1
        else:
            unk_banner_pos_click += 1
            unk_banner_pos_imp += 1

    elif 'site_id' in feature:
        if impression > int(sys.argv[1]):
            unique_site_id += 1
        else:
            unk_site_id_click += 1
            unk_site_id_imp += 1

    elif 'site_domain' in feature:
        if impression > int(sys.argv[1]):
            unique_site_domain += 1
        else:
            unk_site_domain_click += 1
            unk_site_domain_imp += 1

    elif 'site_category' in feature:
        if impression > int(sys.argv[1]):
            unique_site_category += 1
        else:
            unk_site_category_click += 1
            unk_site_category_imp += 1

    elif 'app_id' in feature:
        if impression > int(sys.argv[1]):
            unique_app_id += 1
        else:
            unk_app_id_click += 1
            unk_app_id_imp += 1

    elif 'app_domain' in feature:
        if impression > int(sys.argv[1]):
            unique_app_domain += 1
        else:
            unk_app_domain_click += 1
            unk_app_domain_imp += 1

    elif 'app_category' in feature:
        if impression > int(sys.argv[1]):
            unique_app_category += 1
        else:
            unk_app_category_click += 1
            unk_app_category_imp += 1

    elif 'device_id' in feature:
        if impression > int(sys.argv[1]):
            unique_device_id += 1
        else:
            unk_device_id_click += 1
            unk_device_id_imp += 1

    elif 'device_ip' in feature:
        if impression > int(sys.argv[1]):
            unique_device_ip += 1
        else:
            unk_device_ip_click += 1
            unk_device_ip_imp += 1

    elif 'device_model' in feature:
        if impression > int(sys.argv[1]):
            unique_device_model += 1
        else:
            unk_device_model_click += 1
            unk_device_model_imp += 1

    elif 'device_type' in feature:
        if impression > int(sys.argv[1]):
            unique_device_model += 1
        else:
            unk_device_model_click += 1
            unk_device_model_imp += 1

    elif 'device_conn_type' in feature:
        if impression > int(sys.argv[1]):
            unique_device_type += 1
        else:
            unk_device_type_click += 1
            unk_device_type_imp += 1

    elif 'C14' in feature[0:3]:
        if impression > int(sys.argv[1]):
            unique_C14 += 1
        else:
            unk_C14_click += 1
            unk_C14_imp += 1

    elif 'C15' in feature[0:3]:
        if impression > int(sys.argv[1]):
            unique_C15 += 1
        else:
            unk_C15_click += 1
            unk_C15_imp += 1

    elif 'C16' in feature[0:3]:
        if impression > int(sys.argv[1]):
            unique_C16 += 1
        else:
            unk_C16_click += 1
            unk_C16_imp += 1

    elif 'C17' in feature[0:3]:
        if impression > int(sys.argv[1]):
            unique_C17 += 1
        else:
            unk_C17_click += 1
            unk_C17_imp += 1

    elif 'C18' in feature[0:3]:
        if impression > int(sys.argv[1]):
            unique_C18 += 1
        else:
            unk_C18_click += 1
            unk_C18_imp += 1

    elif 'C19' in feature[0:3]:
        if impression > int(sys.argv[1]):
            unique_C19 += 1
        else:
            unk_C19_click += 1
            unk_C19_imp += 1

    elif 'C20' in feature[0:3]:
        if impression > int(sys.argv[1]):
            unique_C20 += 1
        else:
            unk_C20_click += 1
            unk_C20_imp += 1

    elif 'C21' in feature[0:3]:
        if impression > int(sys.argv[1]):
            unique_C21 += 1
        else:
            unk_C21_click += 1
            unk_C21_imp += 1


for line in sys.stdin:
    line = line.strip()
    feature, click, impression = line.split(',')
    print "hahahahahahahahshjdhkashdkjashjkdhjaksdkjasdhjkashdjkhsk"

    try:
        click = int(click)
        impression = int(impression)
    except ValueError:
        continue

    if 'hour' in feature:
        print "hahahahahahahahshjdhkashdkjashjkdhjaksdkjasdhjkashdjkhsk"

        p1 = float(click + 1) / (total_click + unique_hour)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_hour)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'time' in feature:
        p1 = float(click + 1) / (total_click + unique_time)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_time)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'day' in feature:
        p1 = float(click + 1) / (total_click + unique_hour)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_hour)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'C01' in feature[0:3]:
        print "hahahahahahahahshjdhkashdkjashjkdhjaksdkjasdhjkashdjkhsk"

        p1 = float(click + 1) / (total_click + unique_C01)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_C01)
        print '%s,%.6f,%.6f' % (feature, p1, p2)


    elif 'banner_pos' in feature:
        p1 = float(click + 1) / (total_click + unique_banner_pos)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_banner_pos)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'site_id' in feature:
        p1 = float(click + 1) / (total_click + unique_site_id)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_site_id)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'site_domain' in feature:
        p1 = float(click + 1) / (total_click + unique_site_domain)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_site_domain)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'site_category' in feature:
        p1 = float(click + 1) / (total_click + unique_site_category)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_site_category)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'app_id' in feature:
        p1 = float(click + 1) / (total_click + unique_app_id)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_app_id)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'app_domian' in feature:
        p1 = float(click + 1) / (total_click + unique_app_domian)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_app_domian)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'app_category' in feature:
        p1 = float(click + 1) / (total_click + unique_app_category)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_app_category)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'device_id' in feature:
        p1 = float(click + 1) / (total_click + unique_device_id)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_device_id)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'device_ip' in feature:
        p1 = float(click + 1) / (total_click + unique_device_ip)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_device_ip)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'device_model' in feature:
        p1 = float(click + 1) / (total_click + unique_device_model)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_device_model)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'device_type' in feature:
        p1 = float(click + 1) / (total_click + unique_device_type)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_device_type)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'device_conn_type' in feature:
        p1 = float(click + 1) / (total_click + unique_device_conn_type)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_device_conn_type)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'C14' in feature[0:3]:
        p1 = float(click + 1) / (total_click + unique_C14)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_C14)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'C15' in feature[0:3]:
        p1 = float(click + 1) / (total_click + unique_C15)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_C15)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'C16' in feature[0:3]:
        p1 = float(click + 1) / (total_click + unique_C16)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_C16)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'C17' in feature[0:3]:
        p1 = float(click + 1) / (total_click + unique_C17)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_C17)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'C18' in feature[0:3]:
        p1 = float(click + 1) / (total_click + unique_C18)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_C18)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'C19' in feature[0:3]:
        p1 = float(click + 1) / (total_click + unique_C19)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_C19)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'C20' in feature[0:3]:
        p1 = float(click + 1) / (total_click + unique_C20)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_C20)
        print '%s,%.6f,%.6f' % (feature, p1, p2)

    elif 'C21' in feature[0:3]:
        p1 = float(click + 1) / (total_click + unique_C21)
        p2 = float(impression - click + 1) / (total_impression - total_click + unique_C21)
        print '%s,%.6f,%.6f' % (feature, p1, p2)




p1 = float(1 + unk_hour_click) / (total_click + unique_hour + 1)
p2 = float(1 + unk_hour_imp - unk_hour_click) / (total_impression - total_click + unique_hour + 1)
print '%s,%.6f,%.6f' % ("unk_hour", p1, p2)


p1 = float(1 + unk_time_click) / (total_click + unique_time + 1)
p2 = float(1 + unk_time_imp - unk_time_click) / (total_impression - total_click + unique_time + 1)
print '%s,%.6f,%.6f' % ("unk_time", p1, p2)


p1 = float(1 + unk_day_click) / (total_click + unique_day + 1)
p2 = float(1 + unk_day_imp - unk_day_click) / (total_impression - total_click + unique_day + 1)
print '%s,%.6f,%.6f' % ("unk_day", p1, p2)


p1 = float(1 + unk_C01_click) / (total_click + unique_C01 + 1)
p2 = float(1 + unk_C01_imp - unk_C01_click) / (total_impression - total_click + unique_C01 + 1)
print '%s,%.6f,%.6f' % ("unk_C01", p1, p2)


p1 = float(1 + unk_banner_pos_click) / (total_click + unique_banner_pos + 1)
p2 = float(1 + unk_banner_pos_imp - unk_banner_pos_click) / (total_impression - total_click + unique_banner_pos + 1)
print '%s,%.6f,%.6f' % ("unk_banner_pos", p1, p2)


p1 = float(1 + unk_site_id_click) / (total_click + unique_site_id + 1)
p2 = float(1 + unk_site_id_imp - unk_site_id_click) / (total_impression - total_click + unique_site_id + 1)
print '%s,%.6f,%.6f' % ("unk_site_id", p1, p2)


p1 = float(1 + unk_site_domain_click) / (total_click + unique_site_domain + 1)
p2 = float(1 + unk_site_domain_imp - unk_site_domain_click) / (total_impression - total_click + unique_site_domain + 1)
print '%s,%.6f,%.6f' % ("unk_site_domain", p1, p2)


p1 = float(1 + unk_site_category_click) / (total_click + unique_site_category + 1)
p2 = float(1 + unk_site_category_imp - unk_site_category_click) / (total_impression - total_click + unique_site_category + 1)
print '%s,%.6f,%.6f' % ("unk_site_category", p1, p2)


p1 = float(1 + unk_app_id_click) / (total_click + unique_app_id + 1)
p2 = float(1 + unk_app_id_imp - unk_app_id_click) / (total_impression - total_click + unique_app_id + 1)
print '%s,%.6f,%.6f' % ("unk_app_id", p1, p2)


p1 = float(1 + unk_app_domain_click) / (total_click + unique_app_domain + 1)
p2 = float(1 + unk_app_domain_imp - unk_app_domain_click) / (total_impression - total_click + unique_app_domain + 1)
print '%s,%.6f,%.6f' % ("unk_app_domain", p1, p2)


p1 = float(1 + unk_app_category_click) / (total_click + unique_app_category + 1)
p2 = float(1 + unk_app_category_imp - unk_app_category_click) / (total_impression - total_click + unique_app_category + 1)
print '%s,%.6f,%.6f' % ("unk_app_category", p1, p2)


p1 = float(1 + unk_device_id_click) / (total_click + unique_device_id + 1)
p2 = float(1 + unk_device_id_imp - unk_device_id_click) / (total_impression - total_click + unique_device_id + 1)
print '%s,%.6f,%.6f' % ("unk_device_id", p1, p2)


p1 = float(1 + unk_device_ip_click) / (total_click + unique_device_ip + 1)
p2 = float(1 + unk_device_ip_imp - unk_device_ip_click) / (total_impression - total_click + unique_device_ip + 1)
print '%s,%.6f,%.6f' % ("unk_device_ip", p1, p2)


p1 = float(1 + unk_device_model_click) / (total_click + unique_device_model + 1)
p2 = float(1 + unk_device_model_imp - unk_device_model_click) / (total_impression - total_click + unique_device_model + 1)
print '%s,%.6f,%.6f' % ("unk_device_model", p1, p2)


p1 = float(1 + unk_device_type_click) / (total_click + unique_device_type + 1)
p2 = float(1 + unk_device_type_imp - unk_device_type_click) / (total_impression - total_click + unique_device_type + 1)
print '%s,%.6f,%.6f' % ("unk_device_type", p1, p2)


p1 = float(1 + unk_device_conn_type_click) / (total_click + unique_device_conn_type + 1)
p2 = float(1 + unk_device_conn_type_imp - unk_device_conn_type_click) / (total_impression - total_click + unique_device_conn_type + 1)
print '%s,%.6f,%.6f' % ("unk_device_conn_type", p1, p2)


p1 = float(1 + unk_C14_click) / (total_click + unique_C14 + 1)
p2 = float(1 + unk_C14_imp - unk_C14_click) / (total_impression - total_click + unique_C14 + 1)
print '%s,%.6f,%.6f' % ("unk_C14", p1, p2)


p1 = float(1 + unk_C15_click) / (total_click + unique_C15 + 1)
p2 = float(1 + unk_C15_imp - unk_C15_click) / (total_impression - total_click + unique_C15 + 1)
print '%s,%.6f,%.6f' % ("unk_C15", p1, p2)


p1 = float(1 + unk_C16_click) / (total_click + unique_C16 + 1)
p2 = float(1 + unk_C16_imp - unk_C16_click) / (total_impression - total_click + unique_C16 + 1)
print '%s,%.6f,%.6f' % ("unk_C16", p1, p2)


p1 = float(1 + unk_C17_click) / (total_click + unique_C17 + 1)
p2 = float(1 + unk_C17_imp - unk_C17_click) / (total_impression - total_click + unique_C17 + 1)
print '%s,%.6f,%.6f' % ("unk_C17", p1, p2)


p1 = float(1 + unk_C18_click) / (total_click + unique_C18 + 1)
p2 = float(1 + unk_C18_imp - unk_C18_click) / (total_impression - total_click + unique_C18 + 1)
print '%s,%.6f,%.6f' % ("unk_C18", p1, p2)


p1 = float(1 + unk_C19_click) / (total_click + unique_C19 + 1)
p2 = float(1 + unk_C19_imp - unk_C19_click) / (total_impression - total_click + unique_C19 + 1)
print '%s,%.6f,%.6f' % ("unk_C19", p1, p2)

p1 = float(1 + unk_C20_click) / (total_click + unique_C20 + 1)
p2 = float(1 + unk_C20_imp - unk_C20_click) / (total_impression - total_click + unique_C20 + 1)
print '%s,%.6f,%.6f' % ("unk_C20", p1, p2)

p1 = float(1 + unk_C21_click) / (total_click + unique_C21 + 1)
p2 = float(1 + unk_C21_imp - unk_C21_click) / (total_impression - total_click + unique_C21 + 1)
print '%s,%.6f,%.6f' % ("unk_C21", p1, p2)


#calculate Pr(click) and Pr(noclick)
p1 = float(total_click) / (total_impression)
p2 = float(total_impression - total_click) / (total_impression)
print '%s,%.6f,%.6f' % ('totaltotal', p1, p2)
