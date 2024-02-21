from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_iam as iam,
    aws_backup as backup, 
    aws_events as events,
    aws_autoscaling as autoscaling,
    aws_elasticloadbalancingv2 as elbv2,
    aws_certificatemanager as cm,
    aws_cloudwatch as cloudwatch, 
    RemovalPolicy,
    aws_rds as rds,
    CfnOutput,
)
import aws_cdk.aws_s3 as s3
 
class MvpV2AppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

# Create the web server VPC
        self.vpc_webserver = ec2.Vpc(self, "WebServerVPC",
            ip_addresses=ec2.IpAddresses.cidr('10.0.1.0/24'),
            max_azs=3,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", cidr_mask=28, subnet_type=ec2.SubnetType.PUBLIC),
                ec2.SubnetConfiguration(name="private", subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
            ],
            enable_dns_support=True,
            enable_dns_hostnames=True,
            nat_gateways=1,
        )

        # Create the admin server VPC
        self.vpc_adminserver = ec2.Vpc(self, "AdminServerVPC",
            ip_addresses=ec2.IpAddresses.cidr('10.0.2.0/24'),
            availability_zones=["eu-central-1b"],
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", cidr_mask=28, subnet_type=ec2.SubnetType.PUBLIC),
            ],
            enable_dns_support=True,
            enable_dns_hostnames=True,
            nat_gateways=0,
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
            destination_cidr_block="10.0.2.0/24",
            vpc_peering_connection_id=self.Peering_connection.ref
            )
        
        # Get the route tables and subnets for the VPC peering connection from adminserver to webserver
        self.subnet_adminserver = self.vpc_adminserver.public_subnets[0]
        self.rt_sub_adminserver = self.subnet_adminserver.route_table

        #Add route from adminserver to webserver
        self.rt_adminserver_peering = ec2.CfnRoute(self, "rt-adminserver-peering",
            route_table_id=self.rt_sub_adminserver.route_table_id,
            destination_cidr_block="10.0.1.0/24",
            vpc_peering_connection_id=self.Peering_connection.ref
            )

        # Define Network ACLs for the webserver as for the adminserver
        # Create Network ACL for the webserver public and private:
        self.nacl_web_public = ec2.NetworkAcl(self, 'nacl-web-public', 
            network_acl_name='nacl-web-public',
            vpc=self.vpc_webserver,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
            )
        
        self.nacl_web_private = ec2.NetworkAcl(self, 'nacl-web-private', 
            network_acl_name='nacl-web-private',
            vpc=self.vpc_webserver,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
            )
        
        # Create Network ACL for the adminserver public:
        self.nacl_admin_public = ec2.NetworkAcl(self, 'nacl-admin-public', 
            network_acl_name='nacl-admin-public',
            vpc=self.vpc_adminserver,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
            )

        # NACLs for private subnet of webserver:
        # Inbound and outbound rules in vpc_web_private for ephemeral ports
        self.nacl_web_private.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=80,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),    
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Inbound and Outbound rule in vpc_web_private for HTTP 
        self.nacl_web_private.add_entry("Allow HTTP in",
        cidr=ec2.AclCidr.any_ipv4(),
        rule_number=90, 
        traffic=ec2.AclTraffic.tcp_port(80),
        direction=ec2.TrafficDirection.INGRESS
        )

        # Inbound and outbound rules in vpc_web_private for HTTPS 
        self.nacl_web_private.add_entry("Inbound HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),   
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(443), 
            direction=ec2.TrafficDirection.INGRESS
            )
        # Inbound rule for SSH from Admin
        self.nacl_web_private.add_entry("Inbound SSH from Admin",
            cidr=ec2.AclCidr.ipv4('10.0.2.0/24'),        #VPC admin
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port(22),  
            rule_action=ec2.Action.ALLOW,      
            direction=ec2.TrafficDirection.INGRESS,
            )
        
        # Inbound rule for RDP from Admin
        self.nacl_web_private.add_entry("Inbound RDP from Admin",
            cidr=ec2.AclCidr.ipv4('10.0.2.0/24'),        #VPC admin
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port(3389),  
            rule_action=ec2.Action.ALLOW,      
            direction=ec2.TrafficDirection.INGRESS,
            )
        
        # Outbound All
        self.nacl_web_private.add_entry("Outbound-All",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=150,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS
            )
        
      
        # NACLs for public subnet of adminserver:
        # Inbound rule in vpc_admin for ephemeral ports 
        self.nacl_admin_public.add_entry("Inbound-Ephemeral",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=90,
            traffic=ec2.AclTraffic.tcp_port_range(49152, 65535),    # Windows 
            direction=ec2.TrafficDirection.INGRESS
            )
        
        # Inbound rule in vpc_admin for RDP from the admin IP
        admin_ip = "83.83.79.192/32" 

        self.nacl_admin_public.add_entry("Inbound RDP from Admin-ip",
            cidr=ec2.AclCidr.ipv4(admin_ip),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(3389),  
            rule_action=ec2.Action.ALLOW,      
            direction=ec2.TrafficDirection.INGRESS,
            )
        
        # Outbound All
        self.nacl_admin_public.add_entry("Outbound-All",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS
            )

        
         # Create Security Group for Webserver
        sg_webserver = ec2.SecurityGroup(self,"sg_WebServer", 
        vpc = self.vpc_webserver,
        description = "sg_webserver",                                                                  
        )

        sg_webserver.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "Allow SSH from Adminserver")
        sg_webserver.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(443), "Allow HTTPS from Adminserver")
        sg_webserver.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "Allow HTTP from Adminserver")
        

        # Create Security Group for Adminserver
        sg_adminserver = ec2.SecurityGroup(self,"sg_AdminServer", 
        vpc = self.vpc_adminserver,
        description = "sg_webserver",                                                                  
        )

        sg_adminserver.add_ingress_rule(ec2.Peer.ipv4(admin_ip), ec2.Port.tcp(3389), "Allow RDP from Admin-IP") 

        # Create Security group for autoscaling
        sg_autoscaling = ec2.SecurityGroup(self,"sg_autoscaling", 
        vpc = self.vpc_webserver,
        description = "sg_autoscaling",
        allow_all_outbound =True,                                                                  
        )

        # Create key-pair for SSH connection to the webserver
        keypair_adminIT = ec2.KeyPair.from_key_pair_name(self, "kp-adminIT",
            key_pair_name="kp-adminIT",
            )
        keypair_webserver = ec2.KeyPair.from_key_pair_name(self, "kp-WebServer",
            key_pair_name="kp-WebServer",
            )
        
        # Import User Data for Webserver
        with open("./mvp_v2_app/user_data.sh") as f:
            self.user_data = f.read()

        # S3 bucket configurations:
        # Create S3 bucket  
        bootstrap_bucket = s3.Bucket(self, "webserver-bucket",
                                bucket_name="webserver-bucket-mvp1point1-987654321",
                                encryption=s3.BucketEncryption.S3_MANAGED,
                                removal_policy=RemovalPolicy.DESTROY,
                                auto_delete_objects=True
                                )
        
        # Upload scripts to bucket 
        s3deploy.BucketDeployment(self, "DeployScripts",
            sources=[s3deploy.Source.asset("./scripts")],
            destination_bucket=bootstrap_bucket
            )
        
        # Allow access to the bucket from the EC2 instance 
        webserver_role = iam.Role(self, "role-webserver",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )
        webserver_role.add_to_policy(iam.PolicyStatement(
            actions=["s3:GetObject"],
            resources=[bootstrap_bucket.arn_for_objects("*")]
        ))
        
         # Create Webserver instance
        self.instance_webserver = ec2.Instance(self, "instance-webserver",
            instance_name="instance-webserver",
            vpc=self.vpc_webserver,  
            role=webserver_role,                            
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),                                   
            key_name=keypair_webserver.key_pair_name,                    
            security_group=sg_webserver,
            private_ip_address="10.0.1.70",                   
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),    
            block_devices=[ec2.BlockDevice(
                device_name="/dev/sdh",                        
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=40,                              
                    encrypted=True,                             
                    )
                )],
            user_data=ec2.UserData.custom(self.user_data), 
            )
        
        #  # Run script from S3 during startup
        # self.instance_webserver.ec2.UserData.custom(self.user_data).add_s3_download_command(
        # bucket=bootstrap_bucket,
        # bucket_key="setup.sh",
        # local_file="/tmp/setup.sh"  
        # )
        # ec2.UserData.custom(self.user_data).add_commands("chmod +x /tmp/setup.sh", "/tmp/setup.sh")

        # Create Adminserver instance
        self.instance_adminserver = ec2.Instance(self, "instance-adminserver",
            instance_name="instance-adminserver",
            vpc=self.vpc_adminserver,                               
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC),                                   
            key_name=keypair_adminIT.key_pair_name,                    
            security_group=sg_adminserver, 
            private_ip_address="10.0.2.10",                  
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),  
            machine_image=ec2.WindowsImage(
                ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),    
            block_devices=[ec2.BlockDevice(
                device_name="/dev/sda1",                        
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=40,                              
                    encrypted=True,                             
                    )
                ),
                 ec2.BlockDevice(
                device_name="/dev/sdf",                         
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=100,                            
                    encrypted=True,    
                    )                         
                    )], 
            )
        

        # # Webserver Autoscaling
        # webserver_instance = autoscaling.AutoScalingGroup(
        #     self,"Webserver-instance",
        #     vpc=self.vpc_webserver,
        #     vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),  
        #     security_group=sg_webserver,
        #     role=webserver_role,
        #     instance_type = ec2.InstanceType.of(
        #         ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),  
        #     machine_image=ec2.AmazonLinuxImage(
        #         generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023),
        #     user_data=ec2.UserData.custom(self.user_data),
        #     key_name=keypair_adminIT.key_pair_name,
        #     block_devices=[ec2.BlockDevice(
        #         device_name="/dev/xvda",                       
        #         volume=ec2.BlockDeviceVolume.ebs(
        #             volume_size=15,                              
        #             encrypted=True,                            
        #             )
        #         )],
        #     desired_capacity=1,
        #     min_capacity=1,
        #     max_capacity=3,
        #     health_check=autoscaling.HealthCheck.elb(grace=Duration.minutes(5)),
        #  )
        

        # # Create a custom metric for CPU utilization
        # cpu_metric = cloudwatch.Metric(
        #     namespace="AWS/EC2",
        #     metric_name="CPUUtilization",
        #     dimensions_map={"AutoScalingGroupName": webserver_instance.auto_scaling_group_name},
        #     statistic="Average",
        # )

        # # Create a step scaling policy
        # step_scaling_policy = autoscaling.StepScalingPolicy(
        #     self,
        #     "Step-Scaling-Policy",
        #     auto_scaling_group=webserver_instance,
        #     metric=cpu_metric,
        #     adjustment_type=autoscaling.AdjustmentType.CHANGE_IN_CAPACITY,
        #     scaling_steps=[
        #         autoscaling.ScalingInterval(lower=0, upper=40, change=-1),
        #         autoscaling.ScalingInterval(lower=70, change=1),
        #     ],
        # )

        # # Certificate ARN 
        # certificate_arn_alb="arn:aws:acm:eu-central-1:052055660545:certificate/fa9f2ae1-9196-4a4d-9293-5c4c45246248"

        # # Create loadbalancer for the webserver
        # loadbalancer_webserver = elbv2.ApplicationLoadBalancer(self, "LB-Webserver",
        #                                             vpc=self.vpc_webserver,
        #                                             internet_facing=True,
        #                                             load_balancer_name="LB-Webserver",
        #                                             )
        
        # # Output the Public IP (DNS Name) of the load balancer:
        # CfnOutput(self, "WebServer_Public_IP", value=loadbalancer_webserver.load_balancer_dns_name)
        
        # # Create target group for the loadbalancer
        # targetgroup_webserver = elbv2.ApplicationTargetGroup(self, "TG-Webserver",
        #     vpc=self.vpc_webserver,
        #     port=443,
        #     targets=[webserver_instance],
        #    )

        # # Import self signed certificate from console
        # self.certificate_signed = cm.Certificate.from_certificate_arn(self, "certificate-signed",
        #     certificate_arn=certificate_arn_alb
        #     )

        # # Add listener for port 443
        # https_listener = loadbalancer_webserver.add_listener("HTTPS",
        #     port=443,
        #     ssl_policy=elbv2.SslPolicy.TLS12,
        #     certificates=[self.certificate_signed],
        #     default_target_groups=[targetgroup_webserver]
        #     )

        # # Add listener to the ALB for port 80 and redirect traffic to port 443
        # http_listener = loadbalancer_webserver.add_listener("HTTP",
        #     port=80,
        #     default_action=elbv2.ListenerAction.redirect(
        #         port="443",
        #         protocol="HTTPS",
        #         )
        #     )
        
        # # Create backup vault
        # backup_vault = backup.BackupVault(self, "BackupVault",
        # backup_vault_name="WebServerBackupVault",
        # removal_policy=RemovalPolicy.DESTROY
        # )

        # # Create backup plan for the webserver 
        # self.backupplan = backup.BackupPlan(self, "backupplan",
        #     backup_plan_name="7day-Backupplan",
        #     backup_vault=backup_vault,
        #     backup_plan_rules=[backup.BackupPlanRule(
        #         rule_name="7days",
        #         start_window=Duration.hours(1),             
        #         completion_window=Duration.hours(2),        
        #         delete_after=Duration.days(7),              
        #         schedule_expression=events.Schedule.cron(
        #             hour="0",       #UTC
        #             minute="0", )   
        #         )]
        #     )
        # # Select webserver for backup plan
        # self.backupplan.add_selection("add-webserver", 
        #     backup_selection_name="webserver-backup",
        #     resources=[
        #         backup.BackupResource.from_ec2_instance(self.instance_webserver)
        #         ]
        #     )
        
        
        # # S3 bucket voor database backups
        # backup_bucket = s3.Bucket(self, "BackupBucket",
        # encryption=s3.BucketEncryption.S3_MANAGED,
        #                         removal_policy=RemovalPolicy.DESTROY, )


        # # Verbind de KMS key aan de backup bucket
        # DB_role = iam.Role(self, "role-DB",
        #     assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        # )
        # DB_role.add_to_policy(iam.PolicyStatement(
        #     actions=["s3:GetObject", "s3:PutObject"],
        #     resources=[backup_bucket.arn_for_objects("*")]
        # ))

        # # Create Security Group for database
        # self.securitygroup_DB = ec2.SecurityGroup(self, "securitygroup_DB",
        #     vpc=self.vpc_webserver,
        #     description="securitygroup_DB"
        #     )
        
        # # Allow trafic from webserver to database
        # self.securitygroup_DB.add_ingress_rule(
        # ec2.Peer.ipv4("10.10.10.0/24"),
        # ec2.Port.tcp(3306)  
        # )

        # # Sta verkeer toe van database naar S3  
        # self.securitygroup_DB.add_egress_rule(
        # ec2.Peer.ipv4("3.5.140.0/21"),
        # ec2.Port.tcp(443)
        # )

        # # MySQL RDS instance
        # mysql_db_webserver = rds.DatabaseInstance(
        # self, "MySQLDB",
        # vpc=self.vpc_webserver, 
        # vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
        # engine=rds.DatabaseInstanceEngine.MYSQL,
        # instance_type=ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MICRO),
        # allocated_storage=20, 
        # iops=300,
        # storage_encrypted=True,
        # multi_az=True,
        # publicly_accessible=False,
        # database_name="mydb-webserver",
        # deletion_protection=False,
        # backup_retention=Duration.days(30),
        # removal_policy=RemovalPolicy.DESTROY, 
        # )


  



       
        

        

