#!/bin/bash

##################################################################
# This script simply takes you to the /data/mysql/scripts/ folder #
##################################################################

cd /data/mysql/scripts/

dir=$(pwd)
echo "You are now in $dir"
echo "Press Ctrl+D to exit the sub-shell"
echo ""
$SHELL
