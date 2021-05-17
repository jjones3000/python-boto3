import os
import json
import boto3
from boto3.session import Session
#import openpyxl
from botocore.exceptions import ClientError
import datetime
import logging
#import pytz
#import tzlocal
import dateutil.parser
from pprint import pprint
###
#--- [ref] change region programmatically
#https://russell.ballestrini.net/setting-region-programmatically-in-boto3/

#????

#--- RESOURCES AND CLIENTS ---------
#====================================
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
s3Resource = boto3.resource('s3')
#bclient = boto3.client('ce')
athena_client = boto3.client('athena')
budgets_client = boto3.client('budgets')
dynamodb = boto3.resource('dynamodb')
ec2_client = boto3.client('ec2')
rsclient = boto3.client('redshift')
iamc = boto3.client('iam')

reg_arr = []
count = 0

#=====================================
"""
https://www.decalage.info/en/python/print_list

"""

#aws_acct_num = boto3.client('sts').get_caller_identity()['Account']


#-- EVENTS RULE REFERENCE
"""https://github.com/lroguet/amzn-cloudformation/blob/master/lambda/scheduled-lambda.yml
"""

#-- ATTACH IAM POLICY TO A ROLE
"""
response = client.attach_role_policy(
    RoleName='string',
    PolicyArn='string'
)

"""

#--- LIST ALL IAM USERS FOR AN ACCOUNT
"""
for user in iamc.list_users()['Users']:
  user_name = user['UserName']
  print(user_name)
"""
#--- PRINT ALL IAM ACCESS KEYS FOR USERS WHO HAVE ONE OR MORE
"""
  keys = iamc.list_access_keys(UserName=user)
  #print(keys)
  for b in keys['AccessKeyMetadata']:
      username = b['UserName']
      accesskeyid = b['AccessKeyId']
      status = b['Status']
      createdate = str(b['CreateDate']) # creation date
      print("{0:<20} {1:<25} {2:<15} {3:<10}".format(username, accesskeyid, status, createdate))
      #access_key = iam.AccessKey(username,accesskeyid)
        #access_key.deactivate()
"""

#--- PRINT ALL SSH KEYS FOR USERS WHO HAVE ONE OR MORE
"""
iamc = boto3.client('iam')
iamr = boto3.resource('iam')
x=0
for user in iamc.list_users()['Users']:

  user_name = user['UserName']  
 #['SSHPublicKeys'] 
 #['ResponseMetaData'] 
  try:
    response = iamc.list_ssh_public_keys(UserName=user_name)
    for item in response.values():
      #print(user_name) # prints all users
      num_items = len(item)
      if num_items >= 1:
        for each in item:
          print(each['SSHPublicKeyId']) # prints users  and the keys of thosewho have ssh keys
    x = x + 1
  except:
    continue
"""
#--- REPORT CLASS
"""
class Report:
  def __init__(aws_acct_num, creation_date,rsrc_type,rsrc_name,owner):
    self.aws_acct_num = aws_acct_num
    slef.reation_date = reation_date
    self.rsrc_type = rsrc_type
    self.rsrc_name = rsrc_name
    self.owner = owner

  def write_report(aws_acct_num, creation_date,rsrc_type,rsrc_name,owner):
    wb = openpyxl.load_workbook('inventory.xlsx')
    wb.sheetnames
    sheet = wb.active
    currSheet = sheet.title
    
    sheet.append((aws_acct_num,readable_date,"s3",bucket['Name'], bucket_owner))
    print("mark")
    wb.save('inventory.xlsx') 
"""
#--- CREATE CLOUDWATCH CLIENT
"""
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

for region in regions:
  print(region)
  bclient = boto3.client('redshift', region_name = region)
  cluster_list = response = bclient.describe_cluster_parameters(
  ParameterGroupName = 'default',
  )
  for cluster in cluster_list:
    pprint(cluster)
"""    
    
    
#--- GET AWS ACCOUNT NUMBER
"""
boto3.client('sts').get_caller_identity()['Account']
def lambda_handler(event, context):
  print("My account ID is %s" % get_account_id(context))

"""

#--- COMPARING DATES IN PYTHON

time=[]
dt = datetime.datetime.now()
time1 = datetime.datetime(2019, 11, 1)
time2 = datetime.datetime(2020, 3, 30)
time.append(time1)
time.append(time2)
print(time1)
print(time2)
print(time2 - (datetime.timedelta(30)))
past_thirty = time2 - (datetime.timedelta(30))

for x in time:

  if(x <= time2 and x >= past_thirty):
    print(str(x) + " this time is in range")
  else:
    print(str(x) + " this time not in range")


