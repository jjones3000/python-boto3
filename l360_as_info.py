import boto3
import json
from bson import json_util
import os
import sys
import csv
import datetime
import io
import re
import requests
import base64
import logging
import itertools, sys
import dateutil.parser
from pprint import pprint
import datetime
from json import JSONEncoder

"""
class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

"""

auto_sg = boto3.client('autoscaling')

asg = auto_sg.describe_auto_scaling_groups()
for group in asg['AutoScalingGroups']:
    pprint(group['AutoScalingGroupName'])
"""
f = open("demofile2.txt", "a")

json_object = json.dumps(asg, indent = 4, cls=DateTimeEncoder)

with open("demofile2.txt", "w") as outfile:
    outfile.write(json_object)
	
f.close()
"""