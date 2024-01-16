# Theoretical and practical experience in AWS

### CloudFront 

Amazon CloudFront is a globally distributed network of servers that can deliver content to users. The netowrk has edges (servers) in many locations around the world. The servers cache content closer to the users to improve access speed. Creation of new distributions can be automated.

Caching data in multiple locations also provide data redundancy, improving reliability of access. Amazon CloudFront uses RTMP protocol for video streaming and HTTP or HTTPS for web content.

Amazon CloudFront speeds up distribution of your static and dynamic web content, such as .html, .css, .php, image, and media files. When users request your content, CloudFront delivers it through a worldwide network of edge locations that provide low latency and high performance.  

![CloudFront](../00_includes/05_AWS_II/18.Theo-Prac.png) 

### Route 53  
Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. You can use Route 53 to perform three main functions in any combination: domain registration, DNS routing, and health checking.  
  
1. __Register domain names:__  

   Your website needs a name, such as example.com. Route 53 lets you register a name for your website or web application, known as a domain name.

2. __Route internet traffic to the resources for your domain:__  

   When a user opens a web browser and enters your domain name (example.com) or subdomain name (acme.example.com) in the address bar, Route 53 helps connect the browser with your website or web application.    

![Route53](../00_includes/05_AWS_II/19.Route53.png) 

3. __Check the health of your resources:__  

   Route 53 sends automated requests over the internet to a resource, such as a web server, to verify that it's reachable, available, and functional. You also can choose to receive notifications when a resource becomes unavailable and choose to route internet traffic away from unhealthy resources.  

![Route53](../00_includes/05_AWS_II/20.Healthycheck.png)   


### Sources
* https://www.w3schools.com/whatis/whatis_aws_cloudfront.asp 
* https://docs.aws.amazon.com/cloudfront/
* https://www.youtube.com/watch?v=BujVA_Jg6W0
* https://cloud.contentraven.com/awspartners/w3schools/content-viewer/517004/1/11/0 
* https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html 
* https://www.youtube.com/watch?v=10JKpg-eqZU
* https://www.w3schools.com/aws/aws_cloudessentials_amazonelasticfilesystem.php
* https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html
* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEFS.html 
* https://www.w3schools.com/aws/aws_cloudessentials_amazonrds.php 
* https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html 
* https://www.youtube.com/watch?v=tLp8pPNdDXQ 
* https://www.youtube.com/watch?v=ZCt3ctVfGIk 
* https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.environments.html
* https://www.youtube.com/watch?v=cfO5mfI_EdM

### Practical experience with AWS services

### Elastic File System (EFS)

Amazon Elastic File System (Amazon EFS) provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance. Amazon EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files. 

Amazon EFS offers the following storage class options for different use cases:

* __Standard storage classes:__   
(Recommended) – EFS Standard and EFS Standard–Infrequent Access (Standard–IA), which offer Multi-AZ resilience and the highest levels of durability and availability.
* __One Zone storage classes:__   
 – EFS One Zone and EFS One Zone–Infrequent Access (EFS One Zone–IA), which offer you the choice of additional savings by choosing to save your data in a single Availability Zone  

 ##### Exercise 

 1. Create an EFS file system using Amazon EFS Quick Create when making an EC2

 ![EFS](../00_includes/05_AWS_II/21.EC2created.png)
![EFS](../00_includes/05_AWS_II/22.EFS-storage.png)
![EFS](../00_includes/05_AWS_II/23.EFS-Storage-settings.png)
![EFS](../00_includes/05_AWS_II/24.Bashscript.png)
![EFS](../00_includes/05_AWS_II/25.NetworkSettings.png)
![EFS](../00_includes/05_AWS_II/26.Securitygroup.png)

 2. Test the EFS file system

![EFS](../00_includes/05_AWS_II/27.TestEFS.png)
![EFS](../00_includes/05_AWS_II/28.TesteEFS-file.png)

3. Delete the EFS file system
![EFS](../00_includes/05_AWS_II/29.DeleteFileSystem.png) 


### RDS and Aurora 
AWS RDS is also called AWS Relational Database Service. RDS is a service that automates database tasks. It enables running relational databases in AWS Cloud.

Amazon RDS is responsible for hosting the software components and infrastructure of DB instances and DB cluster. You are responsible for query tuning, which is the process of adjusting SQL queries to improve performance.

Amazon Aurora is a relational database ideal for large organizations and enterprises. It offers high availability of data. It is excellent for managing large amounts of data. It is five times faster than a MySQL database. It is three times faster than a PostgreSQL database. 

Amazon Aurora creates six copies of data across three Availability Zones and a data backup on Amazon S3. It ensures the data is available at all times. 

##### Excercise

1. Configure your own RDS Aurora Serverless MySQL instance in the AWS console.   

Instead of provisioning and managing database servers, I specify Aurora capacity units (ACUs). Here, load is CPU utilization and the number of connections. When capacity is constrained by either of these, Aurora Serverless v1 scales up. 

Furthermore, I specified the capacity range, the serverless Aurora, and I enabled the API which allows me to interact with my database. The VPC that is used, is the default one with the three subnets. 

![Aurora](../00_includes/05_AWS_II/30.AuroraSettings.png) 
![Aurora](../00_includes/05_AWS_II/31.EngineAurora.png) 
![Aurora](../00_includes/05_AWS_II/32.AuroraIAM.png) 
![Aurora](../00_includes/05_AWS_II/33.InstanceConfig.png) 
![Aurora](../00_includes/05_AWS_II/34.APIEnabeld.png) 
![Aurora](../00_includes/05_AWS_II/35.AuroraDatabaseMade.png) 

### AWS Elastic Beanstalk

With AWS Elastic Beanstalk, you can quickly deploy and manage applications in the AWS Cloud without worrying about the infrastructure that runs those applications. AWS Elastic Beanstalk reduces management complexity without restricting choice or control. You simply upload your application, and AWS Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.

Elastic Beanstalk supports applications developed in Go, Java, .NET, Node.js, PHP, Python, and Ruby. When you deploy your application, Elastic Beanstalk builds the selected supported platform version and provisions one or more AWS resources, such as Amazon EC2 instances, to run your application.

#### Exercise 

1. Create an example application   

![Beanstalk](../00_includes/05_AWS_II/36.ConfigBean.png)

    * Create IAM Role for EC2 instance profile  

![Beanstalk](../00_includes/05_AWS_II/41.IAMCreated.png)    

 * Continue   

![Beanstalk](../00_includes/05_AWS_II/37.ServiceAcces.png)
![Beanstalk](../00_includes/05_AWS_II/38.NetworkBean.png)
![Beanstalk](../00_includes/05_AWS_II/39.ConfigInstance.png)
![Beanstalk](../00_includes/05_AWS_II/40.congratulations.png)

So what has been created for this example application?

1. An Amazon Elastic Compute Cloud (Amazon EC2) instance (virtual machine)
![Beanstalk](../00_includes/05_AWS_II/42.EC2created.png)
2. An Amazon EC2 security group
![Beanstalk](../00_includes/05_AWS_II/43.EC2securitygroup.png)
3. An Amazon Simple Storage Service (Amazon S3) bucket 
![Beanstalk](../00_includes/05_AWS_II/44.S3Bucket.png)
4. Amazon CloudWatch alarms
![Beanstalk](../00_includes/05_AWS_II/45.Cloudwatch.png)
5. An AWS CloudFormation stack
![Beanstalk](../00_includes/05_AWS_II/46.Cloudformationstack.png)
6. A domain name

