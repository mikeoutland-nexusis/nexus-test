#!/bin/bash

ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && /home/ubuntu/stopSys.sh $1"
echo "connecting to mininet to stop /home/ubuntu/stopSys.sh $1 at $2"
