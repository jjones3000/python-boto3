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

rds = boto3.client('rds')
  
rdscluster = rds.describe_db_clusters()
rdssnaps = rds.describe_db_snapshots()


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
"""
for snap in rdssnaps['DBSnapshots']:

    pprint(snap)
    rds = boto3.client('rds')
    iamc = boto3.client('iam')
    iamr = boto3.resource('iam')
    s3 = boto3.resource('s3')
    s3c = boto3.client('s3')
	
"""	
	
print(boto3.client('sts').get_caller_identity().get('Account'))