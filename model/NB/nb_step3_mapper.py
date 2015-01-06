#!/usr/bin/env python

#authors: Junjun Qian, Xiaoqin Zhou, Alan Ng

"""
input: feature&value \t Pr(feature=value|click) \t Pr(feature=value|no-click)
output: click \t impression \t Pr(click|data)
"""

import sys
import os.path

sys.path.append(os.path.dirname(__file__))

# add the feature you get interested into the feature dictionary
#  1: ad identifier,2:hour, 3:C1, 4:banner_pos, 5:site_id, 6:site_domain, 7:site_category, 8:app_id, 9:app_domian, 10:app_category, 11:device_id, 12:device_ip, 13:device_model, 14:device_type, 15:device_conn_type, 16:C14, 17:C15, 18:C16, 19:C17, 20:C18, 21:C19, 22:C20, 23:C21 

feature_dict = {1: "ad identifier",2:"hour", 3:"C1", 4:"banner_pos", 5:"site_id", 6:"site_domain", 7:"site_category", 8:"app_id", 9:"app_domian", 10:"app_category", 11:"device_id", 12:"device_ip", 13:"device_model", 14:"device_type", 15:"device_conn_type", 16:"C14", 17:"C15", 18:"C16", 19:"C17", 20:"C18", 21:"C19", 22:"C20", 23:"C21"}

prob_dict = {}

# in order to access the file from s3 you need to cache file.

def read_probs():
    """ 
    Reads the probability file and outputs a dictionary.
    The file has the form:
    advert_id10040 \t 0.00184842883549 \t 0.00377969762419
    advert_id1007 \t 0.00184842883549 \t 0.00107991360691
    ad_id10110295 \t 0.00109170305677 \t 0.000898069151325
    ad_id10110317 \t 0.00109170305677 \t 0.000898069151325
    ad_id_unk \t 0.00109170305677 \t 0.000449034575662
    advert_id_unk \t 0.00184842883549 \t 0.000539956803456
    totaltotal \t 0.033185840708 \t 0.966814159292
    """
    probs = {}
    # read prob file
    with open("prob.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        feature_value, prob_click, prob_no_click = line.split('\t')
        key = feature_value
        if float(prob_click) == 0:
            prob_click = 0.000000001
        if float(prob_no_click) == 0:
            prob_no_click = 0.000000001
        probs[key] = (float(prob_click), float(prob_no_click))
    return probs

def get_prob_from_dict(feature, value):
    """ 
    Given feature and value returns probs.
    Returns 
    (Prob(feature = value | click), Prob(feature = value | no click))
    if value is not in the dictionary
    (Prob(feature = "UNK" | click), Prob(feature = "UNK" | no click))
    """
    key = "%s%s" % (feature, value)
    if key in prob_dict:
        return prob_dict[key]
#    key = "%s_%s" % (feature, "unk")
#    if key in prob_dict:
#        return prob_dict[key]
    return None


prob_dict = read_probs()

# Reading validation / test lines
for line in sys.stdin:
    #record the instance we are working at
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into a list of strings
    line = line.split('\t')
    
    #for every feature in the instance, calculate P(click|data) 
    #P(click|data) = P(data|click) * P(noclik) / (P(data|click) * P(noclik) + P(data|noclick) * P(noclik))
    #P(data|click) = Pr(feature1=value|click) * Pr(feature2=value|click) * ...
    #P(data|noclick) = Pr(feature1=value|noclick) * Pr(feature2=value|noclick) * ...
    p = get_prob_from_dict(feature_dict[3], line[3])[0] * get_prob_from_dict("total", "total")[0]
    np = get_prob_from_dict(feature_dict[3], line[3])[1] * get_prob_from_dict("total", "total")[1]
    prob = float(p) / (float(p) + float(np))
    #print click \t impression \t Pr(click|data)
    print "%s\t%s\t%s" % (line[1], prob)
    
