#!/usr/bin/python

import os
import json
import boto3

client = boto3.client('ec2')
addresses = client.describe_addresses()

print(addresses)