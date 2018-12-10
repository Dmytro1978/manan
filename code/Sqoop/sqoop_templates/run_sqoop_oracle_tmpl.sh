#!/bin/bash
#set -vx

# if target dir is in HDFS (an alternative to --delete-target-dir):
# hadoop fs -rm -r /user/hive/warehouse/<table_name>

# if target dir is in S3:
aws s3 rm s3://s3_bucket/folder/folder/ --recursive

sqoop import \
    -Dmapreduce.job.user.classpath.first=true \
    --connect "jdbc:oracle:thin:<user_name>/<pwd>@<host>:<port>/<instance>" \
    --query 'select * from <table> where $CONDITIONS' \
    --target-dir s3://s3_bucket/folder/folder \
    --num-mappers 1 \
    --null-string '' \
    --null-non-string '' 

# if target file format is CSV:
#    --fields-terminated-by '\t' 
#    --lines-terminated-by '\n' 
# if target file format is Avro:
#    --as-avrodatafile
#    --compression-codec snappy
# if target dir is in HDFS:
#    --delete-target-dir
#    --target-dir hdfs:///user/hive/warehouse/<table_name>
# if source table contains LOB objects:
#  --inline-lob-limit <int>
# if target file format is Avro and there are date/time columns in the table:
# --map-column-java <column1>=String,<column2>=String,..,<columnN>=String