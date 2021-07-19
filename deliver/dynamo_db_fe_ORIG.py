#!/usr/bin/python
import os
import json
import boto3
import itertools, sys
import pprint
from pprint import pprint
from json import JSONEncoder
import datetime
import dateutil.parser

dynabo_table_arr = []

client = boto3.client('dynamodb')
response = client.list_tables()
#pprint(response)
#pprint(response['ResponseMetadata'])
 
ec2 = boto3.client('ec2')
s3r = boto3.resource('s3')  

f = open("fe_dynamodb_table_rpt.txt", "a")

for table in response['TableNames']:
  desc_table = client.describe_table(
    TableName = table  
  
  )
  
  
  yr = str(desc_table['Table']['CreationDateTime'].year)
  y = desc_table['Table']['CreationDateTime'].year
  mo = str(desc_table['Table']['CreationDateTime'].month)
  m = desc_table['Table']['CreationDateTime'].month
  day = str(desc_table['Table']['CreationDateTime'].day)
  d = desc_table['Table']['CreationDateTime'].day
  
  cd_dtf = datetime.datetime(y,m,d)#cd_dtf = creation date in datetime format
  
  f.write("\n")
  f.write(table)
  f.write(mo + "-" + day + "-" + yr)
  f.write("Read Capacity Units: " + str(desc_table['Table']['ProvisionedThroughput']['ReadCapacityUnits']))
  f.write("Write Capacity Units: " + str(desc_table['Table']['ProvisionedThroughput']['WriteCapacityUnits']))
  f.write("Table Size (bytes): " + str(desc_table['Table']['TableSizeBytes']))
  table_size = desc_table['Table']['TableSizeBytes']
  max_read_capacity = desc_table['Table']['ProvisionedThroughput']['ReadCapacityUnits']
  max_write_capacity = desc_table['Table']['ProvisionedThroughput']['WriteCapacityUnits']
  f.write(str(table_size))
  f.write("\n")
 
  if(table_size < 0.5 and max_read_capacity > 0 and max_write_capacity > 1):
    #response = client.delete_table(
    #TableName=table
    #)
    f.write(table)
  else:
      continue
	  
f.close()

# Write the file to an ss3 bucket
s3r.Bucket('jeffs-test-bucket').upload_file('fe_dynamodb_table_rpt.txt','fe_dynamodb_table_rpt.txt')

""" AWS VERSION

import os
import json
import boto3
import itertools, sys
import pprint
from pprint import pprint
from json import JSONEncoder
import datetime
import dateutil.parser


def lambda_handler(event, context):
	dynabo_table_arr = []
	
	client = boto3.client('dynamodb')
	response = client.list_tables()
	#pprint(response)
	#pprint(response['ResponseMetadata'])
	 
	ec2 = boto3.client('ec2')
	s3r = boto3.resource('s3')  
	
	f = open("/tmp/fe_dynamodb_table_rpt.txt", "a")
	
	for table in response['TableNames']:
	  desc_table = client.describe_table(
	    TableName = table  
	  
	  )
	  
	  
	  yr = str(desc_table['Table']['CreationDateTime'].year)
	  y = desc_table['Table']['CreationDateTime'].year
	  mo = str(desc_table['Table']['CreationDateTime'].month)
	  m = desc_table['Table']['CreationDateTime'].month
	  day = str(desc_table['Table']['CreationDateTime'].day)
	  d = desc_table['Table']['CreationDateTime'].day
	  
	  cd_dtf = datetime.datetime(y,m,d)#cd_dtf = creation date in datetime format
	  
	  f.write("\n")
	  f.write(table)
	  f.write(mo + "-" + day + "-" + yr)
	  f.write("Read Capacity Units: " + str(desc_table['Table']['ProvisionedThroughput']['ReadCapacityUnits']))
	  f.write("Write Capacity Units: " + str(desc_table['Table']['ProvisionedThroughput']['WriteCapacityUnits']))
	  f.write("Table Size (bytes): " + str(desc_table['Table']['TableSizeBytes']))
	  table_size = desc_table['Table']['TableSizeBytes']
	  max_read_capacity = desc_table['Table']['ProvisionedThroughput']['ReadCapacityUnits']
	  max_write_capacity = desc_table['Table']['ProvisionedThroughput']['WriteCapacityUnits']
	  f.write(str(table_size))
	  f.write("\n")
	 
	  if(table_size < 0.5 and max_read_capacity > 0 and max_write_capacity > 1):
	    #response = client.delete_table(
	    #TableName=table
	    #)
	    f.write(table)
	  else:
	      continue
		  
	f.close()
	
	# Write the file to an ss3 bucket
	s3r.Bucket('jeffs-test-bucket').upload_file('/tmp/fe_dynamodb_table_rpt.txt','fe_dynamodb_table_rpt.txt')
"""
