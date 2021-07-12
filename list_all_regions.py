#!/usr/bin/python
import os
import json
import boto3
import itertools, sys
reg_arr = []
ec2_client = boto3.client('ec2')
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
for region in regions:
  reg_arr.append(region)

for region in reg_arr:
  print(region)