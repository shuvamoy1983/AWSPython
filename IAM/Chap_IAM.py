from Resource.ResouceSelection import *
import sys
iam = resource_name("IAM")

# Create user
def Create_User(a):
    try:
        response = iam.create_user(UserName=a)
        return response
    except ValueError:
        print(ValueError)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

##List Users in Your Account
def listOfUsers():
    lstUsr= iam.list_users()
    for k in lstUsr['Users']:
        return k['UserName']

def deleteUser(a):
    dltUsr= iam.delete_user(UserName=a)
    for i,j in dltUsr.items():
        return i,j['RequestId']

def updateUser(a,b):
    updUsr= iam.update_user(UserName=a, NewUserName=b)
    return updUsr

def create_group(rs):
    cmd='aws iam create-group --group-name {}'.format(rs)
    os.system(cmd)

def addUserToGrp(a,b):
    response = iam.add_user_to_group(
    GroupName=a,
    UserName=b)
    return response