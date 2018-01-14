from IAM.Chap_IAM import *
import json
import datetime
from dateutil.tz import tzutc

if __name__ == '__main__':
    print("Creating group" ,create_group("ItDeveloper"))
    response = Create_User("Sumit")
    print("List of Users:" ,listOfUsers())
    print("User update",updateUser("Sumit","Sumit1"))
    print("Added user to group" ,addUserToGrp("ItDeveloper","Sumit1"))
    #k, l = deleteUser("Sumit1")
    #print("User delete", k, l)
