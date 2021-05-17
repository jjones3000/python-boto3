import boto3
import json
from bson import json_util
import os
import sys
import csv
import datetime
import io
import re
import requests
import base64
import logging
import itertools, sys
import dateutil.parser
from pprint import pprint
import datetime
from json import JSONEncoder

"""
class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

"""
<<<<<<< HEAD
arr_from_slack = [
# 'production-push360-gcm-green-2018102418140676090000000c',
'dev-website-website-blue-20200515221620972100000004',
# 'production-drive-report-green-2018122023334785650000000b',
# 'production-drive-history-green-20181102173958557500000012',
# 'production-quickloc-blue-20181205234708657400000003',
# 'dev-consul.blue.20171025223236660900000002',
# 'production-async-cake-iap-blue-20191004003141579800000004',
# 'mysql-main-55.production20201006014315842500000001',
# 'production-nsq-kinesis-blue-20181116194837156700000008',
# 'mysql-main-04.production20191205001240599700000004',
# 'master-us-east-1c.masters.kube.dev.us-east-1.life360.com',
# 'production-metronome-blue-20181114221222458300000003',
# 'dev-nsq-kinesis-blue-20200204224219868600000007',
# 'production-rattail-http-green-20180913215903145900000003',
# 'nodes.kube.dev.us-east-1.life360.com',
# 'production-grafana-blue-20190816224619768800000004',
# 'eks-56b76412-3f5c-bf98-97b6-fa893fff4ef6',
# 'production-blackbox_exporter-blue-20190621220427752700000004',
# 'eks-f0b80e8a-e150-3694-3f16-eb2b1f545005',
# 'production-mydb-green-20190517010205708100000002',
# 'production-vernemq2-green-20190405164106264500000003',
# 'production-async-cake-device-deleted-blue-2018110118514426130000000f',
# 'production-nsqadmin-blue-20200505150122462400000004',
# 'mysql-main-25.production00c78d1ecfff5178f6046cd8e1',
# 'mysql-main-35.production20191205001240496000000003',
# 'production-tumbler-blue-20190625193057059500000003',
# 'production-nsq-kinesis-drives-green-2018111619483745940000000b',
# 'mysql-main-75.production20191205002553665500000003',
# 'production-eks1-asg',
# 'master-us-east-1d.masters.kube.dev.us-east-1.life360.com',
# 'production-appboy-blue-20181108000619662600000004',
# 'dev-eks2-asg',
# 'production-async-cake-pushuserlocation-green-20180917215043713800000004',
# 'production-geodecode-blue-20181108201329460000000004',
# 'production-nsq-kinesis-dwell-blue-20181116194837056200000007',
# 'production-consul-blue-20200317200756775100000004',
# 'cx-i3.blue.00c2d56cd52c7a6ccc1d089a2f',
# 'eks-98b76412-45ac-b143-ac3a-fa1deec4ea8b',
# 'mysql-main-43.production20200420013936233200000001',
# 'production-dvbrawdataforwarding-blue-20181119185142457900000003',
# 'production-nsqlookupd-blue-20181030234025661100000003',
# 'production-git2consul-blue-20190625193043554700000004',
# 'production-async-cake-sos-alert-green-20200506162200039700000004',
# 'production-platform-location-blue-2019111122020342940000000c',
# 'eks-f8b80e8a-e13c-6bb6-5610-8bc2a5e52f76',
# 'production-data-operations-blue-20191106003614095200000004',
# 'mysql-main-805.production20200324023228805500000001',
# 'master-us-east-1e.masters.kube.dev.us-east-1.life360.com',
# 'production-mydb-google-oauth-blue-20190914003205174800000001',
# 'prod-website-website-green-20200527224852946800000003',
# 'dev-mono-green-debug-158',
# 'dev-cx-qa-blue-20171120191230346000000004',
# 'eks-a8b80e8a-e13f-7e1d-cfdc-952c1b965c5d',
# 'production-cx-drive-report-blue-20181220233345962400000007',
# 'production-frontend-router-blue-20190507215201657500000004',
# 'production-george-read-green-20181102174000458700000016',
# 'eks-b6b76412-455a-4291-a994-30dee265d00e',
# 'production-drive-report-http-green-20181220233346955800000009',
# 'dev-dvbrawdataforwarding-blue-20210430011524223500000003',
# 'production-geonames-platform-blue-20190628195116904500000005',
# 'production-post-rgc-green-20181102173958556600000011'
]

