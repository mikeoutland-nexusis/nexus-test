#!/bin/bash

echo "Testcases:"
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runCmd.sh $1 pingall"
sleep 1