#--- RETRIEVE S3 BUCKET POLICY
"""
result = s3.get_bucket_policy(Bucket='74481-wfm-eidin-flq-explore-sbx-logging')
print(result['Policy'])
"""
#--- CLOUDFORMATION
"""
cfn.list_stacks()
print(type(cfn))
"""

#--- LIST ALL STACKS IN AN ACCOUNT
"""
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
count = 1
for region in regions:
  reg_arr.append(region)
  cfn = boto3.client('cloudformation', region_name = region)
  for stack in cfn.list_stacks(
    StackStatusFilter = [
    'CREATE_COMPLETE', 'UPDATE_COMPLETE'
    ])['StackSummaries']:
      #print('{0}:{1}'.format(stack['StackName'], stack['StackId']))
      count += 1
      print(stack['StackName'])
      #print(stack['StackId'])
      continue
print("here's the count: " + str(count))


#for reg in reg_arr:
  #print(reg)


"""

#--- LIST ALL REGIONS
"""
ec2_client = boto3.client('ec2')
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
for region in regions:
  reg_arr.append(region)

for region in reg_arr:
  print(region)
#regions = ec2_client.describe_regions().get('Regions',[] )
#print(reg_arr)
"""

#--- PRINT ALL REGIONS THAT ARE ACTIVE
"""
for region in regions:
  reg_arr.append(region)
  continue
"""


#--- PRINT THE NUMBER OF BUCKETS
"""
print("lot's of buckets here guys:"+str(len(response['Buckets'])))
"""



#--- CREATE AN S3 BUCKET POLICY
"""
bucket_name = 'BUCKET_NAME'
bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{bucket_name}/*'
    }]
}

#--- Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

# Set the new policy
s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)

"""

#--- GET S3 BUCKET TAGS
"""
s3 = boto3.client('s3')
buckets = s3_client.list_buckets()
s3r = boto3.resource('s3')

response_c = s3.list_buckets()
buckets = response_c
for bucket in response_c['Buckets']:
  try:
    #print(bucket['Name'])
    raw_date = bucket['CreationDate']
    readable_date = raw_date.strftime("%m-%d-%Y")
    time_today = datetime.datetime.now()
    past_thirty = time_today - (datetime.timedelta(30))
    bucket_tag = s3.get_bucket_tagging(Bucket = bucket['Name'])
    bucket_owner_tag = bucket_tag['TagSet'][0]['Key']
    if(bucket_owner_tag == 'owner'):
      print(bucket_tag['TagSet'][0]['Value'])
    else:
      continue
  except:
    continue
  #print("Bucket Name: " + bucket['Name']+ " -- Creation Date: " + readable_date)

[COMMENT]
for bucket in buckets:
  try:
      print(bucket)
      response = s3_client.get_bucket_tagging(Bucket=bucket)
      print(response['owner'])
      #tagset = response['TagSet']
  except ClientError:
      print(bucket, "does not have tags, adding tags")
[END_COMMENT]

"""

#--- S3 - LIST BUCKET NAMES AND CREATION DATES -- https://www.w3schools.com/python/python_datetime.asp
"""

s3 = boto3.client('s3')
buckets = s3_client.list_buckets()
s3r = boto3.resource('s3')
aws_acct_num = boto3.client('sts').get_caller_identity()['Account']
wb = openpyxl.load_workbook('inventory.xlsx')
wb.sheetnames
sheet = wb.active
currSheet = sheet.title
response_c = s3_client.list_buckets()
buckets = response_c
for bucket in response_c['Buckets']:
  try:
    raw_date = bucket['CreationDate']
    readable_date = raw_date.strftime("%m-%d-%Y")
    time_today = datetime.datetime.now()
    past_thirty = time_today - (datetime.timedelta(30))
    bucket_tag = s3.get_bucket_tagging(Bucket = bucket['Name'])
    bucket_owner_tag = bucket_tag['TagSet'][0]['Key']

    if(raw_date.date() >= past_thirty.date()):
      bucket_tagging = s3r.get_bucket_tagging(Bucket = bucket['Name'])
      bucket_owner_tag = bucket_tag['TagSet'][0]['Key']    
      #print(bucket['Name'])
      print(bucket_owner_tag)
    if(bucket_owner_tag == 'owner'):
      bucket_owner = bucket_tag['TagSet'][0]['Value']
      print(bucket_owner)
    else:
      bucket_owner = "no tag found"
      continue

    
    sheet.append((aws_acct_num,readable_date,"s3",bucket['Name'], bucket_owner))
    #print(bucket)
    #sheet.append(B,[readable_date])
    #print(raw_date.strftime("%x"))
    #print(bucket)  
    #print(bucket['CreationDate'])

    wb.save('inventory.xlsx') 
  except:
    continue
"""
 
