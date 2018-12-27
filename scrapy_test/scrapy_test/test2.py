#!/bin/bash
c_path_1=/etc/kolla/ceilometer-notification/ceilometer.conf
p_path_1=/etc/kolla/ceilometer-notification/pipeline.yaml
c_path_2=/etc/kolla/ceilometer-compute/ceilometer.conf
p_path_2=/etc/kolla/ceilometer-compute/pipeline.yaml
c_path_3=/etc/kolla/ceilometer-central/ceilometer.conf
p_path_3=/etc/kolla/ceilometer-central/pipeline.yaml

scp $c_path_1 ZC-Controller-0201:$c_path_1
scp $p_path_1 ZC-Controller-0201:$p_path_1
scp $c_path_1 ZC-Controller-0201:$c_path_3
scp $p_path_1 ZC-Controller-0201:$p_path_3


scp $c_path_1 ZC-Compute-0102:$c_path_2
scp $p_path_1 ZC-Compute-0102:$p_path_2

scp $c_path_1 ZC-Compute-0103:$c_path_2
scp $p_path_1 ZC-Compute-0103:$p_path_2

scp $c_path_1 ZC-Compute-0104:$c_path_2
scp $p_path_1 ZC-Compute-0104:$p_path_2

scp $c_path_1 ZC-Compute-0202:$c_path_2
scp $p_path_1 ZC-Compute-0202:$p_path_2

scp $c_path_1 ZC-Compute-0203:$c_path_2
scp $p_path_1 ZC-Compute-0203:$p_path_2

