#!/bin/bash

# This script will enable IR movement sensor

# Change to Desktop directory
cd /home/pi/rpi-home1

# log process start
echo "`date` - start activate_system" > log_files/app.log

# start app
export LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1
nohup python3 app_silent.py > ./log_files/app.log &

# TODO enable IR sensor
