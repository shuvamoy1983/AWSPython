from boto.ec2.autoscale import AutoScaleConnection
from boto.ec2.autoscale import LaunchConfiguration
from boto.ec2.autoscale import AutoScalingGroup

from Load_Balancer.LoadBalancer_create import ELB


class AutoScaling:
    conn = AutoScaleConnection()

    def __init__(self,name,image_id,groupName,elb_name,min_size,max_size,a_zone=[]):
        self.name = name
        self.image_id = image_id
        self.groupName = groupName
        self.elb_name = elb_name
        self.min_size = min_size
        self.max_size = max_size
        self.a_zone = a_zone


    def Launch_configuration(self):
        lc = LaunchConfiguration(name=self.name,
                                 image_id=self.image_id,
                                 instance_type="t1.micro")
        return lc


    def autoScalingGroup(self):
        ag = AutoScalingGroup(group_name=self.groupName,
                              load_balancers=self.elb_name,
                              availability_zones=self.a_zone,
                              launch_config=AutoScaling.Launch_configuration(self),
                              min_size=self.min_size, max_size=self.max_size,
                              connection=AutoScaling.conn
                              )
        return ag


if __name__ == '__main__':
    zones = ['us-east-1a', 'us-east-1b']
    ports = [(80, 8080, 'http'), (443, 8443, 'tcp')]
    load_balancer_name='myELB'
    v = ELB(load_balancer_name, zones, ports)
    v.create_Load_Balancer()

    Ascl = AutoScaling('my-AS_config','ami-26ebbc5c','my_group',load_balancer_name,1,3,zones)
    confg=Ascl.Launch_configuration()
    AutoScaling.conn.create_launch_configuration(confg)
    asg=Ascl.autoScalingGroup()
    AutoScaling.conn.create_auto_scaling_group(asg)




