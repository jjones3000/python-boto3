#!/usr/bin/python
import os
import json
from json import JSONEncoder
import base64
import boto3
from botocore.exceptions import ClientError
from botocore.config import Config
import itertools, sys
import pprint
from pprint import pprint
from datetime import datetime, timedelta
import dateutil.parser
import logging
import array as arr

from pprint import pprint
ec2_client = boto3.client("ec2")
elb = boto3.client("elbv2")

cloudwatch_client = boto3.client('cloudwatch')
response = cloudwatch_client.list_metrics()

f = open("fe_idle_elb_rpt.txt", "a")

account_no = boto3.client('sts').get_caller_identity().get('Account')

lbs = elb.describe_load_balancers()

reg_arr = []
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
for region in regions:
  reg_arr.append(region)
  
  
#pprint(targetgroups)

#pprint(lbs)
def get_req_count(region, lb_name):
    client = boto3.client('cloudwatch', region_name=region)
    count = 0
    response = client.get_metric_statistics(
            Namespace="AWS/ApplicationELB",
            MetricName="RequestCount",
            Dimensions=[
                {
                    "Name": "LoadBalancer",
                    "Value": lb_name
                },
            ],
            StartTime=datetime.now() - timedelta(days=7),
            EndTime=datetime.now(),
            Period=86460,
            Statistics=[
                "Sum",
            ]
    )   

    #print(response2)        
    for r in response['Datapoints']:
        count = (r['Sum'])

    return count

#pprint(lbs)
x = 0
for lb in lbs['LoadBalancers']:
    tags = elb.describe_tags(
      ResourceArns = [lbs['LoadBalancers'][x]['LoadBalancerArn']]
    )
    
    
    print("Account Number: " + account_no)
    print("Load Balancer ARN: " + lbs['LoadBalancers'][x]['LoadBalancerArn'])
    arn_parts = (lbs['LoadBalancers'][x]['LoadBalancerArn']).split('/')
    lb_name = str(arn_parts[1]+"/"+arn_parts[2]+"/"+arn_parts[3])
    print("Load Balancer Name: " + str(lb_name))
    print("Connections in the past 7 days: ")
    print(get_req_count('us-east-2',lb_name))
    #print("Load Balancer Name: " + lbs['LoadBalancers'][x]['LoadBalancerName'])
    for tag in tags['TagDescriptions']:
      try:
        print("Tags: " + tag['Tags'][0]['Key'])
      except:
        print("no tags")
    targetgroups = elb.describe_target_groups(
        LoadBalancerArn = lbs['LoadBalancers'][x]['LoadBalancerArn']
    )
    for target in targetgroups['TargetGroups']:
        ths = elb.describe_target_health(
            TargetGroupArn = target['TargetGroupArn']
        )
        #pprint(ths)
        if len(ths['TargetHealthDescriptions']):
            pprint(ths['TargetHealthDescriptions'])
            #print('No attached instances found\n')
    print('\n\n')
    x = x + 1
        
    #pprint(tgs['TargetGroups'])

    #pprint(tags['TagDescriptions'])


    #for target in targetgroups['TargetGroups']:
      #pprint(tg['LoadBalancerArns'])
      #pprint(target)
      #pprint
      #pprint(tg['TargetGroupArn'])

    #regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]