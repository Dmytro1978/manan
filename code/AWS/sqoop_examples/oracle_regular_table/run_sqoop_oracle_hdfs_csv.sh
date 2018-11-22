#!/bin/bash
#set -vx

. db_params_ora.cfg

sqoop import \
 -Dmapreduce.job.user.classpath.first=true \
 --connect "jdbc:oracle:thin:${user_name}/${password}@${host}:${port}/${instance}" \
 --num-mappers 1 \
 --query 'select * from '${table_name}' where $CONDITIONS' \
 --delete-target-dir \
 --target-dir hdfs:///${target_dir_hdfs_csv} \
 --fields-terminated-by '\t' \
 --lines-terminated-by '\n' \
 --null-string '' \
 --null-non-string '' 

