#!/bin/bash

for loop in "ZC-Controller-0101" "ZC-Compute-0102" "ZC-Compute-0103" "ZC-Compute-0202"
do
    ssh ${loop} sudo service zabbix-agent status
done