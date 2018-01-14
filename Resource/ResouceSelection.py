import boto3
import os

def resource_name(a):
    print("Resource name is {}".format(a))
    if a.lower()=='iam':
        src = iam_resource(a.lower())
        return src

def iam_resource(rs):
    iam = boto3.client(rs)
    return iam