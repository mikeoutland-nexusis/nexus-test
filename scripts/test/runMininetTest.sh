#!/bin/bash

echo "Positive Testcases:"
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h1 h2"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h1 h3"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h2 h1"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h2 h3"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h3 h1"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h3 h2"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h4 h5"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h4 h6"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h5 h6"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h5 h4"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h6 h4"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h6 h5"
echo "Negative Testcases"
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h1 h4"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h1 h5"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h1 h6"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h2 h4"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h2 h5"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h2 h6"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h3 h4"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h3 h5"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h3 h6"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h4 h1"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h4 h2"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h4 h3"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h5 h1"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h5 h2"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h5 h3"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h6 h1"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h6 h2"
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h6 h3"
sleep 1