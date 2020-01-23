import json, boto3
client = boto3.client('lambda')
response = client.create_function(
    FunctionName='LambdaToGlueExecution',
    Runtime='python3.6',
    Role='arn:aws:iam::655700933854:role/LambdaFullAccess',
    Handler='LambdaToGlueExecution.lambda_handler',
    Code= {'ZipFile': open(r'C:\Users\shumondal\PycharmProjects\Lambda\mylambda.zip', 'rb').read() })