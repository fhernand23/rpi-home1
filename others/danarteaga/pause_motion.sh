#!/bin/bash

# Created by Dan Arteaga

# This script will pause motion detection

# Change to the Desktop directory
cd /home/pi/Desktop

# log process start
echo "`date` - start pause_motion" > txt_files/rphs.log

/usr/bin/wget -q -O /dev/null "192.168.1.80:8086/0/detection/pause"
