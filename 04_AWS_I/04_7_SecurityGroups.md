# Security Groups
In Amazon EC2 (Elastic Compute Cloud), a security group is a virtual firewall for your instances to control inbound and outbound traffic. It acts as a set of rules that govern the traffic allowed to and from an EC2 instance.

Security Groups are stateful virtual firewalls that can be assigned to instances. They do not run in the OS, but rather in the VPC.
One Security Group can be assigned to multiple instances. The other way around, one instance can have up to 5 Security Groups.

Security Groups only have allow rules. Everything not explicitly allowed is automatically implicitly denied.

By carefully configuring security group rules, you can control the network traffic to and from your EC2 instances, ensuring that only the necessary and desired communication is allowed while maintaining a secure environment.

Network Access Control Lists (NACLs) are another layer of security in Amazon Web Services (AWS) that operate at the subnet level. While security groups are associated with EC2 instances, NACLs are associated with subnets.

Here's an overview of NACLs:

1. __Subnet-Level Filtering:__
NACLs act as a stateless network firewall that controls traffic in and out of one or more subnets.
They are associated with a specific subnet, affecting all traffic entering or leaving that subnet.
2. __Ordered Rules:__
NACLs have numbered rules, and the rules are evaluated based on their order (lowest to highest).
The first rule that matches the traffic is applied, and subsequent rules are not evaluated.
3. __Stateless Operation:__
Unlike security groups, NACLs are stateless. If you allow inbound traffic, you must also explicitly allow the corresponding outbound traffic.
4. __Allow/Deny Rules:__
Each rule in an NACL is either an ALLOW or DENY rule.
If a rule explicitly denies a packet, the packet is discarded. Otherwise, it is allowed.
5. __Rule Evaluation:__
Rules are evaluated based on criteria such as source/destination IP address, protocol, and port range.
Default NACL:
When you create a new VPC (Virtual Private Cloud), it comes with a default NACL that allows all inbound and outbound traffic.
6. __Association with Subnet:__
Each subnet in a VPC must be associated with a network ACL. If no association is made, the subnet is associated with the default NACL.
7. __Logging:__
NACLs do not provide logging by default. To log denied traffic, you would need to configure additional logging mechanisms.
8. __Allow/Deny Traffic Based on Rules:__
NACLs allow you to define specific rules to allow or deny traffic based on your network architecture and security requirements.  

In summary, while security groups are associated with EC2 instances and operate at the instance level, NACLs are associated with subnets and operate at the subnet level. Combining security groups and NACLs provides a layered approach to controlling access and securing your AWS resources. 


### Sources
* https://chat.openai.com 
* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html
* https://www.youtube.com/watch?v=ttc0b2NZTV0 

