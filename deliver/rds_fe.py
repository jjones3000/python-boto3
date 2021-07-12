#!/usr/bin/python

"""
1. arn
2. resource id
3. resource name
4. account name
5. account id
6. all tags

"""

import json
import os
import boto3
import base64
from botocore.exceptions import ClientError
import datetime
import logging
import dateutil.parser
import array as arr

from pprint import pprint

reg_arr = []
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
for region in regions:
  reg_arr.append(region)

for region in reg_arr:

    rds = boto3.client('rds')
    account_no = boto3.client('sts').get_caller_identity().get('Account')
    rdscluster = rds.describe_db_clusters()
    rdssnaps = rds.describe_db_snapshots()

    acct_nos = ['007849015507','007849015508']

    #pprint(rdssnaps)

    # Accessing AWS Accounts with Boto3
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html

    # import boto3

    # client = boto3.client(
        # 's3',
        # aws_access_key_id=ACCESS_KEY,
        # aws_secret_access_key=SECRET_KEY,
        # aws_session_token=SESSION_TOKEN
    # )

    for snap in rdssnaps['DBSnapshots']:


        rds = boto3.client('rds')
        iamc = boto3.client('iam')
        iamr = boto3.resource('iam')
        s3 = boto3.resource('s3')
        s3c = boto3.client('s3')


    print('\n')    
    rdscluster = rds.describe_db_clusters()
    rdssnaps = rds.describe_db_snapshots()
    for snap in rdssnaps['DBSnapshots']:


      now = datetime.datetime.now()
      cd = snap['SnapshotCreateTime']
      cd_dtf = datetime.datetime(cd.year,cd.month,cd.day) #cd_dtf = creation date in datetime format
      days_since = now-cd_dtf
      past_fifty_six = now - (datetime.timedelta(56))

     
      
      name = snap['DBSnapshotIdentifier']
      doffset=65-len(name)
      pstr = ' '*doffset + name
            
      if cd_dtf < past_fifty_six:
          print("===============================================  > 8wks:  DELETE  ==================================================================")
          print("Account no.: " + account_no + "\nName: " + snap['DBSnapshotIdentifier'] + "\narn: " + snap['DBSnapshotArn'] + "\nresource id: " + snap['DbiResourceId'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + "  (" + str(days_since.days) + " days ago) \nTags:\n")
          for tag in snap['TagList']:
              print("        " + tag['Value'])

      else:
          print("==================================================   < 8wks:   KEEP  ================================================================")
          print("Account no.: " + account_no + "\nName: " + snap['DBSnapshotIdentifier'] + "\narn: " + snap['DBSnapshotArn'] + "\nresource id: " + snap['DbiResourceId'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + " (" + str(days_since.days) + " days ago) \nTags:\n" )
          for tag in snap['TagList']:
              print("        " + tag['Value'])      
          print('\n')
      

    rdscluster = rds.describe_db_clusters()
    rdssnaps = rds.describe_db_cluster_snapshots()
    for snap in rdssnaps['DBClusterSnapshots']:
      cname = snap['DBClusterSnapshotIdentifier']
      coffset=65-len(name)
      cstr = ' '*coffset + name
      now = datetime.datetime.now()
      cd = snap['SnapshotCreateTime']
      cd_dtf = datetime.datetime(cd.year,cd.month,cd.day) #cd_dtf = creation date in datetime format
      days_since = now-cd_dtf
      past_fifty_six = now - (datetime.timedelta(56))
      #snapshot id= " + snap['DBClusterSnapshotIdentifier']
      # print('\n')
      if cd_dtf < past_fifty_six:
          print("================================================  > 8wks:    DELETE  ==================================================================")
          print("Account no.: " + account_no + "\nName: " + snap['DBClusterIdentifier'] + "\narn: " + snap['DBClusterSnapshotArn'] + "\nresource id: " + snap['DBClusterSnapshotIdentifier'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + "  (" + str(days_since.days) + " days ago)  \nTags:\n")
          for tag in snap['TagList']:
              print("        " + tag['Value'])
       
      else:
          print("========================================================================================================================")
          print("Account no.: " + account_no + "\nName: " + snap['DBClusterIdentifier'] + "\narn: " + snap['DBClusterSnapshotArn'] + "\nresource id: " + snap['DBClusterSnapshotIdentifier'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + "  (" + str(days_since.days) + " days ago) \nTags:\n")
          for tag in snap['TagList']:
              print("         " + tag['Value'])


    print('\n')    
    rdscluster = rds.describe_db_clusters()
