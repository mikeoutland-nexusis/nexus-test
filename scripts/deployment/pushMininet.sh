#!/bin/bash

scp -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $1/mininet/custom/*.py ubuntu@ec2-54-202-78-146.us-west-2.compute.amazonaws.com "/home/ubuntu/mininet/custom"
scp -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $1/scripts/test/remote/*.sh ubuntu@ec2-54-202-78-146.us-west-2.compute.amazonaws.com "/home/ubuntu/"
echo "Transferring custom py's to Mininet"