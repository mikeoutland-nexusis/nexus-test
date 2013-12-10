#!/bin/bash

ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $3 "export TERM=xterm-256color && /home/ubuntu/runCmd.sh $1 $2"
echo "connecting to mininet to execute: /home/ubuntu/runCmd.sh $1 $2 at $3"
sleep 10