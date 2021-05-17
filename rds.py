<<<<<<< HEAD
#!/bin/bash
=======
>>>>>>> 1ebd3473117509d689c758c212efdb0043f2fd30
import json
import os
import boto3
import base64
from botocore.exceptions import ClientError
import datetime
import logging
import dateutil.parser
import array as arr
<<<<<<< HEAD
from pprint import pprint

rds = boto3.client('rds')
  
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
=======

rds = boto3.client('rds')
iamc = boto3.client('iam')
iamr = boto3.resource('iam')
s3 = boto3.resource('s3')
s3c = boto3.client('s3')


print('\n')    
rdscluster = rds.describe_db_clusters()
rdssnaps = rds.describe_db_snapshots()
for snap in rdssnaps['DBSnapshots']:

>>>>>>> 1ebd3473117509d689c758c212efdb0043f2fd30
  now = datetime.datetime.now()
  cd = snap['SnapshotCreateTime']
  cd_dtf = datetime.datetime(cd.year,cd.month,cd.day) #cd_dtf = creation date in datetime format
  days_since = now-cd_dtf
  past_fifty_six = now - (datetime.timedelta(56))
<<<<<<< HEAD
 
  
  name = snap['DBSnapshotIdentifier']
  doffset=65-len(name)
  pstr = ' '*doffset + name
        
  if cd_dtf < past_fifty_six:

      print("Creation Date: " + cd.strftime("%m-%d-%Y") + "  " + str(days_since.days) + " days old - " + pstr + " > 8wks:    DELETE ")
      for tag in snap['TagList']:
          print("        Tag: " + tag['Value'])

  else:

      print("Creation Date: " + cd.strftime("%m-%d-%Y") + "  " + str(days_since.days) + " days old - " + pstr +  "  < 8wks:     KEEP" )
      for tag in snap['TagList']:
          print("        Tag: " + tag['Value'])      

=======
  print("what is today minus 56?: " + str(past_fifty_six))
  print("what is days since: " + str(days_since))
  print("Database snapshot id: " + snap['DBSnapshotIdentifier'])
  print('\n')
  
  
  
		
  if cd_dtf < past_fifty_six:
      print(" Name: " + snap['DBSnapshotIdentifier'] + " Date: " + str(snap['SnapshotCreateTime']) + " > 8wks: yes ")
  else:
      print(" Name: " + snap['DBSnapshotIdentifier'] + " Date: " + str(snap['SnapshotCreateTime']) + " > 8wks: no" ) 
  print('\n')  
  #print(snap['SnapshotCreateTime'])
  #print(rdssnaps['DBSSnapshots'][0])
  #s3c.put_object(Body=rdssnaps, Bucket='jeffs-aws-serverless', Key='output.txt')
  #for snap in rdssnaps:
  #for snap in rdssnaps:
  #print(snap)
>>>>>>> 1ebd3473117509d689c758c212efdb0043f2fd30


# The portion below is for mysql based dbs

<<<<<<< HEAD
  
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

      print("Creation Date: " + cd.strftime("%m-%d-%Y") + "  " + str(days_since.days) + " days old - " + cstr + " > 8wks:    DELETE")
      for tag in snap['TagList']:
          print("        Tag: " + tag['Value'])
   
  else:

      print("Creation Date: " + cd.strftime("%m-%d-%Y") + "  " + str(days_since.days) + " days old - " + cstr + "  < 8wks:     KEEP" )
      for tag in snap['TagList']:
          print("        Tag: " + tag['Value'])

=======
print('\n')    
rdscluster = rds.describe_db_clusters()
rdssnaps = rds.describe_db_cluster_snapshots()
for snap in rdssnaps['DBClusterSnapshots']:

  now = datetime.datetime.now()
  cd = snap['SnapshotCreateTime']
  cd_dtf = datetime.datetime(cd.year,cd.month,cd.day) #cd_dtf = creation date in datetime format
  print("DB or cluster created on this date: "+ str(cd_dtf))
  days_since = now-cd_dtf
  past_fifty_six = now - (datetime.timedelta(56))
  print("what is today minus 56?: " + str(past_fifty_six))
  print("what is days since: " + str(days_since))
  print("Database snapshot id: " + snap['DBClusterSnapshotIdentifier'])
  print('\n')

  if cd_dtf < past_fifty_six:
      print(" Name: " + snap['DBClusterSnapshotIdentifier'] + " Date: " + str(snap['SnapshotCreateTime']) + " > 8wks: yes ")
  else:
      print(" Name: " + snap['DBClusterSnapshotIdentifier'] + " Date: " + str(snap['SnapshotCreateTime']) + " > 8wks: no" ) 
  print('\n')  
  #print(snap['SnapshotCreateTime'])
  #print(rdssnaps['DBSSnapshots'][0])
  #s3c.put_object(Body=rdssnaps, Bucket='jeffs-aws-serverless', Key='output.txt')
  #for snap in rdssnaps:
  #for snap in rdssnaps:
  #print(snap)
>>>>>>> 1ebd3473117509d689c758c212efdb0043f2fd30
