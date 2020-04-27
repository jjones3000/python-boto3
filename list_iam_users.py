import os
import json
import boto3

iamc = boto3.client('iam')


#--- LIST ALL IAM USERS FOR AN ACCOUNT

for user in iamc.list_users()['Users']:
  user_name = user['UserName']
  print(user_name)
