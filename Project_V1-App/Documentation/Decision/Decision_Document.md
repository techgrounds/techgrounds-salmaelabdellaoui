# Decision document 

In this document, my considirations will be outlined and my decisions will be explained. This document will also include my assumptions and improvements. It serves as a base for my design documentation. 

__Table of content:__ 
- [Decision document](#decision-document)
  - [Requirements from the product owners](#requirements-from-the-product-owners)

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
-    
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
- Development: maximum €10.
- Production: maximum €150.




