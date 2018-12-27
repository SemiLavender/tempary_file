#!/usr/bin/env bash

for loop in "ZC-Controller-0201" "ZC-Compute-0102" "ZC-Compute-0103" "ZC-Compute-0104" "ZC-Compute-0202" "ZC-Compute-0203"
do
    ssh ${loop} mkdir -p /etc/zabbix/script/logs
    scp /etc/zabbix/script/logs/logs_discovery.py ${loop}:/etc/zabbix/script/logs/logs_discovery.py
    ssh ${loop} chmod a+x /etc/zabbix/script/logs/logs_discovery.py
    scp /etc/zabbix/zabbix_agentd.conf.d/logs_discovery.conf ${loop}:/etc/zabbix/zabbix_agentd.conf.d/logs_discovery.conf
    ssh ${loop} service zabbix-agent restart
done 