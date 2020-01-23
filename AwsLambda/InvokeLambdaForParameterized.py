import boto3, json, typing

def invokeLambdaFunction(*, functionName:str=None, payload:typing.Mapping[str, str]=None):
    if  functionName == None:
        raise Exception('ERROR: functionName parameter cannot be NULL')
    payloadStr = json.dumps(payload)
    payloadBytesArr = bytes(payloadStr, encoding='utf8')
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName=functionName,
        InvocationType="RequestResponse",
        Payload=payloadBytesArr
    )
    return response

if __name__ == '__main__':
    payloadObj = {"Kg" : "300"}
    response = invokeLambdaFunction(functionName='ParaMeterToLambda',  payload=payloadObj)
    print(f'response:{response}')