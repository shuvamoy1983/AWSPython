import json, boto3
client = boto3.client('lambda')
response = client.create_function(
    FunctionName='mylambda',
    Runtime='python3.6',
    Role='arn:aws:iam::655:role/LambdaFullAccess',
    Handler='mylambda.lambda_handler',
    Code= {'ZipFile': open(r'C:\Users\shumondal\PycharmProjects\Lambda\mylambda.zip', 'rb').read() })
