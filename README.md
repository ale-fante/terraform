To activate env: source venv/bin/activate

# terraform
## To install on mac:

$ brew install terraform

(Brew takes care of the environment part)

## on linux:

Download package
on history, right click on downloaded package and select "copy link address" from the drop down

### On the terminal:

wget https://releases.hashicorp.com/terraform/0.12.20/terraform_0.12.20_linux_amd64.zip

- move to root
- unzip terraform_0.12.20_linux_amd64.zip

____________________________________
____________________________________

1) Download Atom
2) On Atom, go to "Install a package"
3) install language-terraform plugin
4) Add terraform project folder to Atom
5) Open examle.tf.txt
6) To start, we will use the AWS provider
7) Get AWS Free Tier personal account
____________________________________
____________________________________


*************************************************************************************
1) Go to AWS management console
2) Go to users
3) Create new user with programmatic access
4) Attach existing policies with admin access
5) Create user

You will then get an access key ID and a secret access key

- Create a folder
- Open it on atom
- Right click, and create a new file named first_ec2.tf

For authentication, use static credentials.

- Get aws provider access usage code snippet:

provider "aws" {
	region = ""
	access_key = ""
	secret_key = ""
}
*************************************************************************************

Spin up a server:

EC2 Resource > Resources > aws_instance

resource "aws_instance"  "myec2" {
	# Required fields
	ami = " "
	insstance_type = "t2.micro"  # This is the free tier option
}

Select operating system, configure instance details
copy ami ID (changes depending on the region)

*************************************************************************************

Go to the folder you created on the terminal
Run:

$ terraform init

- Notice that another folder is automatically created. 

$ terraform plan

This last command will display the terraform plan. (Displaying the configurations you've set)


$ terraform apply

This last command will apply the configuration you've specified

*************************************************************************************


Note that every region has a different AMI ID. The AMI ID's keeps on changing so make sure you use the latest AMI ID from the AWS console similar to the way it is shown in the video.


Resource Code:

https://github.com/zealvora/terraform-beginner-to-advanced-resource/blob/master/section01/first_ec2.tf

*************************************************************************************

Providers:

- Terraform has several providers. 
- Depending upon where you want to launch your infrastructure
- Look for appropriate provider, depending on your need. 

You must add specific authentication tokens for the given provider. 

- Terraform downloads the appropriate provider plugins. 

Google: Terraform providers
- Terraform categorizers providers by category. 
- The provider name cannot change because it's a name given by Terraform


# create new file

- bitbucket.tf


Paste provider details there

provider "bitbucket" {
	username = "GobBluthe"
	password = "idoillusions"
}

run $ terraform init # this downloads the plugin associated with the bitbucket provider
$ terraform plan  #this will give an error

$ terraform init  #this will actually download the plugin associated with the provider

$ terraform apply


Resources:
- Resources are the reference to an individual service.
- e.g. For a service of ec2 you will have some resources...


resource "" {
	... add required arguments ... 
}

See https://github.com/zealvora/terraform-beginner-to-advanced-resource/blob/master/section01/first_ec2.tf

$ terraform init

$ terraform plan

*************************************************************************************

Terraform Destroy

# This command checks for the resources that were created. 
$ terraform destroy 


# To target a specific instance:
$ terraform destroy -target aws_instance.myec2



*************************************************************************************
State files

- Have all the information associated with specific instances.
- State files associated with resources get removed when resources get destroyed

terraform.tfstate file has metadata information about terraform version, etc. 

$ terraform apply

# To create a new ec2 instance. 
$ yes

$ terraform plan

# Verify what the plan is before you run:
$ terraform apply

************************************************************************************

Desired state and current state

  i) Desired State: EC2 = instance_type = "t2.micro"  # What is explicitly stated in code. If you don't specify it, terraform will not do anything there. Always mention things on your code so it becomes part of the desired state.

  ii) Current state: "instance_state": "stopped", && "instance_type": "t2.nano"

  Desired state == current state

Go back to the console and stop the ec2 instance. Change the type to t2.nano

$ terraform refresh # fetches the information 

# You will note that the state file will be updated

 $terraform plan

# The state is being refreshed. 

 $ terraform apply

# In a production environment, the desired state and the current state are different. 

************************************************************************************

Terraform commands: State files

# All the information from the state file is displayed
  $ terraform show 

earlier: security group is default.


************************************************************************************

Understanding Attributes

Terraform has a capability to output the attribute of a resource with the output values

add a attributes.tf file


Go to the console

Open Elastic IPs

Copy elastic IP


	resource "aws_eip" "lb" {
		# aws_eip = resource name
		# lb = name we have given this resource  [aws_eip.lb or for the one below aws_s3_bucket.mys3]
		vpc = true
	}

	output "eip" {
		value = aws_eip.lb.public_ip
	}



	resource "aws_s3_bucket" "mys3" {
		bucket = "kplabs-attribute-demo-001"
	}

	output "mys3bucket" "mys3"{
		bucket = "kplabs-attribute-demo-001"
	}

$ terraform apply

Under the outputs secion, terraform provides the output values. It becomes easier to look at the outputs instead of going to the console

In documentation: look for attributes reference

https://github.com/zealvora/terraform-beginner-to-advanced-resource/blob/master/section02/attributes.tf



************************************************************************************

Create a new file

reference.tf

  Add resources... 
  
  Then run $ terraform plan

aws_eip_associationHave
https://github.com/zealvora/terraform-beginner-to-advanced-resource/blob/master/section02/reference.tf



Instances:https://www.terraform.io/docs/providers/aws/r/instance.html
