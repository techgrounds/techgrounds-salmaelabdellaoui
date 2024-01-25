from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
    aws_ssm as ssm
)
# basic VPC configs
VPC = 'MVP-V1-VPC1'

INTERNET_GATEWAY = 'internet-gateway'
NAT_GATEWAY = 'nat-gateway' 
REGION = 'eu-central-1'

# route tables
PUBLIC_ROUTE_TABLE = 'public-route-table'
PRIVATE_ROUTE_TABLE = 'private-route-table'

ROUTE_TABLES_ID_TO_ROUTES_MAP = {
    PUBLIC_ROUTE_TABLE: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'gateway_id': INTERNET_GATEWAY,
            'router_type': ec2.RouterType.GATEWAY
        }
    ],
    PRIVATE_ROUTE_TABLE: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'nat_gateway_id': NAT_GATEWAY,
            'router_type': ec2.RouterType.NAT_GATEWAY
        },
    # {
    #         'destination_cidr_block': '10.20.20.0/24',
    #         'vpc_peering_connection_id': 'VPC1toVPC2',
    #         'router_type': ec2.RouterType.VPC_PEERING_CONNECTION
    #     }
    ],
}

# subnets and instances
PUBLIC_SUBNET_1 = 'public-subnet-1'
PUBLIC_SUBNET_2 = 'public-subnet-2' 

SUBNET_CONFIGURATION = {
    PUBLIC_SUBNET_1: {
        'availability_zone': 'eu-central-1a',
        'cidr_block': '10.10.10.0/25',
        'map_public_ip_on_launch': True,
        'route_table_id': PUBLIC_ROUTE_TABLE,
    },
    PUBLIC_SUBNET_2: {
        'availability_zone': 'eu-central-1b',
        'cidr_block': '10.10.10.128/25',
        'map_public_ip_on_launch': True,
        'route_table_id': PUBLIC_ROUTE_TABLE,
    } 
}

