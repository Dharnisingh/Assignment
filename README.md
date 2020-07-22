Description:
============
 # Implemention of REST api using python Flask
 # Api will allow users to access the message using URI and through UI
 # Application will running on docker container

Build, Deploy, Access:
=====================
 # Fetch the code from Github "https://github.com/Dharnisingh/Assignment.git"
 # Deploy the code using AWS codeDeploy
 # Deployment is described in appspec.yml file
 # Once deployment is successful app can be accessed usingh DNS of AWS EC2 instance 

REST API documentation
======================
 # To access the list of messages: 
   domain-name:5001/list
 # To find a message
   domain-name:/find/your_message
 # To add a message:
   domain-name:/add/your_message
 # To delete a message:
   domain-name:/delete/your_message
