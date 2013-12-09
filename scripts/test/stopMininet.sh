#!/bin/bash

ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false ubuntu@ec2-54-202-78-146.us-west-2.compute.amazonaws.com "export TERM=xterm-256color && /home/ubuntu/stopSys.sh $1"
echo "connecting to mininet to stop /home/ubuntu/stopSys.sh $1"
