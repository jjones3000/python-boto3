#!/usr/bin/python

import os
import json
import boto3
import itertools, sys
import pprint
from pprint import pprint
from json import JSONEncoder
import datetime
from botocore.config import Config

reg_arr = []
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
for region in regions:
  reg_arr.append(region)

for region in reg_arr:

    x = datetime.datetime.now()
    date_stamp = str(x.month) + "-" + str(x.day) + "-" + str(x.year) + "\n"

    ec2 = boto3.client('ec2', region_name=region)
    s3r = boto3.resource('s3', region_name=region)

    # Open the file and write the date to it.
    f = open("unattached_eips.txt", "a")

    f.write(date_stamp)

    addresses_dict = ec2.describe_addresses()
    print(addresses_dict)
    for eip_dict in addresses_dict['Addresses']:
        if "NetworkInterfaceId" not in eip_dict:
        
            # WRITE ANY UNATTAHCED EIPS TO THE FILE
            f.write(eip_dict['PublicIp'])

            # UNCOMMENT THIS LINE WHEN READY TO DELETE
            #ec2.release_address(AllocationId=eip_dict['AllocationId'])
            
    # Save and Close the file
    f.close()

    # Write the file to an ss3 bucket
    s3r.Bucket('jeffs-aws-audit-bucket').upload_file('unattached_eips.txt','unattached_eips.txt')