import boto3
import boto.ec2.elb


def resource_name(a):
     print("Resource name is {}".format(a))
     if a.lower() == 'iam':
        print("IAM resource choosen")
        src = boto3.client(a.lower())
        return src
     elif a.lower() == 'ec2':
         print("Ec2 resource choosen")
         src = boto3.client(a.lower(),region_name='us-east-1')
         return src

     elif a.lower() == 'elb':
         print("Elb resource choosen")
         src = boto.ec2.elb.connect_to_region('us-east-1')
         return src

     elif a.lower() == 'cloudformation':
         print("cloudformation resource selected")
         config = None
         src=boto3.client(a.lower())
         return src

     else:
         print('No Resource choosen')
