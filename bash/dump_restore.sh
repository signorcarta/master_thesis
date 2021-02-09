#!/bin/bash

###################
#
###################

dump_folder=/data/mysql/backup/dump_folder

echo "######################################################"
echo "# You are about to start a dump | restore operation. #"
echo "######################################################"

echo ""

## Insert SRC host and port
echo "Insert src host: "
read src_host
echo ""
echo "Insert port: "
read src_port

echo ""

## Insert DEST host and port
echo "Insert dest host:"
read dest_host
echo ""
echo "Insert port"
read dest_port

## Perform dump
echo ""
echo "Dumping instance $src_host on port $src_port ..."
time mysqldump --login-path=read-only --port $src_port --host $src_host --single-transaction --all-databases --verbose --add-locks > $dump_folder/dump_from_script.sql
echo "---> Dump completed"
echo ""

sleep 10s
echo "Press any key: "
read char

## Perform restore
echo ""
echo "Restoring instance $dest_host" on port $dest_port ...
time mysql --login-path=root-vlsidbalab001 --port $dest_port --host $dest_host < $dump_folder/dump_from_script.sql
echo "---> Restore completed"
echo ""
