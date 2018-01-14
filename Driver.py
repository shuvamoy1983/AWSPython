from IAM.Chap1_IAM import *
import json
import datetime
from dateutil.tz import tzutc
import time


if __name__ == '__main__':
    src = IamOperation("Sumit","ItDeveloper")
    src.Create_User()
    src.create_group()
    src.addUserToGrp()
    print("Remove",src.removeUserFromGroup())
    print("Delete group",src.delete_group())
    print("User Deleted",src.deleteUser())