auto_sg = boto3.client('autoscaling')
ec2c = boto3.client('ec2')

def get_asg_tags(group_name):
        asg = auto_sg.describe_auto_scaling_groups(
            AutoScalingGroupNames=[group_name],
        )
        tags = asg['AutoScalingGroups'][0]['Tags']
        return tags

def get_ec2_names(group_name):
        asg = auto_sg.describe_auto_scaling_groups(
            AutoScalingGroupNames=[group_name],
        )
        ec2_names = asg['AutoScalingGroups'][0]['Instances']
        return ec2_names


def asg_info(group):
    i=0
    asg = auto_sg.describe_auto_scaling_groups(
        AutoScalingGroupNames=[group],

    )
    tags = asg['AutoScalingGroups'][0]['Tags']
    instances = asg['AutoScalingGroups'][0]['Instances']
    for i in instances:
        instance_id = asg['AutoScalingGroups'][0]['Instances'][0]['InstanceId']
        start="[ "
        spart=''
        for tag in tags:
            spart += " Key=" + tag['Key'] + ",Value="+tag['Value'] 
            #print(" Key=" + tag['Key'] + ",Value="+tag['Value'] )
            
        fpart="aws ec2 create-tags --resources " + instance_id + " --tags"
        end=" ]"
        print(fpart+start+spart+end)
    # return asg['AutoScalingGroups'][0]['AutoScalingGroupName']



        

for arr in arr_from_slack:
    curr_asg = asg_info(arr)
    # asg_tags = get_asg_tags(group_name)
    # asg_ec2_names = get_ec2_names(group_name)
    # print(group_name)
    
    

    # for tag in asg_tags:
        # print(tag['Key'] + "  " + tag['Value'] )
        
    # for asg_ec2_name in asg_ec2_names:
        # inst_id = asg_ec2_name['InstanceId']
        
        # print(asg_ec2_name['InstanceId'])
    
    
    
    
    
    
############################# ASG INFO FUNCTION ########################################
# def asg_info(group):
    # i=0
    # asg = auto_sg.describe_auto_scaling_groups(
        # AutoScalingGroupNames=[group],

    # )
    # instances = asg['AutoScalingGroups'][0]['Instances']
    # print(asg['AutoScalingGroups'][0]['AutoScalingGroupName'])
    # for instance in instances:
        # print("    " + str(instances[i]['InstanceId']))
        # i=i+1
######################################################################################


#pprint(asg['AutoScalingGroups'][0]['Instances'][0]['InstanceId'])
#pprint(len(asg))




    #pprint(group)
    #pprint(asg['AutoScalingGroups'][0])
    # instances = asg['AutoScalingGroups'][0]['Instances']
    # print("Number of Instances in Group " + str(len(instances)))
    # for inst in instances:
        # pprint(inst['InstanceId'])

"""
for group in asg['AutoScalingGroups']:
    pprint(group['AutoScalingGroupName'])

=======

auto_sg = boto3.client('autoscaling')

asg = auto_sg.describe_auto_scaling_groups()
for group in asg['AutoScalingGroups']:
    pprint(group['AutoScalingGroupName'])
"""
>>>>>>> 1ebd3473117509d689c758c212efdb0043f2fd30
f = open("demofile2.txt", "a")

json_object = json.dumps(asg, indent = 4, cls=DateTimeEncoder)

with open("demofile2.txt", "w") as outfile:
    outfile.write(json_object)
<<<<<<< HEAD
    
=======
	
>>>>>>> 1ebd3473117509d689c758c212efdb0043f2fd30
f.close()
"""