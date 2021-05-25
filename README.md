## AWS Lambda Function for RDS Automated Snapshot Removal

## Create Lambda Function

1. Log into the AWS console and navigate to AWS Lambda.
2. Click Create function
3. Give the function a name.
4. Choose python 3.7 for the runtime
5. For 'Change Default Execution Role', you may either create a new role or use an existing role. The role however, must have basic Lambda function permissions as well as full RDS access.
6. Click 'Create Function'
7. On the function screen, double click on the lambda_function.py file in the left pane to show a basic function.

## Configure Lambda Function

import json
```
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```
