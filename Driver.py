from IAM.Chap1_IAM import *
import json
import datetime
from dateutil.tz import tzutc
import time


if __name__ == '__main__':
    # Create a policy
    my_managed_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "logs:CreateLogGroup",
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "dynamodb:DeleteItem",
                    "dynamodb:GetItem",
                    "dynamodb:PutItem",
                    "dynamodb:Scan",
                    "dynamodb:UpdateItem"
                ],
                "Resource": "*"
            }
        ]
    }
    src = IamOperation("Sumit","ItDeveloper","Bob","myDynamoDb",my_managed_policy)
    src.Create_User()
    src.create_group()
    src.addUserToGrp()
    print("Remove",src.removeUserFromGroup())
    print("Delete group",src.delete_group())
    print("User Deleted",src.deleteUser())
    src.create_policy()

