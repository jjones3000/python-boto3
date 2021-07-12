#!/usr/bin/python
import os
import json
import boto3

client = boto3.client('logs')
paginator = client.get_paginator('describe_log_groups')
iterator = paginator.paginate(PaginationConfig={'MaxItems': 1000})
for page in iterator:
    #print("*** Page")
    for i in page['logGroups']:
        #print(i['logGroupName'])
        print(i)
#lss = client.describe_log_streams()
#for ls in lss:
  #print(ls)


cw_client = boto3.client('cloudwatch')
lgs = cw_client.describe_log_groups()
print(lgs)