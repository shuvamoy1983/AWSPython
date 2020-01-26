import boto3
import logging
from botocore.exceptions import ClientError

class AwsGlueJobCreation(object):
    client = boto3.client('glue', region_name='us-west-2')

    LOG = logging.getLogger(__name__)

    def __init__(self,databaseName,crawlerName,arnForRole,srcPath):
        self.databaseName = databaseName
        self.crawlerName = crawlerName
        self.arnForRole=arnForRole
        self.srcPath=srcPath

    def getDataBaseName(self):
        try:
            response = AwsGlueJobCreation.client.get_database(
            Name=self.databaseName
        )
            return response
        except ClientError as e:
            return e.response.get('ResponseMetadata')['HTTPStatusCode']

    def deleteDatabase(self):
        response = AwsGlueJobCreation.client.delete_database(
            Name=self.databaseName)

    def createDatabase(self):
        response = AwsGlueJobCreation.client.create_database(
            DatabaseInput={
            'Name': self.databaseName,  # Required
            'Description': 'Database created with boto3',
                  },
        )

    def createCrawlar(self):
        response = AwsGlueJobCreation.client.create_crawler(
            Name=self.crawlerName,
            Role=self.arnForRole,
            DatabaseName=self.databaseName,
            Targets={
                'S3Targets': [
                    {
                        'Path': self.srcPath
                    }
                ]
            }
        )


if __name__== '__main__' :
    gl=AwsGlueJobCreation('mydb','rawData',
                          'arn:aws:iam::655700:role/s3glueserviceRole',
                          'arn:aws:s3:::source-buc/test.csv')
    if gl.getDataBaseName() == 400:
        gl.createDatabase()
    else:
        print("Database " + gl.getDataBaseName().get('Database')['Name']+ " Already present")

    gl.createCrawlar()



