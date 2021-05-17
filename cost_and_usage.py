<<<<<<< HEAD
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
=======
import os
import json
import boto3
import pprint
from bson import json_util # pip install pymongo
import bson
import sys
from datetime import datetime, timedelta
>>>>>>> 1ebd3473117509d689c758c212efdb0043f2fd30


iamc = boto3.client('iam')
ec2c = boto3.client('ec2')
price = boto3.client('pricing')
ce = boto3.client('ce')
ebs_client = boto3.client('ebs')
<<<<<<< HEAD
pricing = boto3.client('pricing')


#========== Cost Explorer
# An error occurred (ExpiredTokenException) when calling the GetCostAndUsage operation: The security token included in the request is expired
# https://aws.amazon.com/premiumsupport/knowledge-center/security-token-expired/



# cer = ce.get_cost_and_usage(
    # TimePeriod={
        # 'Start': '2020-05-13',
        # 'End': '2021-05-13'
    # },
    # Granularity='MONTHLY',
    # Filter={
        # 'Dimensions': {
            # 'Key': 'SERVICE',
            # 'Values': [
                # 'EC2',
            # ],
            # 'MatchOptions': [
                # 'EQUALS',
            # ]
        # },
    # },
    # Metrics=[
        # 'BLENDED_COST',
    # ],

# )
# pprint(cer)

# An error occurred (ValidationException) when calling the GetCostAndUsageWithResources operation: Group Definition dimension is invalid. Valid values are AZ, INSTANCE_TYPE, LINKED_ACCOUNT, OPERATION, PURCHASE_TYPE, SERVICE, USAGE_TYPE, PLATFORM, TENANCY, RECORD_TYPE, LEGAL_ENTITY_NAME, DEPLOYMENT_OPTION, DATABASE_ENGINE, CACHE_ENGINE, INSTANCE_TYPE_FAMILY, REGION, BILLING_ENTITY, RESERVATION_ID, RESOURCE_ID, SAVINGS_PLANS_TYPE, SAVINGS_PLAN_ARN, OPERATING_SYSTEM

# ce_with_resource = ce.get_cost_and_usage_with_resources(
    # TimePeriod={
        # 'Start': '2021-04-30',
        # 'End': '2021-05-01'
    # },
    # Granularity='MONTHLY',
    # Filter={
        # 'Dimensions': {
            # 'Key': 'SERVICE',
            # 'Values': ['EC2','Amazon Elastic Compute Cloud - Compute'],
        # },
    # },
    # GroupBy=[
        # {
            # 'Type': 'AZ',
            # 'Key': 'us-east-1'        
        # },
    # ],

# )

# pprint(ce.response)

#========== Savings Plans


products = pricing.get_products(
    ServiceCode='AmazonEC2',
    Filters=[
        {
            'Type': 'TERM_MATCH',
            'Field': 'ServiceCode',
            'Value': 'AmazonEC2',
        },
    ],
    FormatVersion='aws_v1',
    MaxResults=100
)

# Setup the paginator
paginator = pricing.get_paginator('get_products')
page_iterator = paginator.paginate(
    ServiceCode='AmazonEC2',
    Filters=[
        {
            'Type': 'TERM_MATCH',
            'Field': 'ServiceCode',
            'Value': 'AmazonEC2',
        },
    ],
    FormatVersion='aws_v1',
    MaxResults=100
)

# Start iterating over the paginator
for page in page_iterator:
    pprint(page)


# pinfos = products['PriceList']
# x=0
# for pinfo in pinfos:
    # info = (json.loads(pinfo))
    # try:  
        # x=x+1	
        # pprint(info['product']['attributes']['instanceType'])
        # #pprint(info['terms']['OnDemand'])
        # #pprint(info['product']['attributes'])
    # except:
        # continue
# print(x)

#========== Pricing

# prices = pricing.describe_services()
# services = prices['Services']


# for service in services:
    # pprint(service['ServiceCode'])





#========== COST EXPLORER
"""
cost_and_usage = ce.get_cost_and_usage(
    TimePeriod={
        'Start': '2021-03-01',
        'End': '2021-03-31',
    },
    Granularity='DAILY',
    Filter={
        'Dimensions':{
            'Key' : 'LINKED_ACCOUNT',
            'Values': ['007849015507',],
            'MatchOptions':['EQUALS']
        }
    
    },
    Metrics = ['BlendedCost','UsageQuantity']
)
print(cost_and_usage)

"""

#========== CLOUDWATCH
=======


#--- EBS





