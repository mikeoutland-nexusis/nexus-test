#!/bin/bash

ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "(export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h1 h2) || exit -1"
if [ $? -ne 0 ]
then
	exit 1
fi
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "(export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h1 h6) || exit -1"
if [ $? -ne 0 ]
then
	exit 1
fi
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "(export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h4 h5) || exit -1"
if [ $? -ne 0 ]
then
	exit 1
fi
sleep 1
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "(export TERM=xterm-256color && exec /home/ubuntu/runPingTest.sh $1 h4 h6) || exit -1"
if [ $? -ne 0 ]
then
	exit 1
fi
sleep 1