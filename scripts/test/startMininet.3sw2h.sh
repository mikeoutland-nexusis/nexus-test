#!/bin/bash
# Change the --topo varable to reflect the topology class you are running
# Current choices available
#   TwoSwFourHostTopo
#   ThreeSwTwoHostPerTopo
# Don't forget to change runner file to reflect topo changes
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "/home/ubuntu/runSys.sh $1 --custom mininet/custom/topo3Sw2HostPer.py --topo ThreeSwTwoHostPerTopo"
echo "connecting to mininet to execute: /home/ubuntu/runSys.sh $1 at $2"
sleep 5 