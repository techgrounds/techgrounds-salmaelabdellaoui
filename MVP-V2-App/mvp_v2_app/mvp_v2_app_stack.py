from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_ec2 as ec2,
    CfnTag,
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

        # Create Network ACL for the webserver and adminserver:
        self.nacl_web = ec2.NetworkAcl(self, 'nacl-web', 
            network_acl_name='nacl-web',
            vpc=self.vpc_webserver,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
            )
        
        self.nacl_admin = ec2.NetworkAcl(self, 'nacl-admin', 
            network_acl_name='nacl-admin',
            vpc=self.vpc_adminserver,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
            )

        # Inbound and outbound rule in vpc_web for HTTP traffic
        self.nacl_web.add_entry("Inbound-HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),        
            direction=ec2.TrafficDirection.INGRESS
            )
        self.nacl_web.add_entry("Outbound-HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),        
            direction=ec2.TrafficDirection.EGRESS
            )
        
        # Inbound rule in vpc_web for SSH from admin server 
        admin_cidr = "10.20.20.0/26"

        self.nacl_web.add_entry("Inbound SSH from Admin",
            cidr=ec2.AclCidr.ipv4(admin_cidr),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),  
            rule_action=ec2.Action.ALLOW,      
            direction=ec2.TrafficDirection.INGRESS,
            )

        # Inbound rule in vpc_web for RDP from admin server
        self.nacl_web.add_entry("Inbound RDP from Admin",
            cidr=ec2.AclCidr.ipv4(admin_cidr),
            rule_number=201,
            traffic=ec2.AclTraffic.tcp_port(3389),  
            rule_action=ec2.Action.ALLOW,      
            direction=ec2.TrafficDirection.INGRESS,
            )

        # Inbound rule in vpc_web for ephemeral ports 
        self.nacl_web.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=600,
            traffic=ec2.AclTraffic.tcp_port_range(32768, 65535),    
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Outbound rule all trafic in vpc_webserver
        self.nacl_web.add_entry("Outbound-All",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=700,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS
            )
        
        
        # Inbound rule in vpc_admin for RDP from the admin IP
        admin_ip = "192.168.178.12/32" 

        self.nacl_admin.add_entry("Inbound RDP from Admin-ip",
            cidr=ec2.AclCidr.ipv4(admin_ip),
            rule_number=250,
            traffic=ec2.AclTraffic.tcp_port(3389),  
            rule_action=ec2.Action.ALLOW,      
            direction=ec2.TrafficDirection.INGRESS,
            )
        
        # Inbound rule in vpc_admin for ephemeral ports 
        self.nacl_admin.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=555,
            traffic=ec2.AclTraffic.tcp_port_range(40000, 65535),    # Windows ephemeral ports
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Outbound rule all traffic in vpc_admin
        self.nacl_admin.add_entry("Outbound-All",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=500,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS
            )
        
    
        
        # Defining user data, security group, and key pair for the EC2 instance (webserver)
        # define user data 
        user_data_webserver = ec2.UserData.for_linux( shebang =  "#!/bin/bash")
        user_data_webserver.add_commands ( "yum -y install httpd",
                                "systemctl enable httpd",
                                 "systemctl start httpd",
                                """echo '<html><h1>L.S., Welcome on my page, I am looking forward to help you with your problems</h1>
                                 <b1> I hope you enjoyed our website <b1>                                         
                                </html>' > /var/www/html/index.html"""

        )

        # Create key-pair for SSH connection to the webserver
        keypair_webserver = ec2.KeyPair(self, "keypair_webserver",
        key_pair_name="keypair_webserver",
        )

        # Create Security Group for Webserver
        admin_cidr_sg = ec2.Peer.ipv4("10.20.20.0/26")

        sg_webserver = ec2.SecurityGroup(self,"sg_WebServer", 
        vpc = self.vpc_webserver,
        description = "sg_webserver",
        allow_all_outbound = True,
        disable_inline_rules = False,                                                                   
        )

        sg_webserver.add_ingress_rule(admin_cidr_sg, ec2.Port.tcp(22), "Allow SSH from Admin") 
        sg_webserver.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "Allow HTTP")
        sg_webserver.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(443), "Allow HTTPS")
       
        # Create Webserver instance
        self.instance_webserver = ec2.Instance(self, "instance-webserver",
            instance_name="instance-webserver",
            vpc=self.vpc_webserver,                               
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC),                                   
            key_pair=keypair_webserver,                    
            security_group=sg_webserver,                   
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),  
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023), 
            user_data=user_data_webserver,   
            block_devices=[ec2.BlockDevice(
                device_name="/dev/sdh",                        
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=15,                              
                    encrypted=True,                             
                    )
                )], 
            )

