from Resource.ResouceSelection import *
import os
import sys
import json

class IamOperation:
    ##static variable
    iam = resource_name("IAM")

    ## initialize class variable
    def __init__(self,User,Group,NewUser,PolicyName,Policy):
        self.user=User
        self.grp=Group
        self.Nuser=NewUser
        self.PolicyNM=PolicyName
        self.Policy_dtls = Policy

##How to create user in aws IAM
    def Create_User(self):
        try:
         response = IamOperation.iam.create_user(UserName=self.user)
         return response
        except ValueError:
         print(ValueError)
        except:
         print("Unexpected error:", sys.exc_info()[0])
         raise

    ##How to get list of user in aws IAM

    def listOfUsers(self):
        lstUsr= IamOperation.iam.list_users()
        for k in lstUsr['Users']:
         return k['UserName']

    ##How to delete user in aws IAM

    def deleteUser(self):
     dltUsr= IamOperation.iam.delete_user(UserName=self.user)
     for i,j in dltUsr.items():
         return i,j['RequestId']

    ##How to update user in aws IAM
    def updateUser(self):
         updUsr= IamOperation.iam.update_user(UserName=self.user, NewUserName=self.Nuser)
         return updUsr

    ##How to create group in aws IAM
    def create_group(self):
         cmd='aws iam create-group --group-name {}'.format(self.grp)
         os.system(cmd)

    ##How to add user to group in aws IAM
    def addUserToGrp(self):
         response = IamOperation.iam.add_user_to_group(GroupName=self.grp,UserName=self.user)
         return response

    ##How to create access key for user in aws IAM
    def createAccessKey(self):
        response = IamOperation.iam.create_access_key(UserName=self.user)
        return response

    ##How to remove user from group in aws IAM
    def removeUserFromGroup(self):
         response =IamOperation.iam.remove_user_from_group(UserName=self.user, GroupName=self.grp)
         return response

    ##How to delete group in aws IAM
    def delete_group(self):
        response = IamOperation.iam.delete_group(GroupName=self.grp)
        print(type(response))
        return response

    def create_policy(self):
        response = IamOperation\
            .iam.create_policy(PolicyName=self.PolicyNM,
                               PolicyDocument=json.dumps(self.Policy_dtls))

        print(response)
        return response

