#!/usr/local/bin/python3
import boto3

ec2 = boto3.client('ec2')
regions = ec2.describe_regions().get('Regions',[])
#for region in regions:
#    region['RegionName']
ec2 = boto3.client('ec2',region_name='us-east-1')
volumes = ec2.describe_volumes()
for volume in volumes['Volumes']:
    print(volume['VolumeId'])
