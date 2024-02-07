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
