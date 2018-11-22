#!/bin/bash
#set -vx

. db_params_ora.cfg

aws s3 rm s3://${target_dir_s3_xml}/ --recursive

sqoop import \
    -Dmapreduce.job.user.classpath.first=true \
    --connect "jdbc:oracle:thin:${user_name}/${password}@${host}:${port}/${instance}" \
    --query 'select t.id, t.name, t.xml_body.getStringVal() xml_body from xml_test t where $CONDITIONS' \
    --target-dir s3://${target_dir_s3_xml} \
    --num-mappers 1 \
    --as-avrodatafile \
    --compression-codec snappy \
    --null-string '' \
    --null-non-string '' 

