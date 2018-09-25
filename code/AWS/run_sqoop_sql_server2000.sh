#!/bin/bash
#set -vx

aws s3 rm s3://s3_bucket/folder/folder/ --recursive

sqoop import \
 --connect "jdbc:jtds:sqlserver://host:port/database_name" \
 --connection-manager org.apache.sqoop.manager.SQLServerManager \
 --query 'select * from schema.table where $CONDITIONS' \
 --driver net.sourceforge.jtds.jdbc.Driver \
 --username sgroup \
 --password sgroup \
 --target-dir s3://s3_bucket/folder/folder \
 --num-mappers 1 \
 --as-avrodatafile \
 --compression-codec snappy

#--target-dir hdfs:///user/hive/warehouse/ptra \
