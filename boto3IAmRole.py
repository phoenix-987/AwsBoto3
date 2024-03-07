import boto3
import json

DDB_POLICY = {
    'name': 'MyDynamoDBPolicty',
    'policy' : {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "dynamodb:GetItem",
                    "dynamodb:Scan"
                ],
                "Resource": "*"
            }
        ]
    }
}

# ------------------------------------------------------------------------------------------

S3_POLICY = {
    'name': 'MyCustomS3Policy',
    'policy': {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:ListBucket",
                    "s3:GetObject",
                    "s3:PutObject",
                ],
                "Resource": "*"
            }
    ]}
}

# ------------------------------------------------------------------------------------------

def add_new_user(client, user):
    response = client.create_user(UserName=user)                 

    if response['ResponseMetadata'].get('HTTPStatusCode') == 200:
        print(f'\nUser {user} created successfully!')
    
    else:
        print('\nSomething went wrong :(')

# ------------------------------------------------------------------------------------------

def delete_iam_user(client, user):
    response = client.delete_user(UserName=user)
    if response['ResponseMetadata'].get('HTTPStatusCode') == 200:
        print(f'\nUser {user} deleted successfully!')
    
    else:
        print('\nSomething went wrong :(')

# ------------------------------------------------------------------------------------------

def add_user_to_grp(client, user):
    response = client.add_user_to_group(
        GroupName='Admin',
        UserName=user #'DummyAdminUser'
    )
    if response['ResponseMetadata'].get("HTTPStatusCode") == 200:
        print(f'\nUser {user} added to group Admin successfully')
        
    else:
        print('\nSomething went wrong :(')

# ------------------------------------------------------------------------------------------

def remove_iam_user_from_grp(client, user):
    response = client.remove_user_from_group(
        GroupName='Admin',
        UserName=user
    )

    if response['ResponseMetadata'].get('HTTPStatusCode') == 200:
        print(f'\nUser {user} removed from group Admin successfully!')

    else:
        print(f'\nSomething went wrong :(')

# ------------------------------------------------------------------------------------------

def create_new_policy(client, policy):
    response = client.create_policy(
        PolicyName=policy.get('name'),
        PolicyDocument=json.dumps(policy.get('policy'))
    )

    if response['ResponseMetadata'].get('HTTPStatusCode') == 200:
        print(f'\nPolicy {policy["name"]} created successfully!')

    else:
        print(f'\nSomething went wrong :(')

# ------------------------------------------------------------------------------------------

client = boto3.client('iam')
username = 'DemoUser'

add_new_user(client=client, user=username)
add_user_to_grp(client=client, user=username)
remove_iam_user_from_grp(client=client, user=username)
delete_iam_user(client=client, user=username)
create_new_policy(client=client, policy=S3_POLICY)
