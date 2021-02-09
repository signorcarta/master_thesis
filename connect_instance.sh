#!/bin/bash

##################
#                #
##################

host=vlsidbalab001

echo "##########################"
echo "# Connecting to instance #"
echo "##########################"
echo ""
echo "Insert port: "

read port
mysql --login-path=root-vlsidbalab001 --port=$port --host=$host --verbose
