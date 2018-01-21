from Resource.ResouceSelection import resource_name


class EC2:
    ec2_conn = resource_name('ec2')


    def __init__(self,ami_id,key_nm,instance_type):
        self.ami_id =ami_id
        self.key_nm= key_nm
        self.instance_type= instance_type
        #self.security_id = security_id

    def create_instance_ec2(self):
       EC2.ec2_conn.run_instances(ImageId= self.ami_id,
                                     KeyName =self.key_nm,
                                     InstanceType= self.instance_type,

                                     MinCount=1,
                                     MaxCount=1)


if __name__ == "__main__":
    p = EC2('ami-0b1e356e','myec2','t2.micro')
    print(p.create_instance_ec2())