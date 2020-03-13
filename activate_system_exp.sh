#!/bin/bash

# This script will enable IR movement sensor

# Change to Desktop directory
cd /home/pi/rpi-home1

# log process start
echo "`date` - start activate_system" > log_files/rpht.log

# start flask app
nohup python3 app-silent_exp.py > ./log_files/output.log &

# TODO enable IR sensor
