import os
import json
import boto3

cc = boto3.client('codecommit')
repo_list = cc.list_repositories()
x = 0

for repo in repo_list:
  print(repo_list)
  #print(repo_list['repositories'][x]['repositoryName'])
  x = x + 1