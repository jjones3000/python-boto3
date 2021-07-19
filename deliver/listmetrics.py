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
from datetime import datetime, timedelta
import dateutil.parser
import logging
import array as arr

cloudwatch_client = boto3.client('cloudwatch')

response = cloudwatch_client.list_metrics()

# # Create CloudWatch client
# cloudwatch = boto3.client('cloudwatch')

# # List metrics through the pagination interface
# paginator = cloudwatch.get_paginator('list_metrics')
# for response in paginator.paginate(Dimensions=[{'Name': 'LogGroupName'}],
                                   # MetricName='IncomingLogEvents',
                                   # Namespace='AWS/Logs'):
    # pprint(response['Metrics'])


def get_req_count(region, lb_name):
    client = boto3.client('cloudwatch', region_name=region)
    count = 0
    response = client.get_metric_statistics(
            Namespace="AWS/ApplicationELB",
            MetricName="RequestCount",
            Dimensions=[
                {
                    "Name": "LoadBalancer",
                    "Value": lb_name
                },
            ],
            StartTime=datetime.now() - timedelta(days=7),
            EndTime=datetime.now(),
            Period=86460,
            Statistics=[
                "Sum",
            ]
    )   

    #print(response2)        
    for r in response['Datapoints']:
        count = (r['Sum'])

    return count  

print(get_req_count('us-east-2','app/lb-test-traffic/3abff66fd69a6b1c'))

#pprint(response)

# metric_data = cloudwatch_client.get_metric_data(
    # MetricDataQueries=[
        # {
            # 'Id': 'string',
            # 'MetricStat': {
                # 'Metric': {
                    # 'Namespace': 'AWS/ApplicationELB',
                    # 'MetricName': 'RequestCount',
                    # 'Dimensions': [
                        # {
                            # 'Name': 'LoadBalancer',
                            # 'Value': 'app/lb-test-traffic/3abff66fd69a6b1c'
                        # },
                    # ]
                # },
                # 'Period': 60,
                # 'Stat': 'string',
                # 'Unit': 'Count',
            # },

            # 'Label': 'string',
            # 'ReturnData': True,

        # },
    # ],
    # StartTime=1,
    # EndTime=5,
    # NextToken='string',
    # MaxDatapoints=100,

# )