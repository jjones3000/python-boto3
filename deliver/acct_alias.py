import boto3

# Create IAM client
iam = boto3.client('iam')
aa = iam.list_account_aliases()
print(aa['ResponseMetadata'])

# List account aliases through the pagination interface
paginator = iam.get_paginator('list_account_aliases')
for response in paginator.paginate():
    print(response['AccountAliases'])