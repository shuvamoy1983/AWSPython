import boto3
client = boto3.client('lambda')
response1 = client.add_permission(FunctionName='arn:aws:lambda:us-west-2:655700933854:function:mylambda',
                               StatementId='response2-id-2',
                               Action='lambda:InvokeFunction',
                               Principal='s3.amazonaws.com',
                               SourceArn='arn:aws:s3:::source-buc'
                              )

response2 = client.get_policy(FunctionName='arn:aws:lambda:us-west-2:655700933854:function:mylambda')

s3 = boto3.client('s3')
response3 = s3.put_bucket_notification_configuration(
                            Bucket='source-buc',
                            NotificationConfiguration= {'LambdaFunctionConfigurations':[{'LambdaFunctionArn': 'arn:aws:lambda:us-west-2:655700933854:function:mylambda', 'Events': ['s3:ObjectCreated:*']}]})