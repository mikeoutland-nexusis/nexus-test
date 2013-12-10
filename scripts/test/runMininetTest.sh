#!/bin/bash

ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && /home/ubuntu/runPingTest.sh $1 h1 h2"
sleep 2
echo $?
if [ "$?" -ne "0" ]
then
	echo 'error in test' > /dev/stderr
	exit -1
fi
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && /home/ubuntu/runPingTest.sh $1 h1 h3"
sleep 2
echo $?
if [ "$?" -ne "0" ]
then
	echo 'error in test' > /dev/stderr
	exit -1
fi
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && /home/ubuntu/runPingTest.sh $1 h4 h1"
sleep 2
echo $?
if [ "$?" -ne "0" ]
then
	echo 'error in test' > /dev/stderr
	exit -1
fi
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $2 "export TERM=xterm-256color && /home/ubuntu/runPingTest.sh $1 h4 h6"
sleep 2
echo $?
if [ "$?" -ne "0" ]
then
	echo 'error in test' > /dev/stderr
	exit -1
fi