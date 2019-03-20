from botocore.exceptions import ClientError

from creds import Creds
import boto3


creds = Creds("credentials.csv")

REGION = "us-east-2"
ec2 = boto3.client(
    'ec2',
    aws_access_key_id=creds.access_key_id,
    aws_secret_access_key=creds.secret_key,
    region_name=REGION
)

# Ubuntu Server 18.04 ID from the AWS panel
image_id = "ami-0f65671a86f061fcd"

# Second smallest instance, free tier eligible.
instance_type = "t2.micro"

# Make this a command-line argument in the future.
keypair_name = "robot"

response = {}
try:
    response = ec2.run_instances(ImageId=image_id,
                                 InstanceType=instance_type,
                                 KeyName=keypair_name,
                                 MinCount=1,
                                 MaxCount=1)

    print(response['Instances'][0])

except ClientError as e:
        print(e)

response = ec2.describe_instances()
print(response)
