import json
import os
import boto3
import base64
from botocore.exceptions import ClientError
import datetime
import logging
import dateutil.parser

ce = boto3.client('ce')

cau = ce.get_cost_and_usage(
    TimePeriod={
	
	),
	Granularity=''


# Time Period
# Granularity
#
#