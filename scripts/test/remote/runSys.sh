#!/bin/bash

cd opendaylight
nohup ./run.sh &
cd ..
sleep 10
screen -d -m -S $1 sudo mn $2 $3 $4 $5 --mac --switch ovsk --controller=remote,ip=127.0.0.1,port=6633