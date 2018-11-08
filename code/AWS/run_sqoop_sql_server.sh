#!/bin/bash
#set -vx

aws s3 rm s3://s3_bucket/folder/folder/ --recursive

sqoop import \
 --connect "jdbc:sqlserver://<host>:<port>;database=<database_name>" \
 --query 'select * from schema.table where $CONDITIONS' \
 --username <user_name> \
 --password <password> \
 --target-dir s3://s3_bucket/folder/folder \
 --num-mappers 1 \
 --as-avrodatafile \
 --compression-codec snappy


#--target-dir hdfs:///user/hive/warehouse/ptra \
