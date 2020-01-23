import json, boto3
client = boto3.client('lambda')
response = client.create_function(
    FunctionName='ParaMeterToLambda',
    Runtime='python3.6',
    Role='arn:aws:iam::65570093:role/LambdaFullAccess',
    Handler='ParaMeterToLambda.sree_handler',
    Code= {'ZipFile': open(r'C:\Users\shumondal\PycharmProjects\Lambda\ParaMeterToLambda.zip', 'rb').read() })
