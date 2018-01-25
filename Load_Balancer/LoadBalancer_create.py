import boto3

from Resource.ResouceSelection import resource_name
from boto.ec2.elb import HealthCheck

class ELB:
    elb = resource_name('elb')
    hc = HealthCheck(
        interval=20,
        healthy_threshold=3,
        unhealthy_threshold=5,
        target='HTTP:8080/health'
    )

    def __init__(self,ld_names,zones=[],ports=[]):
        self.ld_names = ld_names
        self.zones=zones
        self.ports=ports

    def create_Load_Balancer(self):

        lb = ELB.elb.create_load_balancer(self.ld_names, self.zones, self.ports)
        lb.configure_health_check(ELB.hc)
        print(lb.dns_name)

