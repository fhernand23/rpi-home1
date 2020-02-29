#!/bin/bash

# This script will enable IR movement sensor

# Change to Desktop directory
cd /home/pi/hometasks

# log process start
echo "`date` - start activate_system" > log_files/rpht.log

# start flask app
python3 app.py

# TODO enable IR sensor
