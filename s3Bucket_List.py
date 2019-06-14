# Retrieve the list of existing buckets
import boto3
import logging
import boto3
from botocore.exceptions import ClientError
session = boto3.session.Session(profile_name='DeepRacer')
s3 = session.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(bucket["Name"])


ec2 = session.client('ec2', region_name='eu-west-1')
response = ec2.describe_instances(

)
#print(response)
for i in response['Reservations']:
    for instance in i['Instances']:
        print(instance['InstanceType'])