#!/bin/bash
#set -vx

# JTDS driver - jtds-1.3.1.jar - should be copied to /usr/lib/sqoop/lib/ folder
aws s3 rm s3://barrick-bdf-dev/tmp/prta/ --recursive

sqoop import \
 --connect "jdbc:jtds:sqlserver://10.133.53.43:1433/PowerView" \
 --connection-manager org.apache.sqoop.manager.SQLServerManager \
 --query 'select * from dbo.ptra where $CONDITIONS' \
 --driver net.sourceforge.jtds.jdbc.Driver \
 --username sgroup \
 --password sgroup \
 --target-dir s3://barrick-bdf-dev/tmp/prta \
 --num-mappers 1 \
 --as-avrodatafile \
 --compression-codec snappy

#--target-dir hdfs:///user/hive/warehouse/ptra \
