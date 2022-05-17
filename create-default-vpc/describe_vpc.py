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
import time
import random
import string

client =  boto3.client("ec2")
response = client.describe_vpcs()
pprint(response)
