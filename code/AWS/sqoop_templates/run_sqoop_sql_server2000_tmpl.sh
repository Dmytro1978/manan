#!/bin/bash
#set -vx

# JTDS driver - jtds-1.3.1.jar - should be copied to /usr/lib/sqoop/lib/ folder

# if target dir is in HDFS (an alternative to --delete-target-dir):
# hadoop fs -rm -r /user/hive/warehouse/<table_name>

# S3:
aws s3 rm s3://s3_bucket/folder/folder/ --recursive

sqoop import \
 --connect "jdbc:jtds:sqlserver://<host>:port/<database_name>" \
 --connection-manager org.apache.sqoop.manager.SQLServerManager \
 --query 'select * from schema.table where $CONDITIONS' \
 --driver net.sourceforge.jtds.jdbc.Driver \
 --username <user_name> \
 --password <pwd> \
 --target-dir s3://s3_bucket/folder/folder \
 --num-mappers 1

# if target file format is CSV:
#    --fields-terminated-by '\t' 
#    --lines-terminated-by '\n' 
# if target file format is Avro:
#    --as-avrodatafile
#    --compression-codec snappy
# if target dir is in HDFS:
#    --target-dir hdfs:///user/hive/warehouse/<table_name>
# if source table contains LOB objects:
#  --inline-lob-limit <int>
# if target file format is Avro and there are date/time columns in the table:
# --map-column-java <column1>=String,<column2>=String,..,<columnN>=String
