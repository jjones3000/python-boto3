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

ec2_client = boto3.client("ec2")

reg_arr = []
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
for region in regions:
  reg_arr.append(region)

account_no = boto3.client('sts').get_caller_identity().get('Account')

for region in reg_arr:

    x = datetime.datetime.now()
    date_stamp = str(x.month) + "-" + str(x.day) + "-" + str(x.year) + "\n"

    ec2 = boto3.client('ec2', region_name=region)
    s3r = boto3.resource('s3', region_name=region)

    # Open the file and write the date to it.
    #f = open("unattached_fe_eips.txt", "a")

    #f.write(date_stamp)

    addresses_dict = ec2.describe_addresses()
    
    #print(addresses_dict)
    for eip_dict in addresses_dict['Addresses']:
        if "NetworkInterfaceId" not in eip_dict:
        
            # WRITE ANY UNATTAHCED EIPS TO THE FILE
            #f.write(datestamp + "unattached ip address: " + eip_dict['PublicIp'] + "\n")
            print("ARN: NA") 
            print("Resource id: NA") 
            print("Resource Name: NA") 
            print("Account Name: NA") 
            print("Account no: " + account_no) 
            print(date_stamp + "unattached ip address: " + eip_dict['PublicIp'] + "\n")
            print("Tags: \n")
            for address in addresses_dict:
              try:
                print(addresses_dict['Addresses'][0]['Tags'])
              except:
                print("Resource has no tags")  


            

            # UNCOMMENT THIS LINE WHEN READY TO DELETE
            #ec2.release_address(AllocationId=eip_dict['AllocationId'])
            
    # Save and Close the file
    #f.close()

    # Write the file to an ss3 bucket
    s3r.Bucket('jeffs-test-bucket').upload_file('unattached_fe_eips.txt','unattached_fe_eips.txt')
    