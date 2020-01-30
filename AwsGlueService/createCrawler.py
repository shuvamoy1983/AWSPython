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

    def startCrawlar(self):
         response = AwsGlueJobCreation.client.start_crawler(
             Name=self.crawlerName
         )

    def addJob(self):
        job = AwsGlueJobCreation.client.create_job(
            Name='forum',
            Role=self.arnForRole,
            Command={
                'Name': 'glueetl',
                'ScriptLocation': 's3://etlscript/etl.py', ## this is your spark code to place in s3
                'PythonVersion': '3'
            },
            GlueVersion='1.0',
            Timeout=2880,
            MaxCapacity=10
        )

    def runJob(self):
        response = AwsGlueJobCreation.client.start_job_run(
            JobName='forum')




if __name__== '__main__' :
    gl=AwsGlueJobCreation('mydb','rawData',
                          'arn:aws:iam::6557009:role/s3glueserviceRole',
                          's3://source-buc/test.csv')
    if gl.getDataBaseName() == 400:
        gl.createDatabase()
    else:
        print("Database " + gl.getDataBaseName().get('Database')['Name']+ " Already present")

    gl.createCrawlar()
    gl.startCrawlar()
    gl.addJob()
    gl.runJob()



