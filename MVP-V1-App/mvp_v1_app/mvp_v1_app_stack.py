from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    NestedStack,
)

import mvp_v1_app.config as config 
import mvp_v1_app.config2 as config2 


class MvpV1AppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

# The code that defines the stack goes here
 # create VPC
        self.Salma_vpc = ec2.Vpc(
            self, config.VPC, ip_addresses=ec2.IpAddresses.cidr('10.10.10.0/24'), max_azs=3,
            nat_gateways=0, subnet_configuration=[],
            enable_dns_support=True,
            enable_dns_hostnames=True,
        )

        self.private_salma_vpc = ec2.Vpc(
            self, config2.VPC, ip_addresses=ec2.IpAddresses.cidr('10.20.20.0/24'), max_azs=3,
            nat_gateways=0, subnet_configuration=[],
            enable_dns_support=True,
            enable_dns_hostnames=True,
        )


# Create a network peering stack which creates peering between the production and management VPCs
        self.peering_stack = NetworkPeeringStack(
            self,
            "NetworkPeeringStack",
            vpc_one=self.Salma_vpc,
            vpc_two=self.private_salma_vpc,
        ) 
       
        self.elastic_ip = ec2.CfnEIP(self, "EIP") 
        self.internet_gateway = self.attach_internet_gateway()

        self.subnet_id_to_subnet_map = {}
        self.route_table_id_to_route_table_map = {} 

        self.create_route_tables() 

        self.create_subnets() 
        self.create_subnet_route_table_associations()
        self.nat_gateway = self.attach_nat_gateway()
        self.nat_gateway.add_depends_on(self.elastic_ip) 
        self.create_routes() 

