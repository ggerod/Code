#!/usr/local/bin/python3
import boto3

ec2 = boto3.client('ec2')

#response = ec2.describe_regions()
#print('Regions:', len(response['Regions']))
#for region in response['Regions']:
#    print(region['RegionName'])
#print()

# Retrieves availability zones only for region of the ec2 object
#response = ec2.describe_availability_zones()
#print('Availability Zones:', len(response['AvailabilityZones']))
#for zone in response['AvailabilityZones']:
#    print(zone['RegionName'])

#resp = ec2.describe_instances(
#    Filters=[
#        {
#            'Name': 'availability-zone',
#            'Values': ['us-west-2a',]
#        }
#    ]
#)

#for item in resp['Reservations']:
#    i += 1
#    print()
#    print(i)
#    for element in (item['Instances'][0])['Tags']:
#        if ((element['Key'] == "Name") or (element['Key'] == 'Platform')):
#            print(element['Value'])

#for item in resp['Reservations']:
#    print()
#    print(item)

#for item in resp['Reservations']:
#    print()
#    (item['Instances'][0])['VpcId']

#for item in resp['Reservations']:
#    if ((item['Instances'][0])['VpcId'] != 'vpc-01fa718af3b9a0921'):
#        (item['Instances'][0])['VpcId']

def HasKey(lst,ky):
    foundkey=0
    for element in lst:
        if (element['Key'] == ky): return(True)
    return(False)


resp = ec2.describe_instances()
i = 0
for item in resp['Reservations']:
   if (((item['Instances'][0])['VpcId'] == 'vpc-51ac3636') or ((item['Instances'][0])['VpcId'] == 'vpc-6e8c7316')):
           i+=1
           print("=============")
           print(i,(item['Instances'][0])['VpcId'])
           print(item['Instances'][0]['InstanceId'])
           print()

           for element in (item['Instances'][0])['Tags']:
               print(element['Key']," - ", element['Value'])
