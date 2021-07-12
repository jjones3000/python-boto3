#!/usr/bin/python
import os
import json
import boto3
import itertools, sys
import pprint
from pprint import pprint
from json import JSONEncoder



dynabo_table_arr = []

client = boto3.client('dynamodb')
response = client.list_tables()
#pprint(response)
#pprint(response['ResponseMetadata'])
 
ec2 = boto3.client('ec2')
s3r = boto3.resource('s3')  
 

for table in response['TableNames']:
  desc_table = client.describe_table(
    TableName = table  
  
  )
  
  
  yr = str(desc_table['Table']['CreationDateTime'].year)
  mo = str(desc_table['Table']['CreationDateTime'].month)
  day = str(desc_table['Table']['CreationDateTime'].day)
  
  print("\n")
  print(table)
  print(mo + "-" + day + "-" + yr)
  print("Read Capacity Units: " + str(desc_table['Table']['ProvisionedThroughput']['ReadCapacityUnits']))
  print("Write Capacity Units: " + str(desc_table['Table']['ProvisionedThroughput']['WriteCapacityUnits']))
  print("Table Size (bytes): " + str(desc_table['Table']['TableSizeBytes']))
  table_size = desc_table['Table']['TableSizeBytes']
  max_read_capacity = desc_table['Table']['ProvisionedThroughput']['ReadCapacityUnits']
  max_write_capacity = desc_table['Table']['ProvisionedThroughput']['WriteCapacityUnits']
  print(table_size)
  print("\n")
 
  if(table_size < 0.5 and max_read_capacity > 0 and max_write_capacity > 1):
    #response = client.delete_table(
    #TableName=table
    #)
    print(table)
  else:
      continue
