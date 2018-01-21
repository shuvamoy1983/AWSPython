import boto3


def resource_name(a):
     print("Resource name is {}".format(a))
     if a.lower() == 'iam':
        src = boto3.client(a.lower())
        return src
     elif a.lower() == 'ec2':
         print("Ec2 instance started")
         src = boto3.client(a.lower(),region_name='us-east-1')
         return src
     else:
         print('No Resource choosen')
