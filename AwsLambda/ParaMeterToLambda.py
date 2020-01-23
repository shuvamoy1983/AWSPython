import json

print("Starting..\n")
def sree_handler(event, context):
    kg =event['Kg']
    lb =float(kg)*2.20462
    ans = str(kg) + " Kgs is " + str(round(lb, 2)) + " lbs\n"
    print(ans)
    return ans