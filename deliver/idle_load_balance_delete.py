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
import datetime
import csv
import xlwt
import glob
import os



### elb = boto3.client('elb') # use this for classic load balancers
elb = boto3.client('elbv2') # use this for application load balancers

lbs = elb.describe_load_balancers(
    LoadBalancerArns = ["arn:aws:elasticloadbalancing:us-east-2:725837026074:loadbalancer/app/thisisatestloadbalancerfordev/92f072dc3c21f626"]
)

for lb in lbs['LoadBalancerDescriptions']:
    print(lb['Instances'])
    
#pprint(lbs['LoadBalancerDescriptions'])


