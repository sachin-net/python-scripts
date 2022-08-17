from urllib import response
import boto3
import os
import json

aws_asg_name = os.environ.get( 'AWS_ASG_NAME' )
aws_region = os.environ.get( 'AWS_REGION' )
prod_scaling_required = os.environ.get( 'PROD_SCALING_REQUIRED' )

client = boto3.client('autoscaling',region_name=aws_region)

def lambda_handler(event, context):
    response = client.create_or_update_tags(
        Tags=[
            {
                'ResourceId': aws_asg_name,
                'ResourceType': 'auto-scaling-group',
                'Key': 'prod-scaling',
                'Value': prod_scaling_required,
                'PropagateAtLaunch': True
            },
        ]
    )
    print (response)
    verify_tags = client.describe_tags(
    Filters=[
        {
            'Name': 'auto-scaling-group',
            'Values': [
                aws_asg_name,
            ],
        },
    ],
    )
    print (verify_tags )
