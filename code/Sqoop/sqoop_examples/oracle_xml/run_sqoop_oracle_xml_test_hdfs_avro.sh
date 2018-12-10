#!/bin/bash
#set -vx

. db_params_ora.cfg

sqoop import \
    -Dmapreduce.job.user.classpath.first=true \
    --connect "jdbc:oracle:thin:${user_name}/${password}@${host}:${port}/${instance}" \
    --query 'select t.id, t.name, t.xml_body.getStringVal() xml_body from xml_test t where $CONDITIONS' \
    --delete-target-dir \
    --target-dir hdfs:///${target_dir_hdfs_xml} \
    --num-mappers 1 \
    --as-avrodatafile \
    --compression-codec snappy \
    --null-string '' \
    --null-non-string '' 

