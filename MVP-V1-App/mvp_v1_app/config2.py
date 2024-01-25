from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)

import mvp_v1_app.config as config  

# basic VPC configs
VPC = 'MVP-V1-VPC2'
REGION = 'eu-central-1'

# route tables
PRIVATE_ROUTE_TABLE_1 = 'private-route-table-1'

ROUTE_TABLES_ID_TO_ROUTES_MAP = {
    
    PRIVATE_ROUTE_TABLE_1: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'nat_gateway_id': config.NAT_GATEWAY,
            'router_type': ec2.RouterType.NAT_GATEWAY
        },
    ]
}

# subnets and instances
PRIVATE_SUBNET_1 = 'private-subnet-1'

SUBNET_CONFIGURATION = {
    PRIVATE_SUBNET_1: {
        'availability_zone': 'eu-central-1c',
        'cidr_block': '10.20.20.0/26',
        'map_public_ip_on_launch': False,
        'route_table_id': PRIVATE_ROUTE_TABLE_1,
    }
}

