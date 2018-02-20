import boto3
import json
import os
import sys
import time


###python test.py 'stack1' "/Users/shuvamoymondal/single_instance.json" "/Users/shuvamoymondal/PycharmProjects/cloudformation-template/paramfile.json"
### input template: https://s3-us-west-2.amazonaws.com/cloudformation-templates-us-west-2/EC2InstanceWithSecurityGroupSample.template
cf = boto3.client('cloudformation')


def parse(text):
    try:
        return json.loads(text)
    except ValueError as e:
        print('invalid json: %s' % e)
        return None # or: raise

def create_stack(stackName, templateFile, paramFilename):
    # Setup parameters
    #params.append({"ParameterKey": "EnvironmentType", "ParameterValue": "t1.micro"})
    params = []
    with open(paramFilename, 'r') as f:
        data1=parse(f.read())

        for param_entry in data1:
            params.append(param_entry)

        print(params)



    with open(templateFile, 'r') as file:
        template = file.read()

        cf.create_stack(StackName=stackName,
                    TemplateBody=template,
                    Parameters=params
                    )

def main(argv):
    stackName = sys.argv[1]
    templateFile = sys.argv[2]
    paramFilename = sys.argv[3]


    create_stack(stackName, templateFile, paramFilename)
    print("Started stack creation for %s" % (stackName))


if __name__ == "__main__":
    print(sys.argv[1:])
    main(sys.argv[1:])