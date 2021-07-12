import os
import csv
import json
import boto3
import itertools, sys
import pprint
from pprint import pprint
from json import JSONEncoder
import datetime

support_client = boto3.client('support')
csv_file = open('all_idle_rds.csv', 'w')
obj = csv.writer(csv_file, delimiter=',')
idle_rds_check_id = ''
checks_response = support_client.describe_trusted_advisor_checks(language='en')
for check_detail in checks_response['checks']:
    if check_detail['category'] == 'cost_optimizing' and check_detail['name'] == 'Amazon RDS Idle DB Instances':
         idle_rds_check_id = check_detail['id']
         csv_header = check_detail['metadata']
         obj.writerow(csv_header)

get_check_result = support_client.describe_trusted_advisor_check_result(
    checkId=idle_rds_check_id,
    language='en'
)
for idle_rds in get_check_result['result']['flaggedResources']:
    obj.writerow(idle_rds['metadata'])