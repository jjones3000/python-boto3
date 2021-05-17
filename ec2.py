#!/bin/bash
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


# describe_spot_price_history()



ec2c = boto3.client('ec2')





# ec2s = ec2c.describe_instances()
# pprint(ec2s)





# for instance in ec2s:
    # inst = ec2s['Reservations'][0]['Instances'][0]['ImageId']
    # inst_type = ec2s['Reservations'][0]['Instances'][0]['InstanceType']
    
    # acct_no = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['OwnerId']
    # pub_ip = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp']
    # pvt_ip = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddress']
    # secgrp = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Groups'][0]['GroupId']
    # status = ec2s['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Status']
    # core_ct = ec2s['Reservations'][0]['Instances'][0]['CpuOptions']['CoreCount']
    # print("\n\n")
    # print("-------- Instance Detail ------------")
    # print("\n")
    # print("aws account number:  " + acct_no)
    # print("           ImageId:  " + inst)
    # print(" availability zone:  " + inst_type)
    # print("          PublicIp:  " + pub_ip)
    # print("        Private IP:  " + pvt_ip)
    # print("    Security Group:  " + secgrp)
    # print("            Status:  " + status)
    # print("        Core Count:  " + str(core_ct))
    # print("\n")
    # print("--------------------------------------\n\n")