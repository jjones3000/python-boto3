#!/bin/bash
import boto3
import json
#from bson import json_util
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

#f = open("ec2.txt", "a")
ec2c = boto3.client('ec2')
desc_instances = ec2c.describe_instances()
# f.write(str(desc_instances))
# f.close()
x=0
for instance in desc_instances:
    #pprint(desc_instances['Reservations'][0]['Instances'][0])
    #pprint(desc_instances['Reservations'][0]['Instances'][0]['InstanceType'])
    pprint(desc_instances['Reservations'][x]['Instances'][0]['InstanceId'])
    # pprint(desc_instances['Reservations'][0]['Instances'][0]['InstanceId'])
    # pprint(desc_instances['Reservations'][0]['Instances'][1]['InstanceId'])
    # pprint(desc_instances['Reservations'][0]['Instances'][2]['InstanceId'])
    # pprint(desc_instances['Reservations'][0]['Instances'][3]['InstanceId'])
    # pprint(desc_instances['Reservations'][0]['Instances'][4]['InstanceId'])
    #pprint(desc_instances['Reservations'][0]['Instances'][x]['ImageId'])
    #print(pprint(desc_instances['Reservations'][0]['Instances'][2]['InstanceId']))
    x = x + 1

  #pprint(desc_instances['Reservations'][0]['Instances'][0]['CapacityReservationSpecification'])