#--- S3 LOGGING INFO
"""
bucket_logging = s3Resource.BucketLogging('74481-jeffs-test-land')
print(bucket_logging)
"""
#--- s3 ACL
"""
s3ACL = s3.get_bucket_acl('2120950-land')
s3ACL = s3.acl('2120950-land')
print(s3ACL)

"""
#--- OPEN OPENPYXL
""""
wb = openpyxl.load_workbook('inventory.xlsx')
wb.sheetnames
sheet = wb.active
currSheet = sheet.title

names=[]

for bucket in response['Buckets']:
  try:
    bucket_tagging = s3.get_bucket_tagging(Bucket = bucket['Name'])
    #print(bucket['Name'])
    #print(bucket_tagging)
    sheet.append([bucket['Name']])
    
   
    
    #print(get_s3_keys(bucket['Name']))
  except:
    continue
    #print("XXX")
    

names.append(names)
wb.save(filename='/mnt/c/Users/jjone/Downloads/sbx_python_boto/inventory.xlsx')
#wb.save()  
"""  
    
    
"""
print(type(sheet))

for row in sheet.values:
  for value in row:
    print(value)

print(currSheet)
"""

"""
x = 1
#print(f'  {bucket["Name"]}')

workbook = Workbook()
sheet = workbook.active
for bucket in response['Buckets']:
  
  print(sheet["A"+str(x)])

  x+=x
  
workbook.save(filename="./inventory.xlsx")
LANDING_BUCKET_NAME = os.environ['LANDING_BUCKET_NAME']
PERSIST_BUCKET_NAME = os.environ['PERSIST_BUCKET_NAME']
SNS = os.environ['SNS']


this will get all the regions that dynamoDB is available in

s = Session()
dynamodb_regions = s.get_available_regions('dynamodb')
for dynamo_region in dynamodb_regions:
  print(dynamo_region)
  
"""


#---- GET A LIST OF ALL TOPIC ARNS FROM THE RESPONSE
"""
topics = [topic['TopicArn'] for topic in response['Topics']]

 Print out the topic list
print("Topic List: %s" % topics)
snstopic = 'arn:aws:sns:us-east-1:744810512381:NotifyJeff'
if snstopic in topics:
    #print("we found your topic")
"""

"""
    # log event and context attributes
    print(json.dumps(event, default=str, indent=4))
    print(json.dumps(context.__dict__, default=str, indent=4))
     
    # get bucket name and object key attributes from event object
   
    source_bucket_name = event['Records'][0]['s3']['bucket']['name']
   
    source_object_key = urllib.parse.unquote(event['Records'][0]['s3']['object']['key'])
    print(f"{source_object_key} PUT to {source_bucket_name}")
"""
"""    
    f = open("/tmp/jeffstest.txt", "a")
    for x in event:
        print(x)
        f.write(x)
    f.close()
    s3.Object('jeffs-test-land-copy1', 'jeffstest.txt').put(Body=open('/tmp/jeffstest.txt', 'rb'))
    #s3.upload_fileobj(f, "jeffs-test-land-main", "somefile")
""" 
"""
    if not source_bucket_name == LANDING_BUCKET_NAME:
        raise EnvironmentError("event source_bucket_name NOT equals environment LANDING_BUCKET_NAME")
    
    # build copy source and target object instance from event object attributes
    copy_source = {'Bucket': source_bucket_name, 'Key': source_object_key}
    target_obj = s3.Object(PERSIST_BUCKET_NAME, source_object_key)
    
    print(f"{source_object_key} COPY to {PERSIST_BUCKET_NAME}")
    target_obj.copy_from(CopySource=copy_source)
    
    print(f"wait for {source_object_key} to exist in {PERSIST_BUCKET_NAME}")
    target_obj.wait_until_exists()
    
    print(f"{source_object_key} COPY to {PERSIST_BUCKET_NAME} successful")
"""  
#--- scrap
"""
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
s3r = s3_client.list_buckets()
buckets = s3r
for bucket in s3r['Buckets']:
  

  bucket_tagging = s3r.BucketTagging(Bucket = bucket['Name'])
  #print(bucket['Name'])
  print(bucket_tagging)
  #sheet.append([bucket['Name']])
    
   
    
    #print(get_s3_keys(bucket['Name']))
"""