#Add the code to create routes through the VPC peering connection
# Get the subnets for Frankfurt Availability Zone 1c
        private_subnet = self.subnet_id_to_subnet_map[config2.PRIVATE_SUBNET_1].ref
        Private_route_table = self.route_table_id_to_route_table_map[config2.PRIVATE_ROUTE_TABLE_1].ref

        ec2.CfnRoute(
        self, 'RouteToOtherVPC',
        route_table_id=Private_route_table,
        destination_cidr_block='10.10.10.0/24',  # Het CIDR-blok van de andere VPC
        vpc_peering_connection_id=self.peering_stack.peerconnection.ref,
        )

    def create_route_tables(self):
        """ Create Route Tables """
        for route_table_id in config.ROUTE_TABLES_ID_TO_ROUTES_MAP:
            self.route_table_id_to_route_table_map[route_table_id] = ec2.CfnRouteTable(
                self, route_table_id, vpc_id=self.Salma_vpc.vpc_id,
                tags=[{'key': 'Name', 'value': route_table_id}]
            )
        for route_table_id in config2.ROUTE_TABLES_ID_TO_ROUTES_MAP:
            self.route_table_id_to_route_table_map[route_table_id] = ec2.CfnRouteTable(
                self, route_table_id, vpc_id=self.private_salma_vpc.vpc_id,
                tags=[{'key': 'Name', 'value': route_table_id}]
            )

    def create_routes(self):
        """ Create routes of the Route Tables """
        for route_table_id, routes in config.ROUTE_TABLES_ID_TO_ROUTES_MAP.items():
            for i in range(len(routes)):
                route = routes[i]
            kwargs = {
                **route,
                'route_table_id': self.route_table_id_to_route_table_map[route_table_id].ref,
            }
            if route['router_type'] == ec2.RouterType.GATEWAY:
                kwargs['gateway_id'] = self.internet_gateway.ref
            if route['router_type'] == ec2.RouterType.NAT_GATEWAY:
                kwargs['nat_gateway_id'] = self.nat_gateway.ref 
            del kwargs['router_type']
            ec2.CfnRoute(self, f'{route_table_id}-route-{i}', **kwargs)

        
    def create_subnets(self):
        """ Create subnets of the VPC """
        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION.items():
            subnet = ec2.CfnSubnet(
                self, subnet_id, vpc_id=self.Salma_vpc.vpc_id,
                cidr_block=subnet_config['cidr_block'],
                availability_zone=subnet_config['availability_zone'],
                tags=[{'key': 'Name', 'value': subnet_id}],
                map_public_ip_on_launch=subnet_config['map_public_ip_on_launch'],
            )
            self.subnet_id_to_subnet_map[subnet_id] = subnet 

        for subnet_id, subnet_config in config2.SUBNET_CONFIGURATION.items():
            subnet = ec2.CfnSubnet(
            self, subnet_id, vpc_id=self.private_salma_vpc.vpc_id,
            cidr_block=subnet_config['cidr_block'],
            availability_zone=subnet_config['availability_zone'],
            tags=[{'key': 'Name', 'value': subnet_id}],
            map_public_ip_on_launch=subnet_config['map_public_ip_on_launch'],
        )
        self.subnet_id_to_subnet_map[subnet_id] = subnet


    def create_subnet_route_table_associations(self):
        """ Associate subnets with route tables """
        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION.items():
            route_table_id = subnet_config['route_table_id']
            ec2.CfnSubnetRouteTableAssociation(
            self, f'{subnet_id}-{route_table_id}',
            subnet_id=self.subnet_id_to_subnet_map[subnet_id].ref,
            route_table_id=self.route_table_id_to_route_table_map[route_table_id].ref
        )
        for subnet_id, subnet_config in config2.SUBNET_CONFIGURATION.items():
            route_table_id = subnet_config['route_table_id']
            ec2.CfnSubnetRouteTableAssociation(
            self, f'{subnet_id}-{route_table_id}',
            subnet_id=self.subnet_id_to_subnet_map[subnet_id].ref,
            route_table_id=self.route_table_id_to_route_table_map[route_table_id].ref
        )

    def attach_internet_gateway(self) -> ec2.CfnInternetGateway:
        """ Create and attach internet gateway to the VPC """
        internet_gateway = ec2.CfnInternetGateway(self, config.INTERNET_GATEWAY)
        ec2.CfnVPCGatewayAttachment(self, 'internet-gateway-attachment',
        vpc_id=self.Salma_vpc.vpc_id,
        internet_gateway_id=internet_gateway.ref)
        return internet_gateway
    
    def attach_nat_gateway(self) -> ec2.CfnNatGateway:
        """ Create and attach nat gateway to the VPC """
        nat_gateway = ec2.CfnNatGateway(self, config.NAT_GATEWAY,
                                        allocation_id=self.elastic_ip.attr_allocation_id,
                                        subnet_id=self.subnet_id_to_subnet_map[config.PUBLIC_SUBNET_1].ref, )
        return nat_gateway
    
    
class NetworkPeeringStack(NestedStack):
        def __init__(
            self,
            scope: Construct,
            construct_id: str,
            vpc_one: ec2.Vpc,
            vpc_two: ec2.Vpc,
            **kwargs
        ) -> None:
            super().__init__(scope, construct_id, **kwargs)  

# Peering connection
            self.peerconnection = ec2.CfnVPCPeeringConnection(
            self,
            "VPC1toVPC2",
            vpc_id=vpc_one.vpc_id,
            peer_vpc_id=vpc_two.vpc_id,
        )
            
         

# Create routes in the peered VPCs for traffic flow 
            
        #     ec2.CfnRoute(
        #     self,
        #     "RouteFromVPC1toVPC2",
        #     destination_cidr_block=vpc_two.vpc_cidr_block,
        #     route_table_id=vpc_two.private_subnets[0].route_table.route_table_id,
        #     vpc_peering_connection_id=self.peerconnection.ref,
        # )

        #     ec2.CfnRoute(
        #     self,
        #     "RouteFromVPC2toVPC1",
        #     destination_cidr_block=vpc_one.vpc_cidr_block,
        #     route_table_id=vpc_one.public_subnets[0].route_table.route_table_id,
        #     vpc_peering_connection_id=self.peerconnection.ref,
        # )  
            