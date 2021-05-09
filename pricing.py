import json
import requests
import os
import boto3
import base64
from botocore.exceptions import ClientError
import datetime
import logging
import dateutil.parser
from pprint import pprint

pricing = boto3.client('pricing')

services = pricing.describe_services()

#pprint(services)

f = open("demofile2.txt", "a")

json_object = json.dumps(services, indent = 4)

#open and read the file after the appending:
with open("demofile2.txt", "w") as outfile:
    outfile.write(json_object)



#obj = json.loads(services)
  
# Pretty Print JSON
#json_formatted_str = json.dumps(obj, indent=4)
#print(json_formatted_str)
f.close()