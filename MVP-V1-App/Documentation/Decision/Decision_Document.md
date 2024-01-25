# <a id="top">Decision Document</a>

In this document, my considirations will be outlined and my decisions will be explained. This document will also include my assumptions and improvements. It serves as a base for my design documentation. 
<br>

__Table of contents:__ 
- [Decision Document](#decision-document)
  - [Requirements from the product owners](#requirements-from-the-product-owners)
  - [A clear overview of the assumptions](#a-clear-overview-of-the-assumptions)
  - [Services for the cloud infrastructure](#services-for-the-cloud-infrastructure)

## Requirements from the product owners
Information given by the product owners about the business, the application, and the requirements: 

__Business:__  
- Company is based in the Netherlands
- Costumers are 99% based in the Netherlands 
- One IT administrator at senior level (needs to be hired) 
- Peak traffic of the webserver is during office hours

The goals of the business are:
- A working webserver which can be accessed via internet
- A cloud infrastructure in AWS using Infrastructure as a code
- In the future there could be 30+ workstations 
- Scalability, flexibility, low latency, and high availability

__Requirements of the application__

__Network__   
- The following IP ranges are used: 10.10.10.0/24 & 10.20.20.0/24.
- Subnet for future workstations must be considered (at least 30 usable IP addresses), excluding room for possible growth. (Large growth is not expected in the short term).   
    
__Webserver & Database__   
- Website 24/7 online.
- The web server must be installed in an automated manner.
- SQL database needed for the database; post script deployment must be able to run.
- Connection from the database to the webserver must be able and the other way around. 
- Scalability of the webserver; is not clear whether the customer wants this (budget), but it does sound interesting according to the product owner.

__Admin/ management server__   
- The admin / management server must be reachable with a public IP.
- The admin / management server must only be accessible from trusted locations (office/admin’s home).
- Admin / management server must run on windows
- Admin server should not go down with the workstations if there is a malfunction.
- Access to admin / management server: I will be using my own IP address during development. In production this will be the IP address of the admin’s trusted location.  
  

__Storage__  
- There must be a location available where bootstrap scripts can be stored. This script should not be publicly accessible.    
    
    __Scripts__    
Installation scripts  
Configuration scripts  
Post deployment scripts  
No expiration date for the stored scripts  
Access to the scripts: admin & machines/processes    that call the scripts

__Back up__  
- The web server must be backed up daily. The backups must be retained for 7 days.
- Recovery Point Objective (RPO): 24 hours.
- Recovery Time Objective (RTO): 1 hour.
- Back-up should preferably take place at a time that it is not busy. 4 AM for example.

__Security__  
- Much value is attached to the security of data at rest and in motion. All data must be encrypted.
- All VM disks must be encrypted.
- VM encryption: industry standard.
- All subnets must be protected by a firewall at subnet level.
- SSH or RDP connections to the web server may only be established from the admin server.

__Budget__  
- As cheap as possible within the necessary requirements.
- No support plans
- Development: maximum €10.
- Production: maximum €150.  
  
*Back to [top](#top)* 

## A clear overview of the assumptions  

__Region__  
From the given infrastructure design, two regions where selected. After a thorough evaluation of the company's needs, taking into consideration that a significant portion of the customers are located in the Netherlands, I have come to the conclusion that adding an extra AWS region may not be necessary at this time. 

The customers are primarily local, making the existing AWS region close enough to provide optimal performance. Additionally, we do not have specific laws and regulations that necessitate an extra region.

Furthermore, there are already two availability zones at our disposal, providing the company with sufficient options for disaster recovery scenarios without the complexity and costs associated with an additional region.   
  
__Security__  
Given the statement that protection against attacks and hacking will be handled in-house, our assumption is that while we acknowledge the importance of security measures, the primary focus may not be extensively on proactive measures against attacks. Instead, our approach will lean towards ensuring robust data protection through the encryption of data at rest.  
  
__Manual Updates and Patches__  
Considering that updates and patches will be manually handled by their internal IT administration personnel, our assumption is that the choice of services will be made in alignment with budget considerations and service costs. This flexibility allows for the selection of services ranging from serverless options, where maintenance tasks are abstracted away, to servers where updates and patches need to be managed independently.    

*Back to [top](#top)* 

## Services for the cloud infrastructure

The following list indicates the AWS services which will be used in the cloud infrastructure. 

__Cloud Financial Management__
- 🟩 Billing and Cost Management: View and pay bills, analyze and govern your spending, and optimize your costs.
	- Cost explorer: Regularly review costs using AWS Cost Explorer to stay within budget.       

__Compute__ 
- 🟧 EC2: Virtual servers in the cloud.
	- for web server (AMI)
	- for admin server (AMI)
	- Security groups
	- Application Load balancer 
	- EBS container  
	- Autoscaling 
	- Elastic IP 

__Database__
- 🟦 RDS: Managed Relational Database Service (SQL).
	- AWS back-up/ EBS snapshots

__Management & Governance__
- 🟥 CloudTrail: Track User Activity and API Usage.
- 🟥 Cloudwatch: (To monitor performance logs)

    __Alarms:__ Set up alarms for critical metrics.  
    __Events:__ Schedule backups and automate tasks at a convenient time.

__Networking & Content Delivery__
- 🟪 VPC: Isolated Cloud Resources.
- 🟪 Netwerk ACLs
- 🟪 Route53 
- 🟪 Cloudfront   

__Security, Identity, & Compliance__
- 🟥 Certificate Manager: Provision, Manage, and Deploy SSL/TLS Certificates.
- 🟥 IAM: Manage access to AWS resources.
- 🟥 Key Management Service: Securely Generate and Manage AWS Encryption Keys
	(For RDS databases/EBS volumes)
-  🟥 AWS secrets Manager (for database credentials etc. system manager documents)   

__Storage__
- 🟩 S3: Scalable Storage in the Cloud 
- 🟩 AWS Backup 


*Back to [top](#top)* 