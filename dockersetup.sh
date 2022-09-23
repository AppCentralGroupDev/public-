#!/bin/bash

#install git 
sudo yum -y git

#removing older versions of docker 

sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine


#yum and yum utils package 
sudo yum install -y yum-utils

#repository setup with 
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

# package updates
sudo yum check-update
sudo yum update 

#docker engine installation 

sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# If prompted to accept the GPG key, verify that the fingerprint matches 
# 060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35, and if so, accept it.



#start docker 

sudo systemctl start docker

# verify docker is running 

sudo docker run hello-world


#stop container 

sudo docker run hello-world


#add user to docker group 

sudo usermod -aG docker "$1"



