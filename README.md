# HelloWorld
#Overview

This is a HelloWorld application and when you run it, it will take logs and pass them through the ElasticSearch and then you can view it in Kibana. 

#Prerequisites

You will need:
- Python latest version installed
- Terraform installed in Visual Studio Code
- Filebeat installed
- Ansible installed
- This repo cloned


#Setup and Execution

- run python file helloWorld.py to see "env var is visible USER:" printed in the terminal and see the folder where been created a new file test.log which also prints outputs in the file

- run playbook.yaml, which takes variable from data.yaml and creates helloWorld.py file (delete existing file to see its created)

- run terraformAppR.tf to build and manage the infrastructure

- run Filebeat (change directory/open new terminal) so he logs can be easily found in the kibana

- open ElasticSearch and search for "filebeat_test_rimma", then go to kibana dashboard and you can see saved visualisation of data