#--- COST EXPLORER
"""
cost_and_usage = ce.get_cost_and_usage(
    TimePeriod={
	    'Start': '2021-03-01',
		'End': '2021-03-31',
	},
	Granularity='DAILY',
	Filter={
	    'Dimensions':{
		    'Key' : 'LINKED_ACCOUNT',
			'Values': ['007849015507',],
			'MatchOptions':['EQUALS']
		}
	
	},
	Metrics = ['BlendedCost','UsageQuantity']
)
print(cost_and_usage)
"""


>>>>>>> 1ebd3473117509d689c758c212efdb0043f2fd30

"""
# Create CloudWatch client
client = boto3.client('cloudwatch')

response = client.get_metric_statistics(
<<<<<<< HEAD
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    StartTime=datetime(2021, 4, 4) - timedelta(seconds=600),
    EndTime=datetime(2021, 5, 4),
    Period=86400,
    Statistics=[
        'Average',
    ],
    Unit='Percent'
=======
	Namespace='AWS/EC2',
	MetricName='CPUUtilization',
	StartTime=datetime(2021, 4, 4) - timedelta(seconds=600),
	EndTime=datetime(2021, 5, 4),
	Period=86400,
	Statistics=[
		'Average',
	],
	Unit='Percent'
>>>>>>> 1ebd3473117509d689c758c212efdb0043f2fd30
)
for cpu in response['Datapoints']:
  if 'Average' in cpu:
    print(cpu['Average'])

#print(response)

for cpu in response['Datapoints']:
  print(cpu)
"""
<<<<<<< HEAD
#========== LIST ALL IAM USERS FOR AN ACCOUNT

# for user in iamc.list_users()['Users']:
  # user_name = user['UserName']
  # print(user_name)
# ec2response = ec2c.describe_hosts()
# #print(ec2response)

#========== EC2
# ec2s = ec2c.describe_instances()



# for instance in ec2s:
    # inst = ec2s['Reservations'][0]['Instances'][0]['ImageId']
    # inst_type = ec2s['Reservations'][0]['Instances'][0]['InstanceType']
    
    # acct_no = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['OwnerId']
    # pub_ip = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp']
    # pvt_ip = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddress']
    # secgrp = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Groups'][0]['GroupId']
    # status = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Status']
    # core_ct = ec2s['Reservations'][0]['Instances'][0]['CpuOptions']['CoreCount']
    # print("\n\n")
    # print("-------- Instance Detail ------------")
    # print("\n")
    # print("aws account number:  " + acct_no)
    # print("           ImageId: " + inst)
    # print(" availability zone:  " + inst_type)
    # print("          PublicIp:  " + pub_ip)
    # print("        Private IP:  " + pvt_ip)
    # print("    Security Group:  " + secgrp)
    # print("            Status:  " + status)
    # print("        Core Count:  " + str(core_ct))
    # print("\n")
    # print("--------------------------------------\n\n")


=======
#--- LIST ALL IAM USERS FOR AN ACCOUNT
"""
for user in iamc.list_users()['Users']:
  user_name = user['UserName']
  print(user_name)
ec2response = ec2c.describe_hosts()
#print(ec2response)


ec2s = ec2c.describe_instances()



for instance in ec2s:
    inst = ec2s['Reservations'][0]['Instances'][0]['ImageId']
    inst_type = ec2s['Reservations'][0]['Instances'][0]['InstanceType']
    
    acct_no = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['OwnerId']
    pub_ip = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp']
    pvt_ip = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddress']
    secgrp = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Groups'][0]['GroupId']
    status = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Status']
    core_ct = ec2s['Reservations'][0]['Instances'][0]['CpuOptions']['CoreCount']
    print("\n\n")
    print("-------- Instance Detail ------------")
    print("\n")
    print("aws account number:  " + acct_no)
    print("           ImageId: " + inst)
    print(" availability zone:  " + inst_type)
    print("          PublicIp:  " + pub_ip)
    print("        Private IP:  " + pvt_ip)
    print("    Security Group:  " + secgrp)
    print("            Status:  " + status)
    print("        Core Count:  " + str(core_ct))
    print("\n")
    print("--------------------------------------\n\n")

"""
>>>>>>> 1ebd3473117509d689c758c212efdb0043f2fd30



"""

for instance in ec2response['Hosts']:
   print(instance)

for instance in ec2response['ResponseMetadata']['HTTPHeaders']:
   print(instance[0])
 
for img in ec2imgs:
    print(img)
""" 