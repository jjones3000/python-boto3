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






ec2 = boto3.client('ec2')
response = ec2.describe_instances()
pprint(response)												
