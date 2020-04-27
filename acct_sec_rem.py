import os
import json
import boto3
import openpyxl
from botocore.exceptions import ClientError
from datetime import datetime
import logging
import pytz
import tzlocal
import dateutil.parser
import array as arr
import pandas as pd

iamc = boto3.client('iam')
iamr = boto3.resource('iam')
x=0

for user in iamc.list_users()['Users']:
  user_name = user['UserName']
  get_user = iamc.get_user(UserName=user_name)
  print("UserName: " + user_name)  
  print("Create Date: " + str(get_user['User']['CreateDate']))
  try:
    ssh_keys = iamc.list_ssh_public_keys(UserName=user_name)
    iam_keys = iamc.list_access_keys(UserName=user_name)
    user_rsc = iamr.User(user_name)
    last_login = user_rsc.password_last_used
    num_iamkeys = len(iam_keys['AccessKeyMetadata'])
    
    print("Last login: " + str(last_login))
    print("API last used: " + str(API_last_used))
     
    for iamkey in iam_keys.values():
      num_iamkeys = len(iamkey)
      if num_iamkeys >= 1:
        for eachi in iamkey:
          #print(eachi['AccessKeyId'])
          API_last_used = iamc.get_access_key_last_used(AccessKeyId=eachi['AccessKeyId'])
          print("AccessKeys: " + str(API_last_used['AccessKeyLastUsed']['LastUsedDate']))
        else:
          break
  
    for sshkey in ssh_keys.values():
      print(user_name) # prints all users
      num_sshkeys = len(sshkey)
      if num_sshkeys >= 1:
        for eachs in sshkey:
          print("SSHKeys: " + user_name + " - " + eachs['SSHPublicKeyId']) # prints users  and the keys of those who have ssh keykey)
          print("")
        else:
          break
       
            response = client.delete_access_key(
            UserName= user_name,
            AccessKeyId = each['SSHPublicKeyId']
            )
         
        
    x = x + 1
    
  except:
    continue  
