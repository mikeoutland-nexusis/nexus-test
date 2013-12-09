#!/bin/bash

scp -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $1/mininet/custom/*.py $2:/home/ubuntu/mininet/custom
scp -i ~/.ssh/id_rsa -o StrictHostKeyChecking=false $1/scripts/test/remote/*.sh $2:/home/ubuntu/
echo "Transferring custom py's to Mininet at $2"