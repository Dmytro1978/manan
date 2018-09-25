#!/bin/bash
#set -vx

aws s3 rm s3://s3_bucket/folder/folder/ --recursive

sqoop import \
 --connect "jdbc:oracle:thin:<user_name>/<pwd>@<host>:<port>/<instance>" \
 --query 'select * from <table> where $CONDITIONS' \
 --target-dir s3://s3_bucket/folder/folder \
 --num-mappers 1 \
 --as-avrodatafile \
 --compression-codec snappy


#--target-dir hdfs:///user/hive/warehouse/ptra \
