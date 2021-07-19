#!/usr/bin/python

"""
1. arn
2. resource id
3. resource name
4. account name
5. account id
6. all tags

"""

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
import datetime
import dateutil.parser
import logging
import array as arr

from pprint import pprint

ec2_client = boto3.client("ec2")
rds = boto3.client('rds')

f = open("fe_rds_snapshot_rpt.txt", "a")



reg_arr = []
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
for region in regions:
  reg_arr.append(region)
  
#pprint(reg_arr) 
 
for region in reg_arr:


    account_no = boto3.client('sts').get_caller_identity().get('Account')
    rdscluster = rds.describe_db_clusters()
    rdssnaps = rds.describe_db_snapshots()
    ec2 = boto3.client('ec2', region_name="us-east-2")
    s3r = boto3.resource('s3', region_name=region)
    #acct_nos = ['725837026074']

    pprint(rdscluster)
    pprint(rdssnaps)

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


    f.write('\n')    
    #rdscluster = rds.describe_db_clusters()
    #rdssnaps = rds.describe_db_snapshots()
	
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
          f.write("===============================================  > 8wks:  DELETE  ==================================================================")
          f.write("Account no.: " + account_no + "\nName: " + snap['DBSnapshotIdentifier'] + "\narn: " + snap['DBSnapshotArn'] + "\nresource id: " + snap['DbiResourceId'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + "  (" + str(days_since.days) + " days ago) \nTags:\n")
          print(account_no)
          print(snap['DBSnapshotIdentifier'])
          print(snap['DBSnapshotArn'])
          for tag in snap['TagList']:
              f.write("        " + tag['Key'])

      else:
          f.write("==================================================   < 8wks:   KEEP  ================================================================")
          f.write("Account no.: " + account_no + "\nName: " + snap['DBSnapshotIdentifier'] + "\narn: " + snap['DBSnapshotArn'] + "\nresource id: " + snap['DbiResourceId'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + " (" + str(days_since.days) + " days ago) \nTags:\n" )
          print(account_no)
          print(snap['DBSnapshotIdentifier'])
          print(snap['DBSnapshotArn'])

          for tag in snap['TagList']:
              f.write("        " + tag['Key'])      
          f.write('\n')
      

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
          f.write("================================================  > 8wks:    DELETE  ==================================================================")
          f.write("Account no.: " + account_no + "\nName: " + snap['DBClusterIdentifier'] + "\narn: " + snap['DBClusterSnapshotArn'] + "\nresource id: " + snap['DBClusterSnapshotIdentifier'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + "  (" + str(days_since.days) + " days ago)  \nTags:\n")
          print(snap['DBClusterIdentifier'])
          for tag in snap['TagList']:
              f.write("        " + tag['Key'])
       
      else:
          f.write("============================================== < 8wks:   KEEP ======================================================================")
          f.write("Account no.: " + account_no + "\nName: " + snap['DBClusterIdentifier'] + "\narn: " + snap['DBClusterSnapshotArn'] + "\nresource id: " + snap['DBClusterSnapshotIdentifier'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + "  (" + str(days_since.days) + " days ago) \nTags:\n")
          print(snap['DBClusterIdentifier'])
          for tag in snap['TagList']:
              f.write("         " + tag['Key'])


f.write('\n')
f.close()
# Write the file to an s3 bucket
s3r.Bucket('fe-rdssnapshot-report-bucket').upload_file('fe_rds_snapshot_rpt.txt','fe_rds_snapshot_rpt.txt')
    
#    rdscluster = rds.describe_db_clusters()



"""   AWS VERSION
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
import datetime
import dateutil.parser
import logging
import array as arr

from pprint import pprint

def lambda_handler(event, context):
	f = open("fe_rds_snapshot_rpt.txt", "a")



	reg_arr = []
	regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
	for region in regions:
	  reg_arr.append(region)
	  
	#pprint(reg_arr) 
	 
	for region in reg_arr:


		account_no = boto3.client('sts').get_caller_identity().get('Account')
		rdscluster = rds.describe_db_clusters()
		rdssnaps = rds.describe_db_snapshots()
		ec2 = boto3.client('ec2', region_name="us-east-2")
		s3r = boto3.resource('s3', region_name=region)
		#acct_nos = ['725837026074']

		pprint(rdscluster)
		pprint(rdssnaps)

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


		f.write('\n')    
		#rdscluster = rds.describe_db_clusters()
		#rdssnaps = rds.describe_db_snapshots()
		
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
			  f.write("===============================================  > 8wks:  DELETE  ==================================================================")
			  f.write("Account no.: " + account_no + "\nName: " + snap['DBSnapshotIdentifier'] + "\narn: " + snap['DBSnapshotArn'] + "\nresource id: " + snap['DbiResourceId'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + "  (" + str(days_since.days) + " days ago) \nTags:\n")
			  print(account_no)
			  print(snap['DBSnapshotIdentifier'])
			  print(snap['DBSnapshotArn'])
			  for tag in snap['TagList']:
				  f.write("        " + tag['Key'])

		  else:
			  f.write("==================================================   < 8wks:   KEEP  ================================================================")
			  f.write("Account no.: " + account_no + "\nName: " + snap['DBSnapshotIdentifier'] + "\narn: " + snap['DBSnapshotArn'] + "\nresource id: " + snap['DbiResourceId'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + " (" + str(days_since.days) + " days ago) \nTags:\n" )
			  print(account_no)
			  print(snap['DBSnapshotIdentifier'])
			  print(snap['DBSnapshotArn'])

			  for tag in snap['TagList']:
				  f.write("        " + tag['Key'])      
			  f.write('\n')
		  

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
			  f.write("================================================  > 8wks:    DELETE  ==================================================================")
			  f.write("Account no.: " + account_no + "\nName: " + snap['DBClusterIdentifier'] + "\narn: " + snap['DBClusterSnapshotArn'] + "\nresource id: " + snap['DBClusterSnapshotIdentifier'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + "  (" + str(days_since.days) + " days ago)  \nTags:\n")
			  print(snap['DBClusterIdentifier'])
			  for tag in snap['TagList']:
				  f.write("        " + tag['Key'])
		   
		  else:
			  f.write("============================================== < 8wks:   KEEP ======================================================================")
			  f.write("Account no.: " + account_no + "\nName: " + snap['DBClusterIdentifier'] + "\narn: " + snap['DBClusterSnapshotArn'] + "\nresource id: " + snap['DBClusterSnapshotIdentifier'] + "\nCreated: " + cd.strftime("%m-%d-%Y") + "  (" + str(days_since.days) + " days ago) \nTags:\n")
			  print(snap['DBClusterIdentifier'])
			  for tag in snap['TagList']:
				  f.write("         " + tag['Key'])


	f.write('\n')
	f.close()
	# Write the file to an ss3 bucket
	s3r.Bucket('fe-rdssnapshot-report-bucket').upload_file('fe_rds_snapshot_rpt.txt','fe_rds_snapshot_rpt.txt')

"""