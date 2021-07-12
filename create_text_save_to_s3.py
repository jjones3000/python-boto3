#!/usr/bin/python
import os
import json
import boto3
import itertools, sys
import pprint
from pprint import pprint
from json import JSONEncoder
import datetime

x = datetime.datetime.now()

#print(str(x.month) + "-" + str(x.day) + "-" + str(x.year))
date_stamp = str(x.month) + "-" + str(x.day) + "-" + str(x.year) + "\n"

s3 = boto3.client('s3')
s3r = boto3.resource('s3')

f = open("demofile2.txt", "a")
f.write(date_stamp)
f.write("Now the file has more content!\n")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
#print(f.read())
print(f.read())
#s3.Object('jeffs-test-bucket', 'demofile100.txt').put(Body=open('/tmp/demofile2.txt', 'rb'))
s3r.Bucket('jeffs-test-bucket').upload_file('demofile2.txt','demofile20.txt')