#!/bin/bash
notification="ceilometer_notification"
central="ceilometer_central"
compute="ceilometer_compute"

for loop in "" "ZC-Controller-0201" "ZC-Compute-0102" "ZC-Compute-0103" "ZC-Compute-0104" "ZC-Compute-0202" "ZC-Compute-0203"
do
    if [[ ${loop} = "" ]]
    then
        docker restart ${notification} ${central}
    elif [[ ${loop} = "ZC-Controller-0201" ]]
    then
        ssh ${loop} docker restart ${notification} ${central}
    else
        ssh ${loop} docker restart ${compute}
    fi
    sleep 3
done
