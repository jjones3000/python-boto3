import os
import json
import boto3
import pprint
from bson import json_util # pip install pymongo
import bson
import sys
from datetime import datetime, timedelta


iamc = boto3.client('iam')
ec2c = boto3.client('ec2')
price = boto3.client('pricing')
ce = boto3.client('ce')
ebs_client = boto3.client('ebs')


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



"""
# Create CloudWatch client
client = boto3.client('cloudwatch')

response = client.get_metric_statistics(
	Namespace='AWS/EC2',
	MetricName='CPUUtilization',
	StartTime=datetime(2021, 4, 4) - timedelta(seconds=600),
	EndTime=datetime(2021, 5, 4),
	Period=86400,
	Statistics=[
		'Average',
	],
	Unit='Percent'
)
for cpu in response['Datapoints']:
  if 'Average' in cpu:
    print(cpu['Average'])

#print(response)

for cpu in response['Datapoints']:
  print(cpu)
"""
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



"""

for instance in ec2response['Hosts']:
   print(instance)

for instance in ec2response['ResponseMetadata']['HTTPHeaders']:
   print(instance[0])
 
for img in ec2imgs:
    print(img)
""" 