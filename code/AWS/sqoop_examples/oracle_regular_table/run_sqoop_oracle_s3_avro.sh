#!/bin/bash
#set -vx

. db_params_ora.cfg

aws s3 rm s3://${target_dir_s3_avro}/ --recursive

sqoop import \
 -Dmapreduce.job.user.classpath.first=true \
 --connect "jdbc:oracle:thin:${user_name}/${password}@${host}:${port}/${instance}" \
 --num-mappers 1 \
 --query 'select * from '${table_name}' where $CONDITIONS' \
 --target-dir s3://${target_dir_s3_avro} \
 --map-column-java CREATE_DATE=String,UPDATE_DATE=String \
 --as-avrodatafile \
 --compression-codec snappy \
 --null-string '' \
 --null-non-string '' 

