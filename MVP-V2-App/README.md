
# Welcome to my Finale project!
  
  Over the past few months, I have immersed myself in cloud technologies and applied my learning to various smaller tasks. Now, all this knowledge will culminate in my capstone project, where I aim to enhance and automate an existing system.

My task involves assisting a company with their cloud migration efforts. After a thorough infrastructure analysis by a previous team, a comprehensive diagram of the current setup has been created.

My role will be to translate this design into cloud infrastructure using Infrastructure as Code (IaC) principles, leveraging the AWS Cloud Development Kit (CDK) with Python.

Throughout the project, I will navigate through company policies, user requirements, colleague input etc. to ensure that the design is aligned with company policies. 

You can visit the following documents for more information on the project: 

## Working MVP Application

Explore the latest version of our Minimum Viable Product (MVP) here. This section includes detailed instructions on how to build and deploy the application successfully. You'll also find information on how to tag or release different versions for easy identification. Additionally, we provide documentation on how to interact with the application, including the required arguments and necessary permissions for deployment on AWS or Azure.

## Design Documentation

Delve into the intricacies of our architecture in this section. We'll walk you through the existing architecture, highlighting areas that require further elaboration. You'll find practical and technical details, such as Network Security Group (NSG) rules, as well as visualization of the deployment sequence in the cloud. In version 1.1, we'll introduce our own diagrams illustrating modifications and justify improvements made.

## Decision Documentation

Understand the rationale behind our design decisions and strategic choices in this section. We'll outline the considerations that influenced our selection of services and technologies, providing insights into our decision-making process. Additionally, you'll find a comprehensive list of assumptions and potential enhancements that serve as the foundation for our design documentation.

## Time Logs

Track our project's development journey through our detailed time logs. Each entry provides a succinct summary of our daily activities, highlighting the tasks undertaken and obstacles encountered. We'll also share the solutions we devised to overcome these challenges, offering valuable insights into our problem-solving approach.

---

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
