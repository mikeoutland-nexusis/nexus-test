#!/bin/bash

screen -d -m -S $1 sudo mn $2 --mac --switch ovsk --controller=remote