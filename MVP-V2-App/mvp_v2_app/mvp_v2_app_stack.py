from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_ec2 as ec2,
)


class MvpV2AppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

# Create the web server VPC
        self.vpc_webserver = ec2.Vpc(self, "WebServerVPC",
            cidr="10.10.10.0/24",
            availability_zones=["eu-central-1a"],
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", cidr_mask=26, subnet_type=ec2.SubnetType.PUBLIC),
                ec2.SubnetConfiguration(name="private", cidr_mask=26, subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
            ],
            enable_dns_support=True,
            enable_dns_hostnames=True,
            nat_gateways=1,
        )


        # Create the management server VPC
        self.vpc_adminserver = ec2.Vpc(self, "AdminServerVPC",
            cidr="10.20.20.0/24",
            availability_zones=["eu-central-1b"],
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", cidr_mask=26, subnet_type=ec2.SubnetType.PUBLIC),
                ec2.SubnetConfiguration(name="private", cidr_mask=26, subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
            ],
            enable_dns_support=True,
            enable_dns_hostnames=True,
            nat_gateways=1,
        )

        # VPC Peering:
        self.Peering_connection = ec2.CfnVPCPeeringConnection(self, "VPCwebToVPCadmin",
            peer_vpc_id=self.vpc_webserver.vpc_id,
            vpc_id=self.vpc_adminserver.vpc_id,
        ) 

        # Get the route tables and subnets for the VPC peering connection from webserver to adminserver
        self.subnet_webserver = self.vpc_webserver.public_subnets[0]
        self.rt_sub_webserv = self.subnet_webserver.route_table

        #Add route from webserver to adminserver 
        self.rt_webserver_peering = ec2.CfnRoute(self, "rt-webserver-peering",
            route_table_id=self.rt_sub_webserv.route_table_id,
            destination_cidr_block="10.20.20.0/26",
            vpc_peering_connection_id=self.Peering_connection.ref
            )
        
        # Get the route tables and subnets for the VPC peering connection from adminserver to webserver
        self.subnet_adminserver = self.vpc_adminserver.public_subnets[0]
        self.rt_sub_adminserver = self.subnet_adminserver.route_table

        #Add route from adminserver to webserver
        self.rt_adminserver_peering = ec2.CfnRoute(self, "rt-adminserver-peering",
            route_table_id=self.rt_sub_adminserver.route_table_id,
            destination_cidr_block="10.10.10.0/24",
            vpc_peering_connection_id=self.Peering_connection.ref
            )

