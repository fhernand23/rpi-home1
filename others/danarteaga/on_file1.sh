#!/bin/bash

# Created by Dan Arteaga

# This script will create the file motion_files.txt when the camera detects motion

# Change to the Desktop directory
cd /home/pi/Desktop

# log process start
echo "`date` - start on_file1" > txt_files/rphs.log

# Create the file
sudo echo -n 1 > /home/pi/Desktop/txt_files/motion_files.txt
