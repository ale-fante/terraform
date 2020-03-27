Infrastructure as Code!
-----------------------

There are various types of tools that can allow you to deploy infrastructure as code: Terraform, CloudFormation, Heat, Ansible, SaltStack, Chef, Puppet and others.

Which tool to use?
------------------
Ansible, Chef, Puppet are configuration management tools which means that they are primarily designed to install and manage software on existing servers.

Terraform, CloudFormation are orchestration tools which basically means they can provision the servers and infrastructure by themselves. 

Configuration Management tools can do some degree of infrastructure provisioning; however it's good to consider some tools are going to be better for certain type of tasks.

(e.g. Ansible can be used to launch ec2 instances just like in Terraform)


Install Terraform
=================

To install on mac:
------------------

	$ brew install terraform

(Brew takes care of the environment part)

On linux:
---------

1. Download binary from https://www.terraform.io/downloads.html
2. Or through the terminal:

		$ wget https://releases.hashicorp.com/terraform/0.12.20/terraform_0.12.20_linux_amd64.zip

  - move to root
  - unzip terraform_0.12.20_linux_amd64.zip

AWS Management Console
======================
1) Go to AWS management console
2) Go to users
3) Create new user with programmatic access
4) Attach existing policies with admin access
5) Create user

You will then get an access key ID and a secret access key

Launch first server through Terraform
=====================================

1) Select provider. In this example, we will be using the AWS provider:
	https://www.terraform.io/docs/providers/aws/index.html

2) Select type of credentials. For authentication, we will use static credentials.


		provider "aws" {
  			region     = "us-west-2"
  			access_key = "my-access-key"
  			secret_key = "my-secret-key"
		}

3) Go into AWS Management Console. From Services, select IAM.
4) From the menu, select users.
	- Create New user (programatic access) > Attach existing policies > Admin access
5) Access Key and Secret key will be created.


		mkdir terraformfiles
		
6) Within the directory, create file: first_ec2.tf

7) Set up initial configuration on first_ec2.tf file

		provider "aws" { 
			# Specify which region
  			region = "XXX"
			# Add user keys
  			access_key = "XXXXXXXXXXXXX"
  			secret_key = "XXXXXXXXXXXXXCXXXXX"
		}

8) Specify the resource type within first_ex2.tf (Review Argument Reference: https://www.terraform.io/docs/providers/aws/d/instance.html)


		resource "aws_instance" "myecc2" {
			# aws_instance = resource name
			# lb = name we have given this resource  [aws_eip.lb or for the one below aws_s3_bucket.mys3]
			# Note that every region has a different AMI ID.
			ami = "XXXXXXXXX" 
			instance_type = "t2.micro"
		}
		
		
- Select operating system, configure instance details
- copy ami ID (changes depending on the region)

		
9) Save and and run:	

		$ terraform init

 - Notice that another folder is automatically created. 

		$ terraform plan

 - This last command will display the terraform plan. (Displaying the configurations you've set)

		$ terraform apply

 - This last command will apply the configuration you've specified.


Terraform Destroy
=================

- This command checks for the resources that were created. 

		$ terraform destroy 


 - To target a specific instance:
 
		$ terraform destroy -target aws_instance.myec2


Terraform State files
=====================

- All the information from the state file is displayed
  
  	$ terraform show 


