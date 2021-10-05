import json
import boto3
import pprint
import re

# https://www.sentiatechblog.com/using-the-ec2-price-list-api

pricing_client = boto3.client('pricing', region_name='us-east-1')

def get_products(region):
    paginator = pricing_client.get_paginator('get_products')

    response_iterator = paginator.paginate(
        ServiceCode="AmazonRDS",
        Filters=[
            {
                'Type': 'TERM_MATCH',
                'Field': 'location',
                'Value': region
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'memory',
                'Value': '32 GiB'
            }
        ],
        PaginationConfig={
            'PageSize': 100
        }
    )

    products = []
    for response in response_iterator:
        for priceItem in response["PriceList"]:
            priceItemJson = json.loads(priceItem)
            products.append(priceItemJson)
            print("++++++")
            print(priceItemJson['product']['attributes']['instanceType'])
            
            items = priceItemJson['terms']['OnDemand']
            #print(priceItemJson['terms']['OnDemand'])
            for item in items:
                y = items[item]['priceDimensions']
                #print(y)
                for x in y:
                    print(y[x])
                #print(items[item])

            
            print("------")
            print("")
    #print(products)

if __name__ == '__main__':
    get_products('US East (Ohio)')
    
"""
US East (Ohio)	us-east-2
US East (N. Virginia)	us-east-1
US West (N. California)	us-west-1
US West (Oregon)	us-west-2
Africa (Cape Town)	af-south-1
Asia Pacific (Hong Kong)	ap-east-1
Asia Pacific (Mumbai)	ap-south-1
Asia Pacific (Osaka)	ap-northeast-3
Asia Pacific (Seoul)	ap-northeast-2
Asia Pacific (Singapore)	ap-southeast-1
Asia Pacific (Sydney)	ap-southeast-2
Asia Pacific (Tokyo)	ap-northeast-1
Canada (Central)	ca-central-1
China (Beijing)	cn-north-1
China (Ningxia)	cn-northwest-1
Europe (Frankfurt)	eu-central-1
Europe (Ireland)	eu-west-1
Europe (London)	eu-west-2
Europe (Milan)	eu-south-1
Europe (Paris)	eu-west-3
Europe (Stockholm)	eu-north-1
Middle East (Bahrain)	me-south-1
South America (São Paulo)	sa-east-1
"""