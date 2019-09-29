#!/usr/local/bin/python3
import boto3

ec2 = boto3.resource('ec2',region_name='us-west-2')

Vols = ['vol-0007075b37b9a6148','vol-046379c4f489ccf48']

for Vol in Vols:
    print("=================================================================")
    print(Vol)
    gvol = ec2.Volume(Vol)
    print(gvol.attachments)
    print(gvol.describe_status())
    print(gvol.state)
    gvol.delete()


