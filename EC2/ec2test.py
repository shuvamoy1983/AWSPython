from Resource.ResouceSelection import resource_name

class StartInstances:
    ec2_conn = resource_name('ec2')

    def __init__(self,keypair):
        self.keypair=keypair


    def create_ec2(self):
        amiNameArr = ["ami-26ebbc5c"]
        amiDescArr = ["Amazon Linux","Red Hat Enterprise","SUSE Enterprise",
              "Ubuntu Server 13.10","Microsoft Server 2012"]
        amiInstTypesArr = ["t1.micro"]
        print("Creating key pair...")
        awsKeyPair =StartInstances.ec2_conn.create_key_pair(KeyName=self.keypair)
        print(awsKeyPair)
        path = "/Users/shuvamoymondal/"+self.keypair
        f = open(path, "w")
        f.write(str(awsKeyPair))
        print("Saved key pair: " + self.keypair)
        f.close()

        print("Spawning instances...")

        for amiIndx in range(1):  # len(amiNameArr)):
         print("   AMI description: " + str(amiDescArr[amiIndx]))
         for typeIndx in range(1):  # len(amiInstTypesArr)):
           print("      starting machine: " + str(amiInstTypesArr[typeIndx]))
           StartInstances.ec2_conn.run_instances(
            ImageId=amiNameArr[amiIndx],
            InstanceType=amiInstTypesArr[typeIndx],
           # SecurityGroups='default',
            KeyName=self.keypair,
            MinCount=1,
            MaxCount=1
        )


if __name__ == "__main__":
    v = StartInstances("mykeypair.pem")
    v.create_ec2()