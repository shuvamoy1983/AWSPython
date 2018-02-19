import json
import boto3
import json
import urllib

from Resource.ResouceSelection import *

class CloudFormation:
    cl = resource_name("CloudFormation")


    def __init__(self,file_name):
        self.file_name=file_name

    def cf_validation(self):
        response = CloudFormation.cl.validate_template(
            TemplateBody=self.file_name)



    def cf_create_stack(self,file):
        CloudFormation.cl.create_stack(
            StackName='mystack4',
            TemplateBody=file,
            Parameters=[{
                'ParameterKey': 'InstanceType',
                'ParameterValue': 't2.micro'
            }])

    def file_local_read(self):
        with open(self.file_name, 'r') as f:
            data1 = CloudFormation.parse(f.read())
            data2 = json.dumps(data1)
            return data2

    def parse(text):
        try:
            return json.loads(text)
        except ValueError as e:
            print('invalid json: %s' % e)
            return None  # or: raise


if __name__ == '__main__':
    obj=CloudFormation("single_instance1.json")
    obj.cf_create_stack(obj.file_local_read())


