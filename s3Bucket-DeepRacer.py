import boto3
import logging
import boto3
from botocore.exceptions import ClientError
session = boto3.session.Session(profile_name='DeepRacer')
s3 = session.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
#for bucket in response['Buckets']:
    #print(bucket["Name"])


for bucket in response['Buckets']:
    print(bucket["Name"])
    try:
        response1 = s3.get_bucket_encryption(
            Bucket=bucket["Name"]
        )
        print(response1)
    except:
        response = s3.put_bucket_encryption(
            Bucket=bucket["Name"],
            ServerSideEncryptionConfiguration={
                'Rules': [
                    {
                        'ApplyServerSideEncryptionByDefault': {
                            'SSEAlgorithm': 'AES256'
                        }
                    },
                ]
            }
        )
    