# Provisioners

This feature makes terraform more interesting. 

Until now we have been working on creation and destruction of infrastructure scenarios

Let's take an example:
 - Say we created a web-server EC2 instance with Terraform 
 Problem: it's only an EC2 instance, it doesn't have any software installed?
 
 What if you want a complete end to end solution? 
 
 ##### Provisioners are used to execute scripts on local or remote machines as part of resource creation or destruction
 
 As an example: On creation of Web-server, execute a script which installs nginx web-server.
 
 Create EC2. -> install Nginx webserver
 
 ## DEMO:
 
 provisioners.tf
 
resource "aws_instance" "myec2" {
	ami = "ami-0ce21b51cb31a48b8"
	instance_type = "t2.micro"
  
provisioner "remote-exec" {
inline = [
  "sudo amazon-linux-extras install -y nginx1.12"
  "sudo systemctl start"
]
}




save

run 
terraform plan
terraform apply
