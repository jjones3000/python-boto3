#!/usr/bin/python
import os
import json
import boto
import boto.ec2.elb
import boto.ec2.cloudwatch
from boto import ec2
from boto.ec2.cloudwatch import CloudWatchConnection
import boto3
import itertools, sys
import pprint
from pprint import pprint
from json import JSONEncoder
from datetime import datetime, timedelta
import csv
import xlwt
import glob
import os

cloudwatch_client = boto3.client('cloudwatch', region_name='us-east-2')

start_time = datetime.now() - timedelta(days=7)
end_time = datetime.now()


elb_conn_metric = cloudwatch_client.get_metric_statistics(
	Namespace='AWS/ELB',
	MetricName='ActiveFlowCount',
	Statistics=[
		'Average',
	],
	StartTime= start_time,
    EndTime= end_time,
    Period=3600 * 24,
	Unit='Count'
)

pprint(elb_conn_metric)


"""
### elb = boto3.client('elb') # use this for classic load balancers
elb = boto3.client('elbv2') # use this for application load balancers

lbs = elb.describe_load_balancers()
x = 0
for lb in lbs:
  
  pprint(lbs['LoadBalancers'][x]['LoadBalancerArn'])
  rarn = lbs['LoadBalancers'][x]['LoadBalancerArn']
  tags = elb.describe_tags(
    ResourceArns=[rarn]
  )
  try:
    pprint(tags['TagDescriptions'][0]['Tags'][0]['Key'])
  except:
    print("no tags found")

  x = x + 1

target_groups = elb.describe_target_groups()
pprint(target_groups)

target_health = elb.describe_target_health()
pprint(target_health)

"""
