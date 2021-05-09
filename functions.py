import json
import os
import boto3
import base64
from botocore.exceptions import ClientError
import datetime
import logging
import dateutil.parser

#---- tdelta

def cutoff_date(rsrc_creation, days_since):
  now = datetime.datetime.now()
  date_parts = rsrc_creation.split("-")
  year = int(date_parts[0])
  month = int(date_parts[1])
  day = int(date_parts[2])
  create_date = datetime.datetime(year,month,day)
  print("                        Create Date: " + str(create_date))
  #cd = datetime.datetime(rsrc_creation)
  #cd_dtf = datetime.datetime(cd.year,cd.month,cd.day) #cd_dtf = creation date in datetime format
  #days_since = now-create_date
  print("         Delta passed into function: " + str(days_since))
  target_date = now - (datetime.timedelta(days_since))
  #print("                        Target Date: " + str(target_date))
  #print("                         days since: " + str(days_since))
  print("         Today's date minus 30 days: " + str(target_date))
  print("Create date older than target date?: ")
  print("                            compare: " + str(create_date) + " ----- " + str(target_date))
  
  
cod = cutoff_date('2021-03-15',30)

  