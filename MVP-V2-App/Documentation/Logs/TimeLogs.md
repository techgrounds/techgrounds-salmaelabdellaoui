# Daily Logs 

Welcome to my daily logs, where I document the progress, challenges, and next steps of my ongoing project. 

Let's make each day a step closer to success!     

- [Daily Logs](#daily-logs)
  - [January 08, 2024](#january-08-2024)
  - [January 09, 2024](#january-09-2024)
  - [January 10, 2024](#january-10-2024)
  - [January 11, 2024](#january-11-2024)
  - [January 15, 2024](#january-15-2024)
  - [January 16, 2024](#january-16-2024)
  - [January 17, 2024](#january-17-2024)
  - [January 18, 2024](#january-18-2024)
  - [January 19, 2024](#january-19-2024)
  - [January 22, 2024](#january-22-2024)
  - [January 23, 2024](#january-23-2024)
  - [January 24, 2024](#january-24-2024)
  - [January 25, 2024](#january-25-2024)
  - [January 26, 2024](#january-26-2024)
  - [January 30, 2024](#january-30-2024)
  - [January 31, 2024](#january-31-2024)
  - [February 01, 2024](#february-01-2024)
  - [February 02, 2024](#february-02-2024)
  - [February 05, 2024](#february-05-2024)
  - [February 06 till February 16 SICK](#february-06-till-february-16-sick)
  - [February 19, 2024](#february-19-2024)
    - [V1.0](#v10)
    - [V1.1](#v11)


## January 08, 2024

__Daily report__  

It is the first day of the final project (Project V1 application).

- Familiarizing myself with the final project requirements  
    - Learn environment from TechGrounds   
    - The goal of the project and criteria
- Determining the necessary components and identifying the required installations: 
    - Making an account on Jira   
    - AWS cloud environment   
    - Visual Studio Code:   
            - Python  
            - AWS CLI  
            - AWS CDK Toolkit  
            - Node   
            - Pip 
- Outlining the next steps

## January 09, 2024  
  
__Daily report__

On Wednesday, January 10th, our team has scheduled a meeting with the product owners. During this session, we aim to seek clarification on the program, discuss the requirements, and understand their expectations from my role.

__Tasks completed__

- I have reviewed all the requirements of the final product, based on that I formulated questions for the product owners.
- I collaborated with my team for an hour to discuss the questions and finalize them, creating a comprehensive set for our meeting with the product owners.

## January 10, 2024 

__Daily report__

At 9:15 in the morning, we held a meeting with the product owner. During this session, we addressed all questions and clarified every detail regarding their requirements and interests.

__Tasks completed__

- Finalized the requirement list of the application 
- Made an account on Jira 
- Installed AWS CLI in my terminal 
- Orienting about the CDK toolkit 

## January 11, 2024

__Daily report__

I created my project folder today and installed all the necessary components in my project environment, such as the CDK toolkit, Pip, and Node.

I also linked my AWS environment to my project in VS Code, and I executed a sample project using AWS SNS and SQS services.

__Obstacles__ 

My Python language interpreter did not match the language of the AWS CDK kit. Which caused problems. 

## January 15, 2024 

__Daily report__

I fixed the problem related to my language interperter. Everything is correctly installed. I worked half a day on this project. 

__Tasks completed__

- Meeting with the team to discuss our list of services and assumptions which we will use in our infrastructure.

## January 16, 2024

__Daily report__ 

Working on the structure of my github and making it ready for the building phase. Finishing of my exploration user stories.

__Tasks completed__

- Structured my Github folders 
- Updated my logs 
- Updated my documentations 

## January 17, 2024

__Daily report__

Finalizing all exploration epics in github. Completing the design for the infrastructure and start coding in CDK. 

__Tasks completed__
- All exploration epics are done
- The design for the infrastructure is in progress 
- I started coding 

## January 18, 2024

__Daily report__  
Building the infrastructure as a code. starting with setting up the VPC, region, subnets etc. 

__Tasks completed__  
- Exploring the CDK environment 

## January 19, 2024

__Daily report__  
- Setting up the VPC environment in AWS 

## January 22, 2024

__Daily report__  
- Setting up the VPC environment in AWS 

__Obstacles__  
- I changed the given infrastructure to one VPC, but this was not allowed. We had to use VPC peering (for our own learn curve)


## January 23, 2024

__Daily report__  
- Setting up the right VPC infrastructure

## January 24, 2024

__Daily report__  
- Setting up VPC peering 

__Obstacles__
- The routtabels where not defined by me in the main stack, so the route table of the VPC peering could not find them. 

## January 25, 2024

__Daily report__  
- Finalizing my VPCs and VPC peering 
- Helping my peers with their errors

## January 26, 2024

__Daily report__  
- Learning how to set up Network ACLs   
- Presentations of group members 


## January 30, 2024

__Daily report__
- Finalizing my network infrastructure by adding the right rules for my network ACLs. 
- Updating my documentation 
- Helping my peers with their errors  
- The Iac code can be found in the mvp_v1_app map 


| Status  | User Story | Description | Deliverable |
| - | - | - | - |
| Finished | As a customer, I want a working application with which I can deploy a secure network. | The application must build a network that meets all requirements. An example of a stated requirement is that only traffic from trusted sources may access the management server. | IaC code for the network and all components. |

## January 31, 2024

__Daily report__  
- Starting with the second user stories (adding the webserver to the code) 

__Obstacles__  
- The instance could not find the public subnet of my VPC   
I was able to define my public subnet in my main code and then allocate that definition in my instance code. This worked out for me. I need to do that extra step because I configured my public subnets in a different file. The instance code could not read those, that is why it gave me the error 'no public subnets in this VPC'. 

## February 01, 2024

__Daily report__ 

- I was able to fix the problem with the subnet that could not be found. But I gained another error 'Public Subnet and Security Group belong to different network' 
- I had a meeting with my booking mentor, He looked with me in my code to try and find out the problem, after almost an hour he was also not able to solve it. 

## February 02, 2024
__Daily report__   
- I tried to fix the error, but it did not work out
- I prepared my presentation and presented what I accomplished and what my problems are. 

## February 05, 2024  
__Daily report__    
- In the morning I tried for the last time to fix the problem, but it did not worked out. 
- I decided to start over using a different contruct for my VPC. 

## February 06 till February 16 SICK 

## February 19, 2024 
Because I was missing 2 weeks of working on the project I had to prioritize my tasks. The following user stories where finished within week 8 of 2024. 

### V1.0
Here are the user stories for the epic V1.0.

| Status | User Story | Description | Deliverable |
| - | - | - | - |
| Finished | As a customer, I want a working application with which I can deploy a secure network. | The application must build a network that meets all requirements. An example of a stated requirement is that only traffic from trusted sources may access the management server. | IaC code for the network and all components. |
| Finished | As a customer I want a working application with which I can deploy a working web server. | The application must start a web server and make it available to the general public. | IaC code for a web server and all supplies. |
| Finished | As a customer, I want a working application with which I can deploy a working management server. | The application must start a management server and make it available to a limited audience. | IaC code for a management server with all the necessities. |
| Finished | As a customer I want a storage solution in which bootstrap/post-deployment script can be stored. | There must be a location available where bootstrap scripts become available. This script should not be publicly accessible. | IaC code for a script storage solution. |
| Finished | As a customer, I want all my data in the infrastructure to be encrypted. | Much value is attached to the security of data at rest and in motion. All data must be encrypted. | IaC code for encryption facilities. |
| Finished | As a customer, I want to have a backup every day that is retained for 7 days. | The customer would like to have a backup available should it be necessary to restore the servers to a previous state. (Make sure the Backup actually works) | IaC code for backup facilities. |
| 7 | As a customer I want to know how I can use the application. | Make sure the customer can understand how to use the application. Make sure it is clear what the customer must configure before the deployment can start and which arguments the program needs. | Documentation for using the application. |
| 8 | As a customer, I want to be able to deploy an MVP for testing. | The customer wants to test your architecture internally before using the code in production. Ensure that configuration is available that allows the customer to deploy an MVP. | Configuration for an MVP deployment. |
<br>

### V1.1
Here are the user stories for the epic V1.1.

|  | Status | Description | Deliverable |
| - | - | - | - |
| 1 | Finished | The web server must no longer be "naked" on the internet. The customer would prefer to see a proxy intervene. The server will also no longer need to have a public IP address. | IaC code |
| 2 | Finished | If a user connects to the load balancer via HTTP, this connection should be automatically upgraded to HTTPS. | IaC code |
| 3 | Finished | The connection must be secured with at least TLS 1.2 or higher. | IaC code |
| 4 | Finished | The web server must undergo a health check on a regular basis. If the web server fails this health check, the server should be automatically restored. | IaC code |
| 5 | Finished | If the web server comes under persistent load, a temporary additional server should be started. | IaC code |
|  | As a customer I want to know how I can use the application. | Make sure the customer can understand how to use the application. Make sure it is clear what the customer must configure before the deployment can start and which arguments the program needs. | Documentation for using the application. |
|  | As a customer, I want to be able to deploy an MVP for testing. | The customer wants to test your architecture internally before using the code in production. Ensure that configuration is available that allows the customer to deploy an MVP. | Configuration for an MVP deployment. |
<br>

