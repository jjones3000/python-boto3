import boto
import boto.ec2.elb
import boto.ec2.cloudwatch
import datetime
import csv
import boto.rds
import datetime
import itertools
from boto import ec2
from boto.ec2.cloudwatch import CloudWatchConnection
import xlwt
import glob
import os
#Generating all the regions
regions=boto.ec2.elb.regions()
#To identify Idle ELB (a load balancer has no active instance, no healthy instance and load balancer has less then 100 request for last 7 days

def idle_elb():
    with open('idle_elb.csv','w+') as cw:
        csvwriter=csv.writer(cw,delimiter=',')
        data=[ 'Region Name','ELB Name','Instance ID' ,'Status','Reason' ]
        csvwriter.writerow(data)
        for r in regions:
            name=str(r.name)
            if not (name == 'us-gov-west-1' or name == 'cn-north-1'):
                con=ec2.elb.connect_to_region(r.name)
                #Connecting to Cloudwatch                
                mon=ec2.cloudwatch.connect_to_region(r.name)
                elb=con.get_all_load_balancers()
                if not elb:
                    print "Region Name:",str(r.name)
                    print "There are no elbs in",str(r.name)
                else:
                    print "Region Name:",str(r.name)
                    for e in elb:
                        if not e.instances:
                            data=[str(r.name),str(e.name),'',"IDLE","No active Instances"]
                            csvwriter.writerow(data)
                        else:
                            print "There are instances in",str(e.name)
                            for i in range (len(e.instances)):
                                #Checking the health of the instance                                
                                b=e.get_instance_health()[i]
                                if b.state == "InService":
                                #Listing all the statistics for the metric RequestCount of Load Balancers                
                                    d=mon.get_metric_statistics(600,datetime.datetime.now() - datetime.timedelta(seconds=604800),datetime.datetime.now(),"RequestCount",'AWS/ELB','Sum',dimensions={'LoadBalancerName':str(e.name)})
                                    for j in d:
                                        z=0
                                        z=z+j.values()[1]
                                    if z > 100:
                                        print "The",str(e.name),"is not idle for instance",e.instances[i]
                                    else:
                                        print "The",str(e.name),"is idle for instance",e.instances[i]
                                        data=[str(r.name),str(e.name),e.instances[i],"IDLE","Number of Requests are less than 100 for past 7 days"]
                                        csvwriter.writerow(data)
                                else:
                                    print "The instance are Out of Service",str(e.instances[i])
                                    data=[str(r.name),str(e.name),e.instances[i],"IDLE","Instance are Out of Service"]
                                    csvwriter.writerow(data)