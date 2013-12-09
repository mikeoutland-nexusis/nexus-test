#!/bin/bash

ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "/home/ubuntu/runSys.sh $1 --custom custom/topo3Sw2HostPer.py --topo ThreeSwTwoHostPerTopo"
echo "connecting to mininet to execute: /home/ubuntu/runSys.sh $1 at $2"
sleep 5 