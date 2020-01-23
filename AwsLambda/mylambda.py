import boto3
s3 = boto3.resource('s3')
def lambda_handler(event, context):
    copy_source = {
        'Bucket': 'source-buc',
        'Key': 'test.csv'
    }
    s3.meta.client.copy(copy_source, 'target-buc','test.csv')