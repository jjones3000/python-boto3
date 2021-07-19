import os
import csv
import json
import boto3
import itertools, sys
import pprint
from pprint import pprint
from json import JSONEncoder
import datetime
from datetime import datetime, timedelta

x = datetime.now()
date_stamp = str(x.month) + "-" + str(x.day) + "-" + str(x.year) + "\n"
start_time = datetime.now() - timedelta(days=7)
end_time = datetime.now()
list_of_rds_id = []

s3r = boto3.resource('s3')
cloudwatch_client = boto3.client('cloudwatch', region_name='us-east-2')

f = open("idle_rds_instances.txt", "a")
f.write(date_stamp)

for rds_id in list_of_rds_id:
    print(rds_id)
    rds_conn_metric = cloudwatch_client.get_metric_statistics(
        Namespace='AWS/RDS',
        MetricName='DatabaseConnections',
        Dimensions=[
            {
                'Name': 'DBInstanceIdentifier',
                'Value': rds_id
            },
        ],
        StartTime= start_time,
        EndTime= end_time,
        Period=3600 * 24,
        Statistics=[
            'Average',
        ],
        Unit='Count'
    )
    is_idle = True
    for day_metric in rds_conn_metric['Datapoints']:
        if day_metric['Average'] == 0.0:
            is_idle &= True
        else:
            is_idle &= False
    if is_idle:
        print(rds_id + ' is idle for last 7 days.')
        """
        cloudwatch_client.create_db_cluster_snapshot(
             DBClusterSnapshotIdentifier=rds_id
        )
        
        delete_db_instance(
            DBInstanceIdentifier=rds_id,
            SkipFinalSnapshot=False,
            FinalDBSnapshotIdentifier='final_snap_'+rds_id,
            DeleteAutomatedBackups=True
        )
        """
f.close()
s3r.Bucket('jeffs-test-bucket').upload_file('unattached_eips.txt','unattached_eips.txt')



""" AWS VERSION

import os
import csv
import json
import boto3
import itertools, sys
import pprint
from pprint import pprint
from json import JSONEncoder
from datetime import datetime
from datetime import datetime, timedelta


def lambda_handler(event, context):
    x = datetime.now()
    date_stamp = str(x.month) + "-" + str(x.day) + "-" + str(x.year) + "\n"
    start_time = datetime.now() - timedelta(days=7)
    end_time = datetime.now()
    list_of_rds_id = []
    
    s3r = boto3.resource('s3')
    cloudwatch_client = boto3.client('cloudwatch', region_name='us-east-2')
    
    f = open("/tmp/idle_rds_instances.txt", "a")
    f.write(date_stamp)
    
    for rds_id in list_of_rds_id:
        rds_conn_metric = cloudwatch_client.get_metric_statistics(
            Namespace='AWS/RDS',
            MetricName='DatabaseConnections',
            Dimensions=[
                {
                    'Name': 'DBInstanceIdentifier',
                    'Value': rds_id
                },
            ],
            StartTime= start_time,
            EndTime= end_time,
            Period=3600 * 24,
            Statistics=[
                'Average',
            ],
            Unit='Count'
        )
        is_idle = True
        for day_metric in rds_conn_metric['Datapoints']:
            if day_metric['Average'] == 0.0:
                is_idle &= True
            else:
                is_idle &= False
        if is_idle:
            fwrite(rds_id + ' is idle for last 7 days.')
            
            #### BLOCK COMMENT
            # cloudwatch_client.create_db_cluster_snapshot(
                 # DBClusterSnapshotIdentifier=rds_id
            # )
            
            # delete_db_instance(
                # DBInstanceIdentifier=rds_id,
                # SkipFinalSnapshot=False,
                # FinalDBSnapshotIdentifier='final_snap_'+rds_id,
                # DeleteAutomatedBackups=True
            # )

           
    f.close()
    s3r.Bucket('jeffs-test-bucket').upload_file('/tmp/idle_rds_instances.txt','idle_rds_instances.txt')
"""