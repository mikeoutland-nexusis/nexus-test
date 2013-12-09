#!/bin/bash

ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false ubuntu@ec2-54-202-78-146.us-west-2.compute.amazonaws.com "/home/ubuntu/runSys.sh $1 --custom custom/topo3Sw2HostPer.py --topo ThreeSwTwoHostPerTopo"
echo "connecting to mininet to execute: /home/ubuntu/runSys.sh $1"
sleep 5